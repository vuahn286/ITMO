"""Đường dẫn dùng chung cho mọi script của dự án (tính từ thư mục du-an-nghien-cuu/)."""
from pathlib import Path

DU_AN = Path(__file__).resolve().parents[1]

DL_THO = DU_AN / "03-du-lieu" / "1-du-lieu-tho"        # dữ liệu gốc – chỉ đọc
DL_XU_LY = DU_AN / "03-du-lieu" / "2-da-xu-ly"          # dữ liệu đã hợp nhất, báo cáo chất lượng
DL_BO_SUNG = DU_AN / "03-du-lieu" / "3-bo-sung"         # dữ liệu mới thả vào
C_OLR = DL_THO / "c-olr" / "C-OLR_datasets.xlsx"

KQ = DU_AN / "05-ket-qua"
BANG = KQ / "bang"
HINH = KQ / "hinh"
MO_HINH = KQ / "mo-hinh"
MO_HINH_3D = KQ / "mo-hinh-3d"

for _p in (DL_XU_LY, DL_BO_SUNG, BANG, HINH, MO_HINH, MO_HINH_3D):
    _p.mkdir(parents=True, exist_ok=True)
