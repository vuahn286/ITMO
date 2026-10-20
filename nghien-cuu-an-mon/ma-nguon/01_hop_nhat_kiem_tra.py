"""
Bước 1 – Hợp nhất và kiểm tra chất lượng dữ liệu ăn mòn khí quyển của thép cacbon.

Nguồn: kho GitHub arashrockey/C-OLR (giấy phép MIT), commit 107ffa4, tệp datasets.xlsx
  - training_dataset (320): ISOCORRAG (Chico et al. 2017) + MICAT (Pintos et al. 2000)
  - testing_dataset  (67) : các công bố độc lập (Việt Nam – Lien et al.; Nga – Mikhailov et al.;
                            Tây Ban Nha, Colombia, quần đảo Canary …)
Mọi số liệu là số đo thực địa đã công bố; KHÔNG có số liệu giả lập ở bước này.
"""
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "du-lieu" / "goc" / "C-OLR_datasets.xlsx"
OUT = ROOT / "ket-qua"
OUT.mkdir(exist_ok=True)

RHO_THEP = 7.86  # g/cm³ – quy đổi µm → g/m² (1 µm ≙ 7,86 g/m²)
# Ngưỡng ISO 9223:2012 cho thép cacbon, tốc độ năm đầu (µm/năm): C1 ≤1,3; C2 ≤25; C3 ≤50; C4 ≤80; C5 ≤200; CX ≤700
NGUONG_UM = [(1.3, "C1"), (25, "C2"), (50, "C3"), (80, "C4"), (200, "C5"), (700, "CX")]
QUOC_GIA = {"Lien et al.": "Việt Nam", "mikhailov et al.": "Nga", "de la Fuente et al.": "Tây Ban Nha",
            "Morales et al.": "Tây Ban Nha (Canary)", "Castano et al.": "Colombia", "Santa et al.": "Colombia"}

def cap(um):
    for nguong, c in NGUONG_UM:
        if um <= nguong:
            return c
    return ">CX"

tr = pd.read_excel(SRC, sheet_name="training_dataset").assign(tap="huan_luyen")
te = pd.read_excel(SRC, sheet_name="testing_dataset").assign(tap="kiem_dinh_doc_lap")
df = pd.concat([tr, te], ignore_index=True)
df.columns = ["nguon", "tram", "loai_khi_quyen", "T_C", "TOW_h_nam", "Cl_mg_m2_ngay",
              "SO2_mg_m2_ngay", "WL", "cap_goc", "tai_lieu", "tap"]
df["tai_lieu"] = df.tai_lieu.str.strip()
df["tram"] = df.tram.astype(str).str.strip()
df["quoc_gia"] = df.tai_lieu.map(QUOC_GIA).fillna("Nhiều nước (" + df.nguon + ")")

# Dữ liệu bổ sung: mọi tệp *.csv trong du-lieu/bo-sung/ theo mẫu MAU_bo_sung.csv.template
# (r_corr_um_nam tính bằng µm/năm). Được xếp vào tập kiểm định độc lập để đánh giá mô hình.
COT_BS = ["nguon", "tram", "loai_khi_quyen", "T_C", "TOW_h_nam", "Cl_mg_m2_ngay",
          "SO2_mg_m2_ngay", "r_corr_um_nam", "tai_lieu", "quoc_gia"]
for f in sorted((ROOT / "du-lieu" / "bo-sung").glob("*.csv")):
    bs = pd.read_csv(f)
    thieu = set(COT_BS) - set(bs.columns)
    if thieu:
        raise ValueError(f"{f.name} thiếu cột {thieu}")
    bs = bs[COT_BS].rename(columns={"r_corr_um_nam": "WL"}).assign(tap="kiem_dinh_doc_lap")
    bs["cap_goc"] = bs.WL.apply(cap)
    df = pd.concat([df, bs], ignore_index=True)
    print(f"Đã nạp {len(bs)} dòng bổ sung từ {f.name}")

kiem_tra = []
def ghi(muc, n, mo_ta, ket_luan):
    kiem_tra.append(dict(muc=muc, so_dong=n, mo_ta=mo_ta, ket_luan=ket_luan))

# 1. Đơn vị WL: từ điển dữ liệu ghi g/m², kiểm tra bằng cách đối chiếu với cột cấp ăn mòn
khop_um = (df.WL.apply(cap) == df.cap_goc).mean()
khop_g = (df.WL.apply(lambda g: cap(g / RHO_THEP)) == df.cap_goc).mean()
ghi("Đơn vị WL", len(df),
    f"Từ điển dữ liệu ghi g/m². Nếu hiểu là µm/năm: {100*khop_um:.1f}% khớp cột CAT; "
    f"nếu là g/m²: {100*khop_g:.1f}% khớp.",
    "WL thực chất là µm/năm (lỗi trong từ điển dữ liệu của nguồn)" if khop_um > khop_g else "Giữ g/m²")
df = df.rename(columns={"WL": "r_corr_um_nam"})
df["r_corr_g_m2_nam"] = (df.r_corr_um_nam * RHO_THEP).round(1)
df["cap_tinh_lai"] = df.r_corr_um_nam.apply(cap)
lech = df[df.cap_tinh_lai != df.cap_goc]
ghi("Cấp ăn mòn không khớp", len(lech),
    "; ".join(f"{r.tram}: {r.r_corr_um_nam} µm → {r.cap_tinh_lai} (nguồn ghi {r.cap_goc})" for r in lech.itertuples())[:600],
    "Dùng cấp tính lại theo ngưỡng ISO; giữ cột gốc")

# 2. Giá trị thiếu / ngoài miền vật lý
ghi("Ô trống", int(df.isna().sum().sum()), "Tổng số ô trống trong các cột số", "—")
ghi("TOW cực thấp (< 300 h/năm)", int((df.TOW_h_nam < 300).sum()),
    ", ".join(df.loc[df.TOW_h_nam < 300, "tram"]), "Giữ – có thể là trạm khô hạn/lạnh; đánh dấu")
ghi("TOW vượt 8760 h/năm", int((df.TOW_h_nam > 8760).sum()), "", "Không có")
ghi("Cl⁻ = 0 hoặc SO₂ = 0", int(((df.Cl_mg_m2_ngay == 0) | (df.SO2_mg_m2_ngay == 0)).sum()),
    "Giá trị 0 (dưới ngưỡng phát hiện)", "Thay bằng 0,1 khi lấy log")

# 3. Trùng lặp
dup = df.duplicated(["tram", "T_C", "TOW_h_nam", "Cl_mg_m2_ngay", "SO2_mg_m2_ngay", "r_corr_um_nam"])
ghi("Dòng trùng hoàn toàn", int(dup.sum()), ", ".join(df.loc[dup, "tram"]), "Loại bản trùng")
df = df[~dup].copy()
cung_tram = df[df.tap == "kiem_dinh_doc_lap"].tram.value_counts()
ghi("Một trạm có nhiều quan sát", int((cung_tram > 1).sum()),
    ", ".join(cung_tram[cung_tram > 1].index), "Giữ – các năm phơi mẫu khác nhau (Cl⁻ khác nhau)")

df.to_csv(OUT / "du_lieu_hop_nhat.csv", index=False, encoding="utf-8-sig")
pd.DataFrame(kiem_tra).to_csv(OUT / "kiem_tra_chat_luong.csv", index=False, encoding="utf-8-sig")

print(pd.DataFrame(kiem_tra).to_string(index=False, max_colwidth=110))
print(f"\nSố quan sát sau hợp nhất: {len(df)}")
print(df.groupby(["tap", "quoc_gia"]).size().to_string())
print(df.groupby("quoc_gia").r_corr_um_nam.describe().round(1).to_string())
