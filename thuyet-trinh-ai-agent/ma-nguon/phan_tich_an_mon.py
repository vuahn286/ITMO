"""
Phân tích dữ liệu ăn mòn khí quyển (DỮ LIỆU GIẢ LẬP – dùng cho demo).

Đây là loại mã mà AI Agent tự viết và chạy trong Demo 2. Giữ lại để:
  - đối chiếu với kết quả AI tạo ra khi chạy lại trên Claude;
  - minh họa "mã tái lập" (ai chạy cũng ra cùng kết quả).

Chạy:  python3 phan_tich_an_mon.py
Đầu ra: thư mục ../ket-qua-mau/
"""
from pathlib import Path
import re
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "du-lieu-demo"
OUT = ROOT / "ket-qua-mau"
OUT.mkdir(exist_ok=True)

KHOI_LUONG_RIENG = {"Thep_CT3": 7.85, "Kem": 7.14, "Dong": 8.96, "Nhom": 2.70}  # g/cm³
# Ngưỡng tốc độ ăn mòn năm đầu (g/m²·năm) – ISO 9223:2012, Bảng 2.
# Đã đối chiếu: thép, kẽm (cả 6 cấp); đồng, nhôm (C1–C3).
# Đồng, nhôm từ C4 trở lên: CẦN ĐỐI CHIẾU BẢN GỐC trước khi dùng chính thức.
ISO9223 = {
    "Thep_CT3": [10, 200, 400, 650, 1500, 5500],
    "Kem":      [0.7, 5, 15, 30, 60, 180],
    "Dong":     [0.9, 5, 12, 25, 50, 90],
    "Nhom":     [0, 0.6, 2, 5, 10, np.inf],
}
CAP = ["C1", "C2", "C3", "C4", "C5", "CX"]
TEN_TRAM = {"TRAM_BIEN": "Trạm ven biển", "TRAM_DOTHI": "Trạm đô thị", "TRAM_NOIDIA": "Trạm nội địa"}
TEN_KL = {"Thep_CT3": "Thép CT3", "Kem": "Kẽm", "Dong": "Đồng", "Nhom": "Nhôm"}

log = []          # nhật ký kiểm tra chất lượng dữ liệu
def ghi(muc, ma, mo_ta, xu_ly):
    log.append(dict(loai_loi=muc, ma_mau=ma, mo_ta=mo_ta, xu_ly=xu_ly))

# ---------------------------------------------------------------- 1. Đọc và làm sạch
raw = pd.read_csv(DATA / "an_mon_tho.csv", dtype=str, keep_default_na=False)
df = raw.copy()

dup = df.duplicated(keep="first")
for ma in df.loc[dup, "ma_mau"]:
    ghi("Trùng dòng", ma, "Dòng lặp lại hoàn toàn", "Xóa bản trùng")
df = df[~dup].copy()

chuan = df["tram"].str.strip().str.upper().str.replace(" ", "_")
for ma, a, b in zip(df.ma_mau, df.tram, chuan):
    if a != b:
        ghi("Tên trạm không thống nhất", ma, f"'{a}'", f"Chuẩn hóa thành {b}")
df["tram"] = chuan

def so(x, ma, cot):
    s = x.strip()
    if s == "":
        ghi("Thiếu số liệu", ma, f"{cot} trống", "Loại khỏi phân tích, giữ trong dữ liệu gốc")
        return np.nan
    s2 = re.sub(r"[^\d,.\-]", "", s).replace(",", ".")
    if s2 != s:
        ghi("Sai định dạng số", ma, f"{cot} = '{s}'", f"Chuyển thành {s2}")
    return float(s2)

for cot in ["khoi_luong_truoc_g", "khoi_luong_sau_g"]:
    df[cot] = [so(v, m, cot) for v, m in zip(df[cot], df.ma_mau)]
df["dien_tich_cm2"] = df["dien_tich_cm2"].astype(float)
df["thoi_gian_thang"] = df["thoi_gian_thang"].astype(int)

def ngay(x, ma):
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", x):
        return pd.Timestamp(x)
    ghi("Sai định dạng ngày", ma, f"ngay_thu_mau = '{x}'", "Chuyển về YYYY-MM-DD")
    return pd.to_datetime(x, dayfirst=("/" in x and x.index("/") == 2))
df["ngay_thu_mau"] = [ngay(v, m) for v, m in zip(df.ngay_thu_mau, df.ma_mau)]

for ma, g in zip(df.ma_mau, df.ghi_chu):
    if g:
        ghi("Ghi chú thực nghiệm", ma, g, "Giữ lại, đánh dấu để nhà khoa học xem xét")

# ---------------------------------------------------------------- 2. Tính tổn thất
df["ton_that_g_m2"] = (df.khoi_luong_truoc_g - df.khoi_luong_sau_g) / (df.dien_tich_cm2 / 1e4)
df["t_nam"] = df.thoi_gian_thang / 12

am = df.ton_that_g_m2 < 0
for ma in df.loc[am, "ma_mau"]:
    ghi("Giá trị phi vật lý", ma, "Khối lượng sau > trước (tổn thất âm)", "Loại – đề nghị kiểm tra sổ cân")
df.loc[am, "ton_that_g_m2"] = np.nan

# Ngoại lệ: mỗi nhóm chỉ có 3 mẫu lặp nên không dùng z-score/MAD (lần chạy đầu
# đánh dấu nhầm 20 giá trị bình thường). Dùng quy tắc: lệch > 30% so với
# trung bình hai mẫu lặp còn lại → đánh dấu.
NGUONG = 0.30
df["ngoai_le"] = False
for _, g in df.groupby(["tram", "kim_loai", "thoi_gian_thang"]):
    v = g.ton_that_g_m2.dropna()
    if len(v) < 3:
        continue
    for i in v.index:
        ref = v.drop(i).mean()
        if abs(v[i] - ref) / ref > NGUONG:
            df.loc[i, "ngoai_le"] = True
            ghi("Ngoại lệ thống kê", df.loc[i, "ma_mau"],
                f"{v[i]:.1f} g/m², lệch {100 * (v[i] - ref) / ref:+.0f}% so với 2 mẫu lặp ({ref:.1f})",
                "Loại khỏi mô hình – đề nghị kiểm tra sổ cân")

sach = df[df.ton_that_g_m2.notna() & ~df.ngoai_le].copy()
sach["ton_that_um"] = sach.ton_that_g_m2 / sach.kim_loai.map(KHOI_LUONG_RIENG)  # g/m² ÷ g/cm³ = µm

pd.DataFrame(log).to_csv(OUT / "bao_cao_chat_luong_du_lieu.csv", index=False, encoding="utf-8-sig")
sach.to_csv(OUT / "an_mon_da_lam_sach.csv", index=False, encoding="utf-8-sig")

# ---------------------------------------------------------------- 3. Thống kê mô tả
tk = (sach.groupby(["tram", "kim_loai", "thoi_gian_thang"]).ton_that_g_m2
      .agg(n="count", tb="mean", do_lech="std").round(2).reset_index())
tk.to_csv(OUT / "thong_ke_mo_ta.csv", index=False, encoding="utf-8-sig")

# ---------------------------------------------------------------- 4. Mô hình C = A·t^n
def cap_iso(kl, a):
    for c, nguong in zip(CAP, ISO9223[kl]):
        if a <= nguong:
            return c
    return "CX"

mh = []
for (tram, kl), g in sach.groupby(["tram", "kim_loai"]):
    x, y = np.log(g.t_nam), np.log(g.ton_that_g_m2)
    n, lnA = np.polyfit(x, y, 1)
    r2 = 1 - ((y - (lnA + n * x)) ** 2).sum() / ((y - y.mean()) ** 2).sum()
    A = np.exp(lnA)
    mh.append(dict(tram=tram, kim_loai=kl, A_g_m2=round(A, 2), n=round(n, 3), R2=round(r2, 4),
                   so_diem=len(g), cap_ISO9223=cap_iso(kl, A),
                   du_bao_10_nam_g_m2=round(A * 10 ** n, 1),
                   du_bao_10_nam_um=round(A * 10 ** n / KHOI_LUONG_RIENG[kl], 1)))
mh = pd.DataFrame(mh)
mh.to_csv(OUT / "mo_hinh_A_n.csv", index=False, encoding="utf-8-sig")

# ---------------------------------------------------------------- 5. Liên hệ môi trường
kt = pd.read_csv(DATA / "khi_tuong_tram.csv")
kt_nam = kt[kt.nam == 2023].groupby("tram").agg(
    nhiet_do_C=("nhiet_do_tb_C", "mean"), do_am_pct=("do_am_tb_pct", "mean"),
    tow_gio_nam=("tow_gio", "sum"), clorua=("clorua_mg_m2_ngay", "mean"),
    so2=("so2_mg_m2_ngay", "mean")).round(1)
kt_nam["so_thang_thieu"] = kt[kt.nam == 2023].groupby("tram").apply(
    lambda g: int(g.isna().any(axis=1).sum()), include_groups=False)
thep = mh[mh.kim_loai == "Thep_CT3"].set_index("tram")[["A_g_m2", "cap_ISO9223"]]
lh = kt_nam.join(thep)
lh.to_csv(OUT / "moi_truong_va_ton_that_nam_dau.csv", encoding="utf-8-sig")

# ---------------------------------------------------------------- 6. Biểu đồ
MAU = {"TRAM_BIEN": "#1f77b4", "TRAM_DOTHI": "#ff7f0e", "TRAM_NOIDIA": "#2ca02c"}
fig, axes = plt.subplots(2, 2, figsize=(11, 8.5))
for ax, kl in zip(axes.flat, TEN_KL):
    for tram in TEN_TRAM:
        g = sach[(sach.kim_loai == kl) & (sach.tram == tram)]
        ax.scatter(g.t_nam, g.ton_that_g_m2, s=14, alpha=.6, color=MAU[tram])
        p = mh[(mh.kim_loai == kl) & (mh.tram == tram)].iloc[0]
        t = np.linspace(1 / 12, 3, 100)
        ax.plot(t, p.A_g_m2 * t ** p.n, color=MAU[tram],
                label=f"{TEN_TRAM[tram]}: A={p.A_g_m2:g}, n={p.n:.2f} ({p.cap_ISO9223})")
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_title(TEN_KL[kl]); ax.set_xlabel("Thời gian phơi mẫu (năm)"); ax.set_ylabel("Tổn thất (g/m²)")
    ax.grid(True, which="both", alpha=.25); ax.legend(fontsize=7.5)
fig.suptitle("Động học ăn mòn khí quyển C = A·tⁿ theo trạm thử nghiệm (dữ liệu giả lập)", fontsize=12)
fig.tight_layout(); fig.savefig(OUT / "bieu_do_dong_hoc_an_mon.png", dpi=150); plt.close(fig)

fig, ax = plt.subplots(figsize=(8, 4.5))
th = sach[sach.kim_loai == "Thep_CT3"]
vi_tri = {tram: i for i, tram in enumerate(TEN_TRAM)}
thang = sorted(th.thoi_gian_thang.unique()); w = .8 / len(thang)
for j, m in enumerate(thang):
    v = th[th.thoi_gian_thang == m].groupby("tram").ton_that_um.mean()
    ax.bar([vi_tri[s] + j * w for s in v.index], v.values, w, label=f"{m} tháng")
ax.set_xticks([i + .4 - w / 2 for i in range(3)], list(TEN_TRAM.values()))
ax.set_ylabel("Chiều dày bị ăn mòn (µm)"); ax.legend(ncol=4, fontsize=8)
ax.set_title("Thép CT3: chiều dày tổn thất theo trạm và thời gian (dữ liệu giả lập)")
ax.grid(axis="y", alpha=.25)
fig.tight_layout(); fig.savefig(OUT / "bieu_do_thep_theo_tram.png", dpi=150); plt.close(fig)

# ---------------------------------------------------------------- 7. Tóm tắt ra màn hình
print("=== BÁO CÁO CHẤT LƯỢNG DỮ LIỆU ===")
print(pd.DataFrame(log).groupby("loai_loi").size().to_string())
print(f"\nSố dòng gốc: {len(raw)} | dùng cho mô hình: {len(sach)}")
print("\n=== MÔ HÌNH C = A·t^n ===")
print(mh.to_string(index=False))
print("\n=== MÔI TRƯỜNG (2023) VÀ TỔN THẤT NĂM ĐẦU CỦA THÉP ===")
print(lh.to_string())
