"""Vẽ sơ đồ Gantt từ ke_hoach_cong_viec.csv (minh họa Slide 14)."""
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

TT = Path(__file__).resolve().parents[2]  # thư mục thuyet-trinh/
kh = pd.read_csv(TT / "du-lieu-demo" / "gia-lap" / "ke_hoach_cong_viec.csv")
kh["bd"] = pd.to_datetime(kh.bat_dau)
kh["kt"] = [b + pd.DateOffset(months=int(m)) for b, m in zip(kh.bd, kh.so_thang)]

fig, ax = plt.subplots(figsize=(11, 4.2))
for i, r in kh.iloc[::-1].reset_index(drop=True).iterrows():
    ax.barh(i, (r.kt - r.bd).days, left=r.bd, color="#4c72b0")
    ax.text(r.kt, i, f"  {r.kinh_phi_trieu_dong} tr.đ", va="center", fontsize=8)
ax.set_yticks(range(len(kh)), [f"{a}. {b}" for a, b in zip(kh.ma_nd[::-1], kh.noi_dung[::-1])], fontsize=8)
ax.set_title(f"Tiến độ nhiệm vụ (minh họa) – tổng kinh phí {kh.kinh_phi_trieu_dong.sum():,} triệu đồng".replace(",", "."))
ax.grid(axis="x", alpha=.3)
fig.tight_layout(); fig.savefig(TT / "ket-qua-demo" / "gia-lap" / "so_do_gantt.png", dpi=150)
print(kh[["ma_nd", "bd", "kt", "kinh_phi_trieu_dong"]].to_string(index=False))
