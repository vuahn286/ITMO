"""
Bước 3 – Hiệu chỉnh địa phương (Việt Nam, Nga) và kiểm định bỏ-một-trạm (LOO).

Giả thuyết: mô hình học từ ISOCORRAG + MICAT mang sai lệch hệ thống theo vùng khí hậu.
Cách hiệu chỉnh đơn giản nhất: nhân với hệ số k = trung bình hình học (đo / dự đoán) của các
trạm KHÁC trong cùng vùng → mỗi trạm được dự đoán mà không dùng số đo của chính nó.
"""
from pathlib import Path
import numpy as np
import pandas as pd
from duong_dan import *  # noqa: F401,F403 – đường dẫn dự án

te = pd.read_csv(BANG / "du_doan_kiem_dinh.csv")
NGUONG = [(1.3, "C1"), (25, "C2"), (50, "C3"), (80, "C4"), (200, "C5"), (700, "CX")]
cap = lambda um: next((c for n, c in NGUONG if um <= n), ">CX")

rows, chi_tiet = [], []
for qg in ["Việt Nam", "Nga"]:
    g = te[te.quoc_gia == qg].reset_index(drop=True)
    for col in ["du_doan_M1_DRF", "du_doan_M2_GBM", "du_doan_TB"]:
        lr = np.log(g.r_corr_um_nam / g[col])
        k_loo = np.exp([(lr.sum() - lr[i]) / (len(g) - 1) for i in range(len(g))])
        hc = g[col] * k_loo
        for ten, p in [("chưa hiệu chỉnh", g[col]), ("hiệu chỉnh LOO", hc)]:
            rows.append(dict(vung=qg, mo_hinh=col.replace("du_doan_", ""), trang_thai=ten,
                             sai_lech_TB_pct=round(float((np.exp(np.mean(np.log(p / g.r_corr_um_nam))) - 1) * 100), 1),
                             sai_so_tuong_doi_trung_vi_pct=round(float(np.median(np.abs(p / g.r_corr_um_nam - 1)) * 100), 1),
                             dung_cap_pct=round(float(np.mean([cap(a) == cap(b) for a, b in zip(g.r_corr_um_nam, p)]) * 100), 1)))
        if col == "du_doan_TB":
            k_all = float(np.exp(lr.mean()))
            chi_tiet.append(g.assign(k_LOO=k_loo.round(3), du_doan_hieu_chinh=hc.round(1),
                                     cap_hieu_chinh=hc.apply(cap)))
            print(f"{qg}: hệ số hiệu chỉnh vùng k = {k_all:.3f} "
                  f"(mô hình toàn cầu {'thấp' if k_all > 1 else 'cao'} hơn thực đo {abs(1 - 1 / k_all) * 100:.0f}%)")

kq = pd.DataFrame(rows)
kq.to_csv(BANG / "hieu_chinh_dia_phuong.csv", index=False, encoding="utf-8-sig")
pd.concat(chi_tiet).to_csv(BANG / "du_doan_hieu_chinh_VN_RU.csv", index=False, encoding="utf-8-sig")
print(kq.to_string(index=False))
