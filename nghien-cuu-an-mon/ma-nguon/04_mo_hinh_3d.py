"""
Bước 4 – Mô hình 3D mô tả quá trình ăn mòn của thép cacbon.

3D-1  Mặt đáp ứng: tốc độ ăn mòn năm đầu r(Cl⁻, TOW) cho khí hậu Việt Nam và Viễn Đông Nga
      (mô hình đã hiệu chỉnh vùng) + các điểm đo thật.
3D-2  Diễn tiến theo thời gian: chiều dày bị ăn mòn D(t, Cl⁻) theo ISO 9224:2012
      D = r·t^b (t ≤ 20 năm), sau 20 năm tuyến tính với độ dốc r·b·20^(b−1); b = 0,523 (B1, thép cacbon).
3D-3  Bề mặt tấm thép bị ăn mòn theo thời gian tại Nha Trang và Hà Nội (minh họa hiện tượng học):
      chiều dày trung bình = D(t) từ 3D-2 (định lượng, có căn cứ); độ nhám/hố cục bộ là trường ngẫu nhiên
      có tương quan không gian với tham số GIẢ ĐỊNH (chưa hiệu chỉnh bằng đo profilometry).
"""
from pathlib import Path
import pickle
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "ket-qua"
M = pickle.load(open(OUT / "mo_hinh.pkl", "rb"))
df = pd.read_csv(OUT / "du_lieu_hop_nhat.csv")
hc = pd.read_csv(OUT / "du_doan_hieu_chinh_VN_RU.csv")
# Mặt 3D dùng M1 (DRF) – trơn, có ý nghĩa vật lý; hệ số vùng tính riêng cho DRF
K = {q: float(np.exp(np.log(g.r_corr_um_nam / g.du_doan_M1_DRF).mean())) for q, g in hc.groupby("quoc_gia")}

B_THEP = 0.523  # ISO 9224:2012, B1, thép cacbon

def drf(p, T, tow, cl, so2):
    a, b, c, k1, k2, d, e, g, h = p
    tau = tow / 1000; fT = np.where(T <= 10, k1 * (T - 10), k2 * (T - 10))
    return a * np.maximum(so2, .1) ** b * np.exp(c * tau + fT) + d * np.maximum(cl, .1) ** e * np.exp(g * tau + h * T)

def r_mo_hinh(T, tow, cl, so2, vung):
    T, tow, cl, so2 = np.broadcast_arrays(*[np.asarray(v, float) for v in (T, tow, cl, so2)])
    r = drf(M["drf"], T.ravel(), tow.ravel(), cl.ravel(), so2.ravel())
    return (r * K[vung]).reshape(T.shape)

def D_iso9224(r, t, b=B_THEP):
    t = np.asarray(t, float)
    return np.where(t <= 20, r * t ** b, r * 20 ** b + r * b * 20 ** (b - 1) * (t - 20))

KHI_HAU = {"Việt Nam": dict(T=25.0, SO2=5.0), "Nga": dict(T=0.0, SO2=3.0)}  # gần trung vị các trạm kiểm định
cl_ax = np.logspace(np.log10(0.5), np.log10(200), 60)
tow_ax = np.linspace(1500, 7500, 50)
CL, TOW = np.meshgrid(cl_ax, tow_ax)

# ================================================================ 3D-1 mặt đáp ứng (HTML tương tác)
fig = make_subplots(rows=1, cols=2, specs=[[{"type": "surface"}] * 2],
                    subplot_titles=["Việt Nam (T = 25 °C, SO₂ = 5)", "Viễn Đông Nga (T = 0 °C, SO₂ = 3)"])
for j, (vung, kh) in enumerate(KHI_HAU.items(), start=1):
    R = r_mo_hinh(kh["T"], TOW, CL, kh["SO2"], vung)
    fig.add_trace(go.Surface(x=np.log10(CL), y=TOW, z=R, colorscale="YlOrRd", cmin=0, cmax=200,
                             showscale=(j == 2), colorbar=dict(title="µm/năm"),
                             hovertemplate="Cl⁻=%{customdata:.1f}<br>TOW=%{y:.0f} h<br>r=%{z:.1f} µm/năm<extra></extra>",
                             customdata=CL, opacity=.9), 1, j)
    d = df[df.quoc_gia == vung]
    fig.add_trace(go.Scatter3d(x=np.log10(np.maximum(d.Cl_mg_m2_ngay, .5)), y=d.TOW_h_nam, z=d.r_corr_um_nam,
                               mode="markers+text", text=d.tram, textfont=dict(size=9),
                               marker=dict(size=5, color="#1f3b73", line=dict(width=1, color="white")),
                               name=f"Đo thực địa – {vung}"), 1, j)
ax3 = dict(xaxis=dict(title="log₁₀ Cl⁻ (mg/m²·ngày)"), yaxis=dict(title="TOW (h/năm)"),
           zaxis=dict(title="r (µm/năm)", range=[0, 260]))
fig.update_layout(title="3D-1. Tốc độ ăn mòn năm đầu của thép cacbon theo clorua và thời gian ẩm ướt "
                        "(DRF hiệu chỉnh vùng; điểm = số đo thật)",
                  scene=ax3, scene2=ax3, height=650, margin=dict(l=0, r=0, t=60, b=0))
fig.write_html(OUT / "3D_1_mat_dap_ung.html", include_plotlyjs="cdn")

# ================================================================ 3D-2 diễn tiến theo thời gian (Việt Nam)
t_ax = np.linspace(0, 50, 51)
cl2 = np.logspace(np.log10(1), np.log10(200), 40)
Tt, CL2 = np.meshgrid(t_ax, cl2)
r_vn = r_mo_hinh(25, 5500, CL2, 5, "Việt Nam")
D = D_iso9224(r_vn, Tt)
fig2 = go.Figure(go.Surface(x=Tt, y=np.log10(CL2), z=D, colorscale="Inferno", colorbar=dict(title="µm"),
                            customdata=CL2, hovertemplate="t=%{x:.0f} năm<br>Cl⁻=%{customdata:.1f}<br>D=%{z:.0f} µm<extra></extra>"))
for ten, cl in [("Hà Nội (Cl⁻ 2,2)", 2.24), ("Đồ Sơn (17,5)", 17.51), ("Ven biển mạnh (100)", 100)]:
    rr = float(r_mo_hinh(25, 5500, cl, 5, "Việt Nam"))
    fig2.add_trace(go.Scatter3d(x=t_ax, y=np.full_like(t_ax, np.log10(cl)), z=D_iso9224(rr, t_ax) + 2,
                                mode="lines", line=dict(width=6), name=ten))
fig2.update_layout(title="3D-2. Chiều dày thép cacbon bị ăn mòn theo thời gian và clorua – khí hậu Việt Nam "
                         "(T 25 °C, TOW 5500 h, SO₂ 5; ISO 9224 b = 0,523)",
                   scene=dict(xaxis_title="Thời gian (năm)", yaxis_title="log₁₀ Cl⁻", zaxis_title="D (µm)"),
                   height=650, margin=dict(l=0, r=0, t=60, b=0))
fig2.write_html(OUT / "3D_2_dien_tien_theo_thoi_gian.html", include_plotlyjs="cdn")

# ================================================================ 3D-3 bề mặt tấm thép theo thời gian
TRAM = {"Nha Trang": hc[(hc.tram == "Nhatrang")].iloc[0], "Hà Nội": hc[(hc.tram == "Hanoi")].iloc[0]}
N, L = 160, 40.0  # lưới 160×160 trên tấm 40×40 mm
xs = np.linspace(0, L, N)
rng = np.random.default_rng(42)
nhieu = rng.standard_normal((N, N))  # cùng một "bề mặt ban đầu" cho mọi thời điểm → diễn tiến liên tục

def truong_ngau_nhien(lc_mm):
    """Trường Gauss có độ dài tương quan lc (lọc FFT), chuẩn hóa trung bình 0, độ lệch 1."""
    k = np.fft.fftfreq(N, d=L / N) * 2 * np.pi
    KX, KY = np.meshgrid(k, k)
    f = np.real(np.fft.ifft2(np.fft.fft2(nhieu) * np.exp(-(KX ** 2 + KY ** 2) * lc_mm ** 2 / 4)))
    return (f - f.mean()) / f.std()

def be_mat(D_tb, t):
    # GIẢ ĐỊNH hiện tượng học: hệ số biến thiên độ sâu 0,25→0,45 và độ dài tương quan 0,6→2,5 mm tăng dần theo t
    cv = 0.25 + 0.20 * (1 - np.exp(-t / 8)); lc = 0.6 + 1.9 * (1 - np.exp(-t / 10))
    z = D_tb * (1 + cv * truong_ngau_nhien(lc))
    return np.maximum(z, 0)

MOC = [1, 5, 10, 20]
ket_qua_3 = []
fig3 = go.Figure()
buoc = []
for i_tram, (ten, row) in enumerate(TRAM.items()):
    r = row.r_corr_um_nam  # trạm đã có số đo năm đầu → dùng số đo (đúng cách làm của ISO 9224)
    for t in MOC:
        Dt = float(D_iso9224(r, t)); z = be_mat(Dt, t)
        ket_qua_3.append(dict(tram=ten, r_do=row.r_corr_um_nam, r_mo_hinh_LOO=row.du_doan_hieu_chinh, t_nam=t, D_tb_um=round(Dt, 1),
                              sau_nhat_um=round(float(z.max()), 1), P95_um=round(float(np.percentile(z, 95)), 1)))
        fig3.add_trace(go.Surface(x=xs, y=xs, z=-z, colorscale="brwnyl_r", cmin=-900, cmax=0, showscale=False,
                                  visible=(i_tram == 0 and t == 1), name=f"{ten} {t} năm"))
        buoc.append(f"{ten} – {t} năm (D̄ = {Dt:.0f} µm)")
steps = [dict(method="update", label=b, args=[{"visible": [j == i for j in range(len(buoc))]},
                                               {"title": f"3D-3. Bề mặt tấm thép CT bị ăn mòn: {b}"}])
         for i, b in enumerate(buoc)]
fig3.update_layout(sliders=[dict(steps=steps, currentvalue=dict(prefix=""), pad=dict(t=30))],
                   title=f"3D-3. Bề mặt tấm thép CT bị ăn mòn: {buoc[0]}",
                   scene=dict(xaxis_title="x (mm)", yaxis_title="y (mm)", zaxis_title="độ sâu (µm)",
                              zaxis=dict(range=[-1000, 50]), aspectratio=dict(x=1, y=1, z=.45)),
                   height=700, margin=dict(l=0, r=0, t=60, b=0),
                   annotations=[dict(text="Độ sâu trung bình: định lượng (số đo năm đầu + ISO 9224). "
                                          "Độ nhám/hố: minh họa với tham số giả định.",
                                     x=0, y=0, xref="paper", yref="paper", showarrow=False, font=dict(size=11))])
fig3.write_html(OUT / "3D_3_be_mat_tam_thep.html", include_plotlyjs="cdn")
pd.DataFrame(ket_qua_3).to_csv(OUT / "be_mat_theo_thoi_gian.csv", index=False, encoding="utf-8-sig")

# ================================================================ Ảnh tĩnh cho slide
fig, axs = plt.subplots(1, 2, figsize=(13, 5.2), subplot_kw=dict(projection="3d"))
for ax, (vung, kh) in zip(axs, KHI_HAU.items()):
    R = r_mo_hinh(kh["T"], TOW, CL, kh["SO2"], vung)
    ax.plot_surface(np.log10(CL), TOW, R, cmap="YlOrRd", vmin=0, vmax=200, alpha=.6, lw=0)
    d = df[df.quoc_gia == vung]
    ax.scatter(np.log10(np.maximum(d.Cl_mg_m2_ngay, .5)), d.TOW_h_nam, d.r_corr_um_nam, c="#1f3b73", s=25, depthshade=False)
    ax.set_xlabel("log₁₀ Cl⁻"); ax.set_ylabel("TOW (h/năm)"); ax.set_zlabel("r (µm/năm)")
    ax.set_zlim(0, 260); ax.set_title(f"{vung}: T = {kh['T']:.0f} °C, SO₂ = {kh['SO2']:.0f}", fontsize=10)
    ax.view_init(24, -128)
fig.suptitle("Tốc độ ăn mòn năm đầu của thép cacbon (mặt = DRF hiệu chỉnh vùng – ngoại suy ngoài miền dữ liệu; điểm = số đo thật)")
fig.tight_layout(); fig.savefig(OUT / "3D_1_mat_dap_ung.png", dpi=150); plt.close(fig)

fig = plt.figure(figsize=(14, 7))
for i, (ten, row) in enumerate(TRAM.items()):
    for j, t in enumerate(MOC):
        ax = fig.add_subplot(2, 4, i * 4 + j + 1, projection="3d")
        Dt = float(D_iso9224(row.r_corr_um_nam, t)); z = be_mat(Dt, t)
        X, Y = np.meshgrid(xs, xs)
        ax.plot_surface(X[::2, ::2], Y[::2, ::2], -z[::2, ::2], cmap="copper", vmin=-900, vmax=0, lw=0)
        ax.set_zlim(-1000, 0); ax.set_title(f"{ten} – {t} năm\nD̄ = {Dt:.0f} µm, sâu nhất {z.max():.0f} µm", fontsize=9)
        ax.set_xticks([]); ax.set_yticks([]); ax.tick_params(labelsize=6); ax.view_init(35, -60)
fig.suptitle("Diễn tiến bề mặt tấm thép cacbon bị ăn mòn (độ sâu TB: số đo năm đầu + ISO 9224; độ nhám: minh họa, tham số giả định)")
fig.tight_layout(); fig.savefig(OUT / "3D_3_be_mat_tam_thep.png", dpi=140); plt.close(fig)

print("Hệ số vùng:", {k: round(v, 3) for k, v in K.items()})
print(pd.DataFrame(ket_qua_3).round(1).to_string(index=False))
for cl, ten in [(2.24, "Hà Nội"), (17.51, "Đồ Sơn"), (100, "Cl 100")]:
    rr = float(r_mo_hinh(25, 5500, cl, 5, "Việt Nam"))
    print(ten, "r =", round(rr, 1), "µm/năm; D(10, 25, 50 năm) =", np.round(D_iso9224(rr, [10, 25, 50]), 0))
