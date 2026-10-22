"""
Tạo bộ dữ liệu THẬT nhiều nguồn cho demo Slide 8 từ bộ dữ liệu C-OLR (đã công bố, giấy phép MIT).

Đầu ra: thuyet-trinh/du-lieu-demo/nhieu-nguon/
  nguon1_ISOCORRAG_MICAT_quoc_te.xlsx  – 320 trạm, giữ NGUYÊN tiêu đề gốc (kể cả cột WL không ghi đơn vị)
  nguon2_tram_Viet_Nam.csv             – 12 trạm Việt Nam, tiêu đề tiếng Việt
  nguon3_tram_Nga.csv                  – 18 trạm Nga, tên cột tiếng Anh khác cấu trúc
  ket_qua_mong_doi_bang_tong_hop.csv   – đáp án để đối chiếu khi demo
(nguon4_nguong_ISO_9223.md viết tay, không sinh từ script này.)
"""
from pathlib import Path
import pandas as pd

REPO = Path(__file__).resolve().parents[3]  # gốc repo
SRC = REPO / "du-an-nghien-cuu" / "03-du-lieu" / "1-du-lieu-tho" / "c-olr" / "C-OLR_datasets.xlsx"
OUT = REPO / "thuyet-trinh" / "du-lieu-demo" / "nhieu-nguon"
OUT.mkdir(parents=True, exist_ok=True)

tr = pd.read_excel(SRC, sheet_name="training_dataset")
te = pd.read_excel(SRC, sheet_name="testing_dataset")

# Nguồn 1: quốc tế – giữ nguyên định dạng gốc để AI phát hiện nhãn đơn vị
tr.to_excel(OUT / "nguon1_ISOCORRAG_MICAT_quoc_te.xlsx", index=False)

# Nguồn 2: Việt Nam
TEN = {"Viet tri": "Việt Trì", "Son tay": "Sơn Tây", "Do son": "Đồ Sơn", "Hai duong": "Hải Dương",
       "Hanoi": "Hà Nội", "Thanh hoa": "Thanh Hóa", "Dong hoi": "Đồng Hới", "Hue": "Huế",
       "Danang": "Đà Nẵng", "Nhatrang": "Nha Trang", "Ho Chi Minh City": "TP. Hồ Chí Minh", "Vung tau": "Vũng Tàu"}
VUNG = {"Việt Trì": "Bắc Bộ", "Sơn Tây": "Bắc Bộ", "Đồ Sơn": "Bắc Bộ", "Hải Dương": "Bắc Bộ", "Hà Nội": "Bắc Bộ",
        "Thanh Hóa": "Bắc Trung Bộ", "Đồng Hới": "Bắc Trung Bộ", "Huế": "Bắc Trung Bộ",
        "Đà Nẵng": "Nam Trung Bộ", "Nha Trang": "Nam Trung Bộ", "TP. Hồ Chí Minh": "Nam Bộ", "Vũng Tàu": "Nam Bộ"}
vn = te[te["Ref."].str.strip() == "Lien et al."]
vn2 = pd.DataFrame({
    "Trạm": vn.Site.map(TEN), "Vùng": vn.Site.map(TEN).map(VUNG),
    "Nhiệt độ TB (°C)": vn.Temperature, "TOW (giờ/năm)": vn.TOW,
    "Clorua (mg/m²/ngày)": vn.Cl, "SO2 (mg/m²/ngày)": vn.SO2,
    "Tốc độ ăn mòn thép năm đầu (µm/năm)": vn.WL,
    "Nguồn": "Le Thi Hong Lien và cs. (2007), Sci. Technol. Adv. Mater. 8:552–558 – qua bộ dữ liệu C-OLR"})
vn2.to_csv(OUT / "nguon2_tram_Viet_Nam.csv", index=False, encoding="utf-8-sig")

# Nguồn 3: Nga
ru = te[te["Ref."].str.strip() == "mikhailov et al."][["Site", "Temperature", "TOW", "Cl", "SO2", "WL"]].rename(columns={
    "Site": "site", "Temperature": "T_mean_C", "TOW": "time_of_wetness_h_per_year", "Cl": "chloride_mg_m2_day",
    "SO2": "SO2_mg_m2_day", "WL": "first_year_corrosion_um"})
ru.to_csv(OUT / "nguon3_tram_Nga.csv", index=False)

# Đáp án
NGUONG = [(1.3, "C1"), (25, "C2"), (50, "C3"), (80, "C4"), (200, "C5"), (700, "CX"), (1e9, ">CX")]
cap = lambda u: next(c for n, c in NGUONG if u <= n)
rows = []
for ten, s in [("Quốc tế (ISOCORRAG + MICAT)", tr.WL), ("Việt Nam", vn2.iloc[:, 6]), ("Nga", ru.first_year_corrosion_um)]:
    c = s.apply(cap).value_counts()
    rows.append({"Nhóm": ten, "Số trạm": len(s), "TB (µm/năm)": round(s.mean(), 1), "Trung vị": round(s.median(), 1),
                 "Nhỏ nhất": s.min(), "Lớn nhất": s.max(), **{k: int(c.get(k, 0)) for k in ["C1", "C2", "C3", "C4", "C5", "CX"]}})
kq = pd.DataFrame(rows)
kq.to_csv(OUT / "ket_qua_mong_doi_bang_tong_hop.csv", index=False, encoding="utf-8-sig")
print(kq.to_string(index=False))
