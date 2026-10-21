"""Sinh dữ liệu GIẢ LẬP cho demo (không phải số liệu đo thật).

Tạo lại 3 tệp trong thuyet-trinh/du-lieu-demo/gia-lap/ – kết quả giống hệt nhau mỗi lần chạy (cố định hạt giống ngẫu nhiên).
"""
from pathlib import Path
import numpy as np, pandas as pd
from datetime import date, timedelta

rng = np.random.default_rng(2026)
OUT = str(Path(__file__).resolve().parents[2] / "du-lieu-demo" / "gia-lap") + "/"

# ---------- 1. Khí tượng – môi trường theo tháng ----------
tram_cfg = {
    "TRAM_BIEN":   dict(T=27.0, RH=82, mua=140, tow=5600, cl=180, so2=8),
    "TRAM_DOTHI":  dict(T=24.5, RH=79, mua=135, tow=4300, cl=12,  so2=35),
    "TRAM_NOIDIA": dict(T=23.5, RH=84, mua=150, tow=4900, cl=4,   so2=6),
}
rows = []
for tram, c in tram_cfg.items():
    for i in range(36):
        y, m = 2023 + i // 12, i % 12 + 1
        s = np.sin(2 * np.pi * (m - 4) / 12)
        rows.append(dict(
            tram=tram, nam=y, thang=m,
            nhiet_do_tb_C=round(c["T"] + 4 * s + rng.normal(0, .4), 1),
            do_am_tb_pct=round(min(98, c["RH"] + 5 * s + rng.normal(0, 1.5)), 1),
            luong_mua_mm=round(max(0, c["mua"] * (1 + 1.2 * s) + rng.normal(0, 25)), 1),
            tow_gio=round(max(80, c["tow"] / 12 * (1 + .3 * s) + rng.normal(0, 25))),
            clorua_mg_m2_ngay=round(max(.5, c["cl"] * (1 + .5 * np.cos(2 * np.pi * (m - 11) / 12)) * rng.lognormal(0, .12)), 1),
            so2_mg_m2_ngay=round(max(.5, c["so2"] * rng.lognormal(0, .15)), 1),
        ))
kt = pd.DataFrame(rows)
for idx in rng.choice(len(kt), 4, replace=False):          # thiếu số liệu
    kt.loc[idx, rng.choice(["do_am_tb_pct", "clorua_mg_m2_ngay"])] = np.nan
kt.to_csv(OUT + "khi_tuong_tram.csv", index=False)

# ---------- 2. Ăn mòn: tổn thất khối lượng mẫu ----------
# C = A * t^n  (g/m², t: năm)
A = {"TRAM_BIEN":   {"Thep_CT3": 560, "Kem": 22,  "Dong": 18,  "Nhom": 4.2},
     "TRAM_DOTHI":  {"Thep_CT3": 310, "Kem": 11,  "Dong": 9,   "Nhom": 1.4},
     "TRAM_NOIDIA": {"Thep_CT3": 160, "Kem": 4.5, "Dong": 4,   "Nhom": 0.45}}
n = {"Thep_CT3": .72, "Kem": .85, "Dong": .70, "Nhom": .60}
m0 = {"Thep_CT3": 117.8, "Kem": 107.1, "Dong": 134.4, "Nhom": 40.5}
DT = 300.0  # cm², hai mặt mẫu 100x150 mm
thang_list = [1, 3, 6, 12, 18, 24, 36]
start = date(2023, 1, 15)
rows = []
for tram in A:
    for kl in n:
        for th in thang_list:
            for r in range(1, 4):
                t = th / 12
                C = A[tram][kl] * t ** n[kl] * rng.lognormal(0, .06)
                truoc = m0[kl] + rng.normal(0, .3)
                sau = truoc - C * DT / 1e4
                rows.append(dict(
                    ma_mau=f"{tram[5:7]}-{kl[:2].upper()}-{th:02d}-{r}",
                    tram=tram, kim_loai=kl,
                    ngay_dat_mau=start.isoformat(),
                    ngay_thu_mau=(start + timedelta(days=round(th * 30.44))).isoformat(),
                    thoi_gian_thang=th, lan_lap=r,
                    khoi_luong_truoc_g=f"{truoc:.4f}", khoi_luong_sau_g=f"{sau:.4f}",
                    dien_tich_cm2=DT, ghi_chu=""))
df = pd.DataFrame(rows)

# ---- Cố ý cài lỗi để AI phát hiện ----
def at(code): return df.index[df.ma_mau == code][0]
df.loc[at("BI-TH-12-2"), "khoi_luong_sau_g"] = ""                  # thiếu
df.loc[at("DO-KE-24-3"), "khoi_luong_sau_g"] = ""                  # thiếu
df.loc[at("NO-DO-06-1"), "khoi_luong_sau_g"] = ""                  # thiếu
i = at("BI-KE-06-2"); df.loc[i, "khoi_luong_sau_g"] = df.loc[i, "khoi_luong_sau_g"].replace(".", ",")  # dấu phẩy
i = at("DO-TH-03-1"); df.loc[i, "khoi_luong_sau_g"] += " g"         # dính đơn vị
i = at("NO-TH-18-3")                                                 # khối lượng sau > trước
df.loc[i, "khoi_luong_sau_g"] = f"{float(df.loc[i, 'khoi_luong_truoc_g']) + 0.412:.4f}"
i = at("BI-TH-24-1")                                                 # gõ nhầm (lệch 1 chữ số)
df.loc[i, "khoi_luong_sau_g"] = f"{float(df.loc[i, 'khoi_luong_sau_g']) - 20.0:.4f}"
i = at("DO-NH-12-2"); df.loc[i, "ngay_thu_mau"] = "14/01/2024"      # sai định dạng ngày
i = at("NO-KE-36-1"); df.loc[i, "ngay_thu_mau"] = "2026/01/13"
i = at("BI-DO-03-3"); df.loc[i, "tram"] = "Tram bien"               # tên trạm không thống nhất
i = at("NO-NH-01-2"); df.loc[i, "tram"] = "tram_noidia "
df.loc[at("BI-TH-36-2"), "ghi_chu"] = "mẫu bị rơi khi thu, mất một phần gỉ"
df.loc[at("DO-DO-18-1"), "ghi_chu"] = "tẩy gỉ lần 2"
df = pd.concat([df, df.loc[[at("DO-TH-06-2")]]]).reset_index(drop=True)  # trùng dòng
df = df.sample(frac=1, random_state=7).reset_index(drop=True)            # xáo thứ tự
df.to_csv(OUT + "an_mon_tho.csv", index=False)

# ---------- 3. Kế hoạch công việc (WBS) ----------
wbs = [
 ("ND1", "Tổng quan tài liệu, xây dựng phương pháp", "2027-01", 3, "Ma trận bằng chứng; đề cương chi tiết", "Chủ nhiệm", 60),
 ("ND2", "Chuẩn bị mẫu, lắp đặt giá phơi mẫu tại 3 trạm", "2027-02", 3, "Biên bản lắp đặt; 252 mẫu", "Phòng Độ bền", 220),
 ("ND3", "Quan trắc khí tượng – môi trường (Cl-, SO2, TOW)", "2027-03", 36, "Bộ dữ liệu khí tượng 36 tháng", "Phòng Môi trường", 310),
 ("ND4", "Thu mẫu, tẩy gỉ, cân khối lượng theo 7 mốc", "2027-04", 36, "Bộ dữ liệu tổn thất khối lượng", "Phòng Độ bền", 280),
 ("ND5", "Phân tích dữ liệu, xây dựng mô hình C = A·t^n", "2028-04", 24, "Mô hình dự báo; bản đồ cấp ăn mòn", "Nhóm dữ liệu", 150),
 ("ND6", "Phân tích bề mặt, sản phẩm ăn mòn (SEM, XRD)", "2028-01", 18, "Báo cáo chuyên đề", "Phòng Hóa – Vật liệu", 240),
 ("ND7", "Công bố, hội thảo, báo cáo tổng kết", "2029-06", 10, "02 bài báo; Mẫu 21, 22", "Chủ nhiệm", 90),
]
pd.DataFrame(wbs, columns=["ma_nd", "noi_dung", "bat_dau", "so_thang", "san_pham",
                           "don_vi_thuc_hien", "kinh_phi_trieu_dong"]).to_csv(OUT + "ke_hoach_cong_viec.csv", index=False)
print(len(df), len(kt))
