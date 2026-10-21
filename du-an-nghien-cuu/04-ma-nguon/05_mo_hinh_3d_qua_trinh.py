"""
Bước 5 – Mô hình 3D mô tả QUÁ TRÌNH ăn mòn (hoạt hình theo thời gian) và so sánh vật liệu.

3D-4  Khối mẫu thép cacbon tại Nha Trang, 0 → 30 năm (nút "Chạy" / thanh trượt):
      - bề mặt kim loại hạ dần: chiều dày trung bình D(t) = r·t^b (ISO 9224:2012, b = 0,523), r = số đo năm đầu;
      - lớp gỉ phủ trên: dày k_gỉ × D (k_gỉ = 3 – GIẢ ĐỊNH; gỉ sắt có thể tích lớn hơn thép đã mất);
      - hố ăn mòn cục bộ: sâu hơn trung bình theo hệ số hố PF = 3 – GIẢ ĐỊNH, bán kính lớn dần.
      Định lượng có căn cứ: D(t). Hình dạng gỉ, hố: minh họa hiện tượng học, chưa hiệu chỉnh bằng đo thực tế.
3D-5  So sánh 4 kim loại trong cùng cấp ăn mòn C3 (ISO 9223:2012 Bảng 2, đã đối chiếu C1–C3):
      tốc độ năm đầu = trung bình hình học khoảng C3; số mũ b theo ISO 9224:2012 (B1).
"""
import json
import numpy as np
import pandas as pd
from duong_dan import *  # noqa: F401,F403 – đường dẫn dự án
import plotly.graph_objects as go
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

hc = pd.read_csv(BANG / "du_doan_hieu_chinh_VN_RU.csv")
NT = hc[hc.tram == "Nhatrang"].iloc[0]
R_NT = float(NT.r_corr_um_nam)  # 40,55 µm/năm – số đo năm đầu

def D_iso9224(r, t, b):
    t = np.asarray(t, float)
    return np.where(t <= 20, r * t ** b, r * 20 ** b + r * b * 20 ** (b - 1) * (t - 20))

# ---------------------------------------------------------------- tham số GIẢ ĐỊNH (minh họa)
K_GI = 3.0      # lớp gỉ dày gấp 3 chiều dày thép đã mất
PF = 3.0        # hố sâu nhất ≈ 3 × chiều dày trung bình
SO_HO = 14

N, L = 90, 20.0  # lưới 90×90 trên mẫu 20×20 mm
xs = np.linspace(0, L, N).round(2)
X, Y = np.meshgrid(xs, xs)
rng = np.random.default_rng(7)
nhieu = rng.standard_normal((N, N))
k = np.fft.fftfreq(N, d=L / N) * 2 * np.pi
KX, KY = np.meshgrid(k, k)
f = np.real(np.fft.ifft2(np.fft.fft2(nhieu) * np.exp(-(KX ** 2 + KY ** 2) * 1.2 ** 2 / 4)))
NHAM = (f - f.mean()) / f.std()                 # độ nhám, trung bình 0
HO = rng.uniform(1.5, L - 1.5, (SO_HO, 2))       # vị trí hố
HO_W = rng.uniform(0.6, 1.0, SO_HO)              # trọng số độ sâu từng hố

def hinh_dang_ho(t):
    """Trường hố 0..1, bán kính tăng theo t^0,3."""
    rk = 0.35 * max(t, 0.05) ** 0.3
    z = np.zeros_like(X)
    for (cx, cy), w in zip(HO, HO_W):
        z = np.maximum(z, w * np.exp(-((X - cx) ** 2 + (Y - cy) ** 2) / (2 * rk ** 2)))
    return z

def trang_thai(t):
    Dtb = float(D_iso9224(R_NT, t, 0.523))
    ho = hinh_dang_ho(t)
    mat = Dtb * (1 + 0.15 * NHAM) + (PF - 1) * Dtb * ho   # độ sâu kim loại mất (µm, dương)
    mat = np.maximum(mat, 0)
    mat *= Dtb / mat.mean() if mat.mean() > 0 else 1     # giữ đúng trung bình = D(t)
    kim_loai = -mat
    gi = kim_loai + K_GI * Dtb * (1 + 0.25 * NHAM) * (1 - 0.3 * ho)
    return Dtb, kim_loai, gi

MOC = [0, 1, 2, 3, 5, 7, 10, 15, 20, 25, 30]
bang = []
frames = []
for t in MOC:
    Dtb, km, gi = trang_thai(t)
    bang.append(dict(t_nam=t, D_tb_um=round(Dtb, 1), ton_that_g_m2=round(Dtb * 7.86, 0),
                     ho_sau_nhat_um=round(float(-km.min()), 1), lop_gi_tb_um=round(float((gi - km).mean()), 1)))
    frames.append(go.Frame(name=str(t), data=[
        go.Surface(z=km.round(0), x=xs, y=xs, colorscale=[[0, "#4a4f57"], [1, "#c9ced6"]], cmin=-PF * 600, cmax=0,
                   showscale=False, name="Kim loại"),
        go.Surface(z=gi.round(0), x=xs, y=xs, colorscale=[[0, "#7a3410"], [1, "#d98a3a"]], opacity=0.55,
                   showscale=False, name="Lớp gỉ")],
        layout=go.Layout(title=f"3D-4. Quá trình ăn mòn thép cacbon tại Nha Trang – năm {t}: "
                               f"thép mất trung bình {Dtb:.0f} µm ({Dtb * 7.86:.0f} g/m²), hố sâu nhất {-km.min():.0f} µm")))

fig = go.Figure(data=frames[1].data, frames=frames)
fig.update_layout(
    title=frames[1].layout.title.text, height=700, margin=dict(l=0, r=0, t=60, b=0),
    scene=dict(xaxis_title="x (mm)", yaxis_title="y (mm)", zaxis_title="z (µm) – 0 = bề mặt ban đầu",
               zaxis=dict(range=[-1500, 1700]), aspectratio=dict(x=1, y=1, z=0.6)),
    updatemenus=[dict(type="buttons", x=0.02, y=0.02, buttons=[
        dict(label="▶ Chạy", method="animate", args=[None, dict(frame=dict(duration=350, redraw=True), fromcurrent=True)]),
        dict(label="⏸ Dừng", method="animate", args=[[None], dict(mode="immediate", frame=dict(duration=0))])])],
    sliders=[dict(currentvalue=dict(prefix="Năm: "), pad=dict(t=40), active=1,
                  steps=[dict(label=str(t), method="animate",
                              args=[[str(t)], dict(mode="immediate", frame=dict(duration=0, redraw=True))]) for t in MOC])],
    annotations=[dict(text="Xám: kim loại · Nâu (trong suốt): lớp gỉ · D(t) theo ISO 9224, r = 40,6 µm/năm (đo thực địa). "
                           "Hình dạng gỉ và hố: minh họa, tham số giả định.", showarrow=False, x=0, y=1.02,
                      xref="paper", yref="paper", xanchor="left", font=dict(size=11))])
fig.write_html(MO_HINH_3D / "3D_4_qua_trinh_an_mon_dong.html", include_plotlyjs="cdn")
pd.DataFrame(bang).to_csv(BANG / "qua_trinh_an_mon_Nha_Trang.csv", index=False, encoding="utf-8-sig")

# PNG 4 thời điểm cho slide: hàng trên – bề mặt kim loại 3D (đã bóc gỉ); hàng dưới – mặt cắt qua hố sâu nhất
fig_p = plt.figure(figsize=(16, 7.5))
for i, t in enumerate([1, 5, 10, 30]):
    Dtb, km, gi = trang_thai(t)
    ax = fig_p.add_subplot(2, 4, i + 1, projection="3d")
    ax.plot_surface(X, Y, km, cmap="copper", vmin=-650, vmax=0, linewidth=0, rstride=1, cstride=1)
    ax.set_zlim(-650, 0); ax.set_xlabel("mm"); ax.set_ylabel("mm"); ax.set_zlabel("µm")
    ax.set_title(f"Năm {t}: thép mất trung bình {Dtb:.0f} µm\nhố sâu nhất {-km.min():.0f} µm", fontsize=10)
    hang = np.unravel_index(km.argmin(), km.shape)[0]
    ax2 = fig_p.add_subplot(2, 4, i + 5)
    ax2.fill_between(xs, -700, km[hang], color="#8a9099", label="Thép")
    ax2.fill_between(xs, km[hang], gi[hang], color="#b5562a", alpha=.8, label="Lớp gỉ")
    ax2.axhline(0, ls="--", c="k", lw=.8, label="Bề mặt ban đầu")
    ax2.set_ylim(-700, 1000); ax2.set_xlabel("x (mm) – mặt cắt qua hố sâu nhất"); ax2.set_ylabel("µm")
    if i == 0: ax2.legend(loc="upper right", fontsize=8)
fig_p.suptitle("Quá trình ăn mòn thép cacbon tại Nha Trang – D(t) theo ISO 9224 (r = 40,6 µm/năm đo thực địa); "
               "hình dạng hố và lớp gỉ: minh họa, tham số giả định", fontsize=11)
fig_p.tight_layout(); fig_p.savefig(MO_HINH_3D / "3D_4_qua_trinh_an_mon.png", dpi=130); plt.close(fig_p)

# ================================================================ 3D-5 so sánh vật liệu, cấp C3
# ISO 9223:2012 Bảng 2, cấp C3, g/m²·năm; khối lượng riêng g/cm³; b: ISO 9224:2012 (B1)
VL = {"Thép cacbon": dict(c3=(200, 400), rho=7.86, b=0.523),
      "Kẽm":         dict(c3=(5, 15),    rho=7.14, b=0.813),
      "Đồng":        dict(c3=(5, 12),    rho=8.96, b=0.667),
      "Nhôm":        dict(c3=(0.6, 2),   rho=2.70, b=0.728)}
t_ax = np.linspace(0, 30, 61)
fig5 = go.Figure()
bang5 = []
for j, (ten, v) in enumerate(VL.items()):
    lo, hi = (np.array(v["c3"]) / v["rho"])            # µm/năm
    r_ax = np.linspace(lo, hi, 12)
    TT, RR = np.meshgrid(t_ax, r_ax)
    Z = np.log10(np.maximum(D_iso9224(RR, TT, v["b"]), 1e-2))
    fig5.add_trace(go.Surface(x=TT, y=np.full_like(TT, j) + (RR - lo) / (hi - lo) * 0.6 - 0.3, z=Z,
                              surfacecolor=np.full_like(TT, j), colorscale="Turbo", cmin=0, cmax=3, showscale=False,
                              name=ten, customdata=10 ** Z,
                              hovertemplate=f"{ten}<br>t=%{{x:.0f}} năm<br>D=%{{customdata:.1f}} µm<extra></extra>"))
    r_tb = float(np.sqrt(lo * hi))
    bang5.append(dict(vat_lieu=ten, r_C3_um_nam_min=round(lo, 2), r_C3_um_nam_max=round(hi, 2), b_ISO9224=v["b"],
                      D_10nam_um=round(float(D_iso9224(r_tb, 10, v["b"])), 1),
                      D_30nam_um=round(float(D_iso9224(r_tb, 30, v["b"])), 1)))
fig5.update_layout(title="3D-5. Chiều dày kim loại bị ăn mòn theo thời gian – 4 vật liệu trong cùng cấp C3 "
                         "(ISO 9223 Bảng 2; ISO 9224 b)",
                   scene=dict(xaxis_title="Thời gian (năm)",
                              yaxis=dict(title="", tickvals=list(range(4)), ticktext=list(VL)),
                              zaxis=dict(title="log₁₀ D (µm)")),
                   height=650, margin=dict(l=0, r=0, t=60, b=0))
fig5.write_html(MO_HINH_3D / "3D_5_so_sanh_vat_lieu.html", include_plotlyjs="cdn")
pd.DataFrame(bang5).to_csv(BANG / "so_sanh_vat_lieu_C3.csv", index=False, encoding="utf-8-sig")

json.dump(dict(gia_dinh=dict(K_GI=K_GI, PF=PF, so_ho=SO_HO), r_Nha_Trang_um_nam=R_NT),
          open(MO_HINH_3D / "tham_so_3D_4.json", "w"), ensure_ascii=False, indent=1)
print(pd.DataFrame(bang).to_string(index=False))
print(pd.DataFrame(bang5).to_string(index=False))
