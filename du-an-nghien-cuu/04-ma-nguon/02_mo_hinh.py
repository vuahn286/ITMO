"""
Bước 2 – Xây dựng và kiểm định mô hình tốc độ ăn mòn năm đầu của thép cacbon.

M1  Hàm liều – đáp ứng (DRF) dạng ISO 9223, hiệu chỉnh lại trên dữ liệu
    (dữ liệu có TOW thay cho RH nên không áp dụng nguyên văn hệ số ISO):
      r = a·SO2^b·exp(c·τ + f(T)) + d·Cl^e·exp(g·τ + h·T),  τ = TOW/1000,
      f(T) = k1·(T−10) nếu T ≤ 10 °C, ngược lại k2·(T−10)
M2  Gradient boosting có ràng buộc đơn điệu (r tăng theo Cl⁻, SO₂, TOW) –
    giữ quan hệ vật lý, tương tự tinh thần của C-OLR.

Huấn luyện: 320 quan sát ISOCORRAG + MICAT. Kiểm định độc lập: 67 quan sát (gồm 12 trạm Việt Nam, 18 trạm Nga).
"""
from pathlib import Path
import json
import numpy as np
import pandas as pd
from duong_dan import *  # noqa: F401,F403 – đường dẫn dự án
from scipy.optimize import least_squares
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.model_selection import KFold
from sklearn.inspection import permutation_importance
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

df = pd.read_csv(DL_XU_LY / "du_lieu_hop_nhat.csv")
NGUONG = [(1.3, "C1"), (25, "C2"), (50, "C3"), (80, "C4"), (200, "C5"), (700, "CX")]
cap = lambda um: next((c for n, c in NGUONG if um <= n), ">CX")
FEAT = ["T_C", "TOW_h_nam", "Cl_mg_m2_ngay", "SO2_mg_m2_ngay"]

# ------------------------------------------------------------------ M1: DRF
def drf(p, T, tow, cl, so2):
    a, b, c, k1, k2, d, e, g, h = p
    tau = tow / 1000
    fT = np.where(T <= 10, k1 * (T - 10), k2 * (T - 10))
    return a * np.maximum(so2, .1) ** b * np.exp(c * tau + fT) + d * np.maximum(cl, .1) ** e * np.exp(g * tau + h * T)

def fit_drf(d):
    X = [d[f].values for f in FEAT]; y = np.log(d.r_corr_um_nam.values)
    p0 = [1.0, .5, .2, .1, -.03, .5, .6, .2, .02]
    lb = [1e-4, 0, -2, -1, -1, 1e-4, 0, -2, -1]; ub = [1e3, 2, 2, 1, 1, 1e3, 2, 2, 1]
    r = least_squares(lambda p: np.log(drf(p, *X)) - y, p0, bounds=(lb, ub), loss="soft_l1", f_scale=.3)
    return r.x

def pred_drf(p, d):
    return drf(p, *[d[f].values for f in FEAT])

# ------------------------------------------------------------------ M2: GBM đơn điệu
def Xg(d):
    return np.column_stack([d.T_C, d.TOW_h_nam, np.log(np.maximum(d.Cl_mg_m2_ngay, .1)),
                            np.log(np.maximum(d.SO2_mg_m2_ngay, .1))])

def fit_gbm(d):
    m = HistGradientBoostingRegressor(max_iter=400, learning_rate=.04, max_leaf_nodes=12,
                                      min_samples_leaf=8, l2_regularization=1.0,
                                      monotonic_cst=[0, 1, 1, 1], random_state=0)
    return m.fit(Xg(d), np.log(d.r_corr_um_nam))

def pred_gbm(m, d):
    return np.exp(m.predict(Xg(d)))

# ------------------------------------------------------------------ chỉ số
def chi_so(y, p, ten):
    ly, lp = np.log(y), np.log(p)
    return dict(tap=ten, n=len(y),
                R2_log=round(1 - ((ly - lp) ** 2).sum() / ((ly - ly.mean()) ** 2).sum(), 3),
                RMSE_log=round(float(np.sqrt(((ly - lp) ** 2).mean())), 3),
                sai_so_tuong_doi_trung_vi_pct=round(float(np.median(np.abs(p / y - 1)) * 100), 1),
                dung_cap_ISO_pct=round(float(np.mean([cap(a) == cap(b) for a, b in zip(y, p)]) * 100), 1),
                lech_toi_da_1_cap_pct=round(float(np.mean([abs(int(cap(a)[1]) - int(cap(b)[1])) <= 1
                                                           for a, b in zip(y, p) if cap(a)[1:].isdigit() and cap(b)[1:].isdigit()]) * 100), 1))

tr = df[df.tap == "huan_luyen"].reset_index(drop=True)
te = df[df.tap == "kiem_dinh_doc_lap"].reset_index(drop=True)

# Kiểm định chéo 10 lần trên tập huấn luyện
cv = {"M1_DRF": np.zeros(len(tr)), "M2_GBM": np.zeros(len(tr))}
for i_tr, i_va in KFold(10, shuffle=True, random_state=1).split(tr):
    a, b = tr.iloc[i_tr], tr.iloc[i_va]
    cv["M1_DRF"][i_va] = pred_drf(fit_drf(a), b)
    cv["M2_GBM"][i_va] = pred_gbm(fit_gbm(a), b)

p_drf = fit_drf(tr); gbm = fit_gbm(tr)
te["du_doan_M1_DRF"] = pred_drf(p_drf, te).round(1)
te["du_doan_M2_GBM"] = pred_gbm(gbm, te).round(1)
te["du_doan_TB"] = np.sqrt(te.du_doan_M1_DRF * te.du_doan_M2_GBM).round(1)  # trung bình hình học

rows = []
for ten, p in cv.items():
    rows.append({"mo_hinh": ten, **chi_so(tr.r_corr_um_nam.values, p, "CV 10-lần (huấn luyện)")})
for ten, col in [("M1_DRF", "du_doan_M1_DRF"), ("M2_GBM", "du_doan_M2_GBM"), ("TB(M1,M2)", "du_doan_TB")]:
    rows.append({"mo_hinh": ten, **chi_so(te.r_corr_um_nam.values, te[col].values, "Kiểm định độc lập – tất cả")})
    for qg in ["Việt Nam", "Nga"]:
        s = te[te.quoc_gia == qg]
        rows.append({"mo_hinh": ten, **chi_so(s.r_corr_um_nam.values, s[col].values, f"Kiểm định độc lập – {qg}")})
kq = pd.DataFrame(rows)
kq.to_csv(BANG / "danh_gia_mo_hinh.csv", index=False, encoding="utf-8-sig")

te["cap_do"] = te.r_corr_um_nam.apply(cap); te["cap_du_doan"] = te.du_doan_TB.apply(cap)
te[["quoc_gia", "tram", "T_C", "TOW_h_nam", "Cl_mg_m2_ngay", "SO2_mg_m2_ngay", "r_corr_um_nam",
    "du_doan_M1_DRF", "du_doan_M2_GBM", "du_doan_TB", "cap_do", "cap_du_doan"]].to_csv(
    BANG / "du_doan_kiem_dinh.csv", index=False, encoding="utf-8-sig")

# Mức độ quan trọng của biến (hoán vị, trên tập kiểm định)
pi = permutation_importance(gbm, Xg(te), np.log(te.r_corr_um_nam), n_repeats=50, random_state=0)
qt = pd.DataFrame({"bien": ["Nhiệt độ", "TOW", "log Cl⁻", "log SO₂"],
                   "giam_R2_khi_xao_tron": pi.importances_mean.round(3)}).sort_values("giam_R2_khi_xao_tron", ascending=False)
qt.to_csv(BANG / "muc_do_quan_trong_bien.csv", index=False, encoding="utf-8-sig")

json.dump(dict(zip(["a", "b", "c", "k1", "k2", "d", "e", "g", "h"], np.round(p_drf, 5).tolist())),
          open(MO_HINH / "he_so_DRF.json", "w"), indent=2)
import pickle; pickle.dump({"drf": p_drf, "gbm": gbm}, open(MO_HINH / "mo_hinh.pkl", "wb"))

# ------------------------------------------------------------------ biểu đồ đo – dự đoán
fig, ax = plt.subplots(figsize=(6.5, 6))
mau = {"Việt Nam": "#d62728", "Nga": "#1f77b4", "Colombia": "#2ca02c", "Tây Ban Nha": "#9467bd", "Tây Ban Nha (Canary)": "#ff7f0e"}
ax.scatter(tr.r_corr_um_nam, cv["M2_GBM"], s=10, c="#bbbbbb", label="Huấn luyện (CV 10 lần)")
for qg, g in te.groupby("quoc_gia"):
    ax.scatter(g.r_corr_um_nam, g.du_doan_TB, s=34, c=mau[qg],
               edgecolor="k", lw=.4, label=f"Kiểm định – {qg}", marker="o" if qg in mau else "^")
lim = [1, 400]; ax.plot(lim, lim, "k-", lw=.8)
for f in (0.5, 2): ax.plot(lim, [l * f for l in lim], "k:", lw=.6)
for n, c in NGUONG[:5]:
    ax.axvline(n, color="#999", lw=.4); ax.text(n, 1.1, c, fontsize=7, ha="right")
ax.set_xscale("log"); ax.set_yscale("log"); ax.set_xlim(lim); ax.set_ylim(lim)
ax.set_xlabel("Đo thực địa – tốc độ năm đầu (µm/năm)"); ax.set_ylabel("Mô hình dự đoán (µm/năm)")
ax.set_title("Thép cacbon: đo – dự đoán (đường chấm: sai lệch ×2)", fontsize=10)
ax.legend(fontsize=7, loc="upper left"); fig.tight_layout()
fig.savefig(HINH / "do_vs_du_doan.png", dpi=150)

print(kq.to_string(index=False))
print("\nHệ số DRF:", dict(zip(["a", "b", "c", "k1", "k2", "d", "e", "g", "h"], np.round(p_drf, 4))))
print("\n", qt.to_string(index=False))
print("\n", te[te.quoc_gia.isin(["Việt Nam", "Nga"])][["quoc_gia", "tram", "Cl_mg_m2_ngay", "r_corr_um_nam",
       "du_doan_M1_DRF", "du_doan_M2_GBM", "du_doan_TB", "cap_do", "cap_du_doan"]].to_string(index=False))
