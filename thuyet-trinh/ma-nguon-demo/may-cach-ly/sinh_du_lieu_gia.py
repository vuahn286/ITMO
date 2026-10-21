"""
Sinh dữ liệu GIẢ LẬP địa hình – khí hậu nhiệt đới để thử công cụ lộ trình UAV (Demo 3 – máy không Internet).

Nguyên tắc: AI chỉ được thấy CẤU TRÚC dữ liệu (tên cột, đơn vị) và dữ liệu giả này.
Dữ liệu thật của đề tài mật chỉ nạp vào công cụ trên máy không Internet.

Chạy:  python3 sinh_du_lieu_gia.py
Đầu ra: thuyet-trinh/du-lieu-demo/may-cach-ly/luoi_dia_hinh_khi_hau.csv, nhiem_vu_bay.json
"""
from pathlib import Path
import json
import numpy as np

TT = Path(__file__).resolve().parents[2]  # thư mục thuyet-trinh/
OUT = TT / "du-lieu-demo" / "may-cach-ly"
OUT.mkdir(parents=True, exist_ok=True)

N = 120          # lưới 120 × 120 ô
O_LUOI = 100.0   # mỗi ô 100 m → vùng 12 × 12 km
rng = np.random.default_rng(2026)
I, J = np.meshgrid(np.arange(N), np.arange(N), indexing="ij")

def doi(ci, cj, cao, rong):
    return cao * np.exp(-((I - ci) ** 2 + (J - cj) ** 2) / (2 * rong ** 2))

# Địa hình: dãy núi chéo giữa vùng, có một đèo thấp; vài đồi lẻ
day = 1150 * np.exp(-((I + J - 120) ** 2) / (2 * 9 ** 2))
deo = 1 - 0.75 * np.exp(-((I - J + 20) ** 2) / (2 * 7 ** 2))
h = 20 + day * deo + doi(30, 85, 450, 9) + doi(85, 25, 380, 8) + doi(95, 95, 300, 10)
h += 15 * rng.standard_normal((N, N))
h = np.maximum(h, 5)

# Khí hậu nhiệt đới (giả lập): nhiệt độ giảm theo độ cao 6,5 °C/km; độ ẩm cao
T = 33.0 - 6.5 * h / 1000 + rng.normal(0, 0.5, (N, N))
RH = np.clip(82 + 8 * h / 1150 + rng.normal(0, 2, (N, N)), 60, 100)
# Gió mùa Tây Nam ~4,5 m/s, mạnh lên trên sườn và đỉnh núi
v_nen = 4.5 * (1 + 0.8 * h / 1150)
goc = np.deg2rad(225)  # gió từ hướng Tây Nam thổi về Đông Bắc
u = -v_nen * np.sin(goc) + rng.normal(0, .4, (N, N))
v = -v_nen * np.cos(goc) + rng.normal(0, .4, (N, N))
# Mưa: một ổ mưa dông lớn và một vùng mưa nhẹ
mua = doi(60, 30, 22, 9) + doi(40, 100, 4, 14)

with open(OUT / "luoi_dia_hinh_khi_hau.csv", "w", encoding="utf-8") as f:
    f.write("i,j,do_cao_m,gio_u_ms,gio_v_ms,mua_mm_h,nhiet_do_C,do_am_pct\n")
    for a in range(N):
        for b in range(N):
            f.write(f"{a},{b},{h[a,b]:.1f},{u[a,b]:.2f},{v[a,b]:.2f},{mua[a,b]:.2f},{T[a,b]:.1f},{RH[a,b]:.0f}\n")

json.dump({"ten": "Nhiệm vụ thử – DỮ LIỆU GIẢ LẬP", "o_luoi_m": O_LUOI,
           "diem_xuat_phat": [10, 12], "diem_den": [108, 104], "do_cao_bay_tren_mat_dat_m": 80},
          open(OUT / "nhiem_vu_bay.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"Đã sinh {N*N} ô lưới → {OUT}")
