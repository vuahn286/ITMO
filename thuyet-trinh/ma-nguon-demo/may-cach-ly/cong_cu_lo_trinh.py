"""
CÔNG CỤ ƯỚC LƯỢNG LỘ TRÌNH UAV THEO ĐỊA HÌNH VÀ KHÍ HẬU NHIỆT ĐỚI – chạy trên máy KHÔNG Internet.

Mục đích (Demo 3): minh họa cách dùng AI viết nhanh một công cụ xử lý dữ liệu trên dữ liệu GIẢ,
rồi chép công cụ vào máy không Internet để xử lý dữ liệu THẬT của đề tài mật. AI không bao giờ thấy dữ liệu thật.

Yêu cầu: Python ≥ 3.9, numpy, matplotlib. Không dùng mạng, không gửi dữ liệu ra ngoài.

Chạy:
  python cong_cu_lo_trinh.py --du-lieu luoi.csv --nhiem-vu nhiem_vu.json --ra ket_qua/ [--cau-hinh cau_hinh.json]

Đầu vào:
  luoi.csv        i,j,do_cao_m,gio_u_ms,gio_v_ms,mua_mm_h,nhiet_do_C,do_am_pct
                  (i: hàng, tăng về phía Bắc; j: cột, tăng về phía Đông; gió u – thành phần Đông, v – thành phần Bắc)
  nhiem_vu.json   o_luoi_m, diem_xuat_phat [i, j], diem_den [i, j], do_cao_bay_tren_mat_dat_m
  cau_hinh.json   thông số thiết bị bay và ngưỡng an toàn (mặc định: cau_hinh_mac_dinh.json cạnh tệp này)

Mô hình (đơn giản, có thể thay bằng mô hình của đơn vị):
  - Công suất bay của thiết bị nhiều cánh quạt tỉ lệ 1/√ρ (lý thuyết động lượng); ρ – mật độ không khí ẩm
    tính từ độ cao (khí quyển chuẩn), nhiệt độ, độ ẩm.
  - Mưa làm tăng công suất theo hệ số he_so_mua (GIẢ ĐỊNH – cần hiệu chỉnh bằng thử nghiệm).
  - Tốc độ so với mặt đất tính theo tam giác vận tốc với gió; leo cao tốn thêm m·g·Δh / hiệu suất.
  - Ô cấm bay: mưa, gió vượt ngưỡng hoặc độ cao bay vượt trần bay.
  - Lộ trình tối ưu = đường tốn ít năng lượng nhất trên lưới 8 hướng (thuật toán Dijkstra).
"""
import argparse
import hashlib
import heapq
import json
from datetime import datetime
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

G = 9.80665
RHO0 = 1.225
HUONG = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


# ------------------------------------------------------------------ đọc dữ liệu
def doc_luoi(duong_dan):
    a = np.genfromtxt(duong_dan, delimiter=",", names=True, encoding="utf-8")
    can = ["i", "j", "do_cao_m", "gio_u_ms", "gio_v_ms", "mua_mm_h", "nhiet_do_C", "do_am_pct"]
    thieu = [c for c in can if c not in a.dtype.names]
    if thieu:
        raise SystemExit(f"Thiếu cột: {thieu}")
    ni, nj = int(a["i"].max()) + 1, int(a["j"].max()) + 1
    if len(a) != ni * nj:
        raise SystemExit(f"Lưới không đủ ô: có {len(a)}, cần {ni * nj}")
    luoi = {}
    for c in can[2:]:
        m = np.full((ni, nj), np.nan)
        m[a["i"].astype(int), a["j"].astype(int)] = a[c]
        if np.isnan(m).any():
            raise SystemExit(f"Cột {c} có ô trống")
        luoi[c] = m
    return luoi


def sha256(duong_dan):
    return hashlib.sha256(Path(duong_dan).read_bytes()).hexdigest()


# ------------------------------------------------------------------ mô hình vật lý
def mat_do_khong_khi(do_cao_m, nhiet_do_C, do_am_pct):
    p = 101325 * (1 - 2.25577e-5 * do_cao_m) ** 5.25588                     # Pa, khí quyển chuẩn
    es = 611.2 * np.exp(17.67 * nhiet_do_C / (nhiet_do_C + 243.5))         # Pa, áp suất hơi bão hòa
    e = do_am_pct / 100 * es
    Tk = nhiet_do_C + 273.15
    return (p - e) / (287.05 * Tk) + e / (461.5 * Tk)


def cong_suat(luoi, ch, cao_bay, bo_qua=()):
    rho = RHO0 if "mat_do" in bo_qua else mat_do_khong_khi(cao_bay, luoi["nhiet_do_C"], luoi["do_am_pct"])
    mua = 0 if "mua" in bo_qua else luoi["mua_mm_h"]
    return ch["cong_suat_bay_W"] * np.sqrt(RHO0 / rho) * (1 + ch["he_so_mua_moi_mm_h"] * mua)


def nang_luong_canh(luoi, ch, cao_bay, P, di, dj, o_luoi, a, b, bo_qua=()):
    """Năng lượng (J) và thời gian (s) bay từ ô a sang ô b kề nhau; inf nếu không bay được."""
    d = o_luoi * np.hypot(di, dj)
    ex, ey = dj / np.hypot(di, dj), di / np.hypot(di, dj)            # hướng bay (Đông, Bắc)
    if "gio" in bo_qua:
        wx = wy = 0.0
    else:
        wx = 0.5 * (luoi["gio_u_ms"][a] + luoi["gio_u_ms"][b])
        wy = 0.5 * (luoi["gio_v_ms"][a] + luoi["gio_v_ms"][b])
    w_doc = wx * ex + wy * ey
    w_ngang = abs(wx * ey - wy * ex)
    va = ch["toc_do_bay_ms"]
    if w_ngang >= va:
        return np.inf, np.inf
    vg = w_doc + np.sqrt(va ** 2 - w_ngang ** 2)
    if vg < 1.0:
        return np.inf, np.inf
    t = d / vg
    dh = 0 if "leo" in bo_qua else max(cao_bay[b] - cao_bay[a], 0)
    return 0.5 * (P[a] + P[b]) * t + ch["khoi_luong_kg"] * G * dh / ch["hieu_suat_leo"], t


def o_cam_bay(luoi, ch, cao_bay):
    toc_do_gio = np.hypot(luoi["gio_u_ms"], luoi["gio_v_ms"])
    return ((luoi["mua_mm_h"] > ch["mua_cam_bay_mm_h"]) | (toc_do_gio > ch["gio_cam_bay_ms"])
            | (cao_bay > ch["tran_bay_m"]))


# ------------------------------------------------------------------ tìm lộ trình
def dijkstra(luoi, ch, nv):
    ni, nj = luoi["do_cao_m"].shape
    cao_bay = luoi["do_cao_m"] + nv["do_cao_bay_tren_mat_dat_m"]
    P = cong_suat(luoi, ch, cao_bay)
    cam = o_cam_bay(luoi, ch, cao_bay)
    s, e = tuple(nv["diem_xuat_phat"]), tuple(nv["diem_den"])
    for ten, o in (("xuất phát", s), ("đích", e)):
        if cam[o]:
            raise SystemExit(f"Điểm {ten} {o} nằm trong vùng cấm bay")
    dist = np.full((ni, nj), np.inf); dist[s] = 0
    truoc = {}
    hang = [(0.0, s)]
    while hang:
        dcur, a = heapq.heappop(hang)
        if a == e:
            break
        if dcur > dist[a]:
            continue
        for di, dj in HUONG:
            b = (a[0] + di, a[1] + dj)
            if not (0 <= b[0] < ni and 0 <= b[1] < nj) or cam[b]:
                continue
            E, _ = nang_luong_canh(luoi, ch, cao_bay, P, di, dj, nv["o_luoi_m"], a, b)
            if dcur + E < dist[b]:
                dist[b] = dcur + E; truoc[b] = a
                heapq.heappush(hang, (dist[b], b))
    if not np.isfinite(dist[e]):
        return None, cam, cao_bay
    duong = [e]
    while duong[-1] != s:
        duong.append(truoc[duong[-1]])
    return duong[::-1], cam, cao_bay


def duong_thang(s, e):
    n = max(abs(e[0] - s[0]), abs(e[1] - s[1]))
    return [(round(s[0] + (e[0] - s[0]) * k / n), round(s[1] + (e[1] - s[1]) * k / n)) for k in range(n + 1)]


def danh_gia(duong, luoi, ch, nv, cao_bay, bo_qua=()):
    P = cong_suat(luoi, ch, cao_bay, bo_qua)
    E = T = D = 0.0
    tich_luy = [0.0]
    for a, b in zip(duong[:-1], duong[1:]):
        di, dj = b[0] - a[0], b[1] - a[1]
        e_, t_ = nang_luong_canh(luoi, ch, cao_bay, P, di, dj, nv["o_luoi_m"], a, b, bo_qua)
        E += e_; T += t_; D += nv["o_luoi_m"] * np.hypot(di, dj)
        tich_luy.append(E / 3600)
    return dict(nang_luong_Wh=E / 3600, thoi_gian_phut=T / 60, quang_duong_km=D / 1000, tich_luy_Wh=tich_luy)


# ------------------------------------------------------------------ chương trình chính
def main():
    ap = argparse.ArgumentParser(description="Ước lượng lộ trình UAV theo địa hình và khí hậu – chạy ngoại tuyến")
    ap.add_argument("--du-lieu", required=True)
    ap.add_argument("--nhiem-vu", required=True)
    ap.add_argument("--cau-hinh", default=str(Path(__file__).with_name("cau_hinh_mac_dinh.json")))
    ap.add_argument("--ra", required=True)
    tham_so = ap.parse_args()
    ra = Path(tham_so.ra); ra.mkdir(parents=True, exist_ok=True)

    luoi = doc_luoi(tham_so.du_lieu)
    nv = json.load(open(tham_so.nhiem_vu, encoding="utf-8"))
    ch = json.load(open(tham_so.cau_hinh, encoding="utf-8"))

    duong, cam, cao_bay = dijkstra(luoi, ch, nv)
    if duong is None:
        raise SystemExit("Không tìm được lộ trình an toàn giữa hai điểm")
    kq = danh_gia(duong, luoi, ch, nv, cao_bay)
    nv_ve = dict(nv, diem_xuat_phat=nv["diem_den"], diem_den=nv["diem_xuat_phat"])
    duong_ve, _, _ = dijkstra(luoi, ch, nv_ve)
    kq_ve = danh_gia(duong_ve, luoi, ch, nv, cao_bay) if duong_ve else None
    pin_dung_duoc = ch["dung_luong_pin_Wh"] * (1 - ch["du_tru_pin_pct"] / 100)

    thang = duong_thang(tuple(nv["diem_xuat_phat"]), tuple(nv["diem_den"]))
    so_o_cam_thang = int(sum(cam[o] for o in thang))
    kq_thang = danh_gia(thang, luoi, ch, nv, cao_bay)

    anh_huong = {}
    for ten, bo in [("Gió", ("gio",)), ("Mưa", ("mua",)), ("Mật độ không khí (nóng, ẩm, độ cao)", ("mat_do",)),
                    ("Leo cao theo địa hình", ("leo",))]:
        e0 = danh_gia(duong, luoi, ch, nv, cao_bay, bo)["nang_luong_Wh"]
        anh_huong[ten] = kq["nang_luong_Wh"] - e0

    # --- lộ trình CSV
    with open(ra / "lo_trinh.csv", "w", encoding="utf-8") as f:
        f.write("thu_tu,i,j,x_dong_m,y_bac_m,do_cao_dia_hinh_m,do_cao_bay_m,nang_luong_tich_luy_Wh\n")
        for k, (o, el) in enumerate(zip(duong, kq["tich_luy_Wh"])):
            f.write(f"{k},{o[0]},{o[1]},{o[1] * nv['o_luoi_m']:.0f},{o[0] * nv['o_luoi_m']:.0f},"
                    f"{luoi['do_cao_m'][o]:.1f},{cao_bay[o]:.1f},{el:.2f}\n")

    # --- bản đồ
    o = nv["o_luoi_m"] / 1000
    ni, nj = cam.shape
    ext = [0, nj * o, 0, ni * o]
    fig, ax = plt.subplots(1, 2, figsize=(15, 6.5))
    im = ax[0].imshow(luoi["do_cao_m"], origin="lower", extent=ext, cmap="terrain")
    fig.colorbar(im, ax=ax[0], label="Độ cao địa hình (m)")
    ax[0].contour(np.ma.masked_less(luoi["mua_mm_h"], 1), levels=[2, 5, 10, 20], colors="#1f5fbf",
                  linewidths=.8, origin="lower", extent=ext)
    ax[0].contourf(cam, levels=[.5, 1.5], colors="none", hatches=["xxx"], origin="lower", extent=ext)
    ax[0].contour(cam, levels=[.5], colors="red", linewidths=1.2, origin="lower", extent=ext)
    sl = slice(None, None, 8)
    ax[0].quiver(np.arange(nj)[sl] * o, np.arange(ni)[sl] * o, luoi["gio_u_ms"][sl, sl], luoi["gio_v_ms"][sl, sl],
                 color="#444", alpha=.6, scale=250)
    ax[0].plot([p[1] * o for p in thang], [p[0] * o for p in thang], "k--", lw=1.4,
               label=f"Đường thẳng ({so_o_cam_thang} ô cấm bay)")
    ax[0].plot([p[1] * o for p in duong], [p[0] * o for p in duong], color="#d7191c", lw=2.5,
               label=f"Lộ trình tối ưu ({kq['nang_luong_Wh']:.0f} Wh)")
    if duong_ve:
        ax[0].plot([p[1] * o for p in duong_ve], [p[0] * o for p in duong_ve], color="#fdae61", lw=2, ls="-.",
                   label=f"Lộ trình chiều về ({kq_ve['nang_luong_Wh']:.0f} Wh)")
    ax[0].plot(*[[x * o] for x in nv["diem_xuat_phat"][::-1]], "go", ms=9)
    ax[0].plot(*[[x * o] for x in nv["diem_den"][::-1]], "bs", ms=9)
    ax[0].set_xlabel("Đông (km)"); ax[0].set_ylabel("Bắc (km)")
    ax[0].set_title("Địa hình · đường xanh: mưa (mm/h) · gạch đỏ: cấm bay · mũi tên: gió")
    ax[0].legend(loc="lower right", fontsize=9)

    x_km = np.r_[0, np.cumsum([np.hypot(b[0] - a[0], b[1] - a[1]) * o for a, b in zip(duong[:-1], duong[1:])])]
    ax[1].fill_between(x_km, 0, [luoi["do_cao_m"][p] for p in duong], color="#a6845c", label="Địa hình")
    ax[1].plot(x_km, [cao_bay[p] for p in duong], color="#d7191c", lw=2, label="Độ cao bay")
    ax[1].axhline(ch["tran_bay_m"], color="red", ls=":", label="Trần bay")
    ax2 = ax[1].twinx()
    ax2.plot(x_km, kq["tich_luy_Wh"], color="#2c7bb6", label="Năng lượng tích lũy")
    ax2.axhline(pin_dung_duoc, color="#2c7bb6", ls="-.", lw=1, label=f"Pin dùng được ({pin_dung_duoc:.0f} Wh)")
    ax2.set_ylim(0, 1.6 * max(pin_dung_duoc, kq["nang_luong_Wh"]))
    ax2.set_ylabel("Năng lượng (Wh)")
    ax[1].set_xlabel("Quãng đường (km)"); ax[1].set_ylabel("Độ cao (m)")
    ax[1].set_title("Mặt cắt dọc lộ trình")
    h1, l1 = ax[1].get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
    ax[1].legend(h1 + h2, l1 + l2, loc="upper left", fontsize=9)
    fig.suptitle(nv.get("ten", "Lộ trình"), fontsize=12)
    fig.tight_layout(); fig.savefig(ra / "ban_do_lo_trinh.png", dpi=130); plt.close(fig)

    # --- báo cáo
    du = pin_dung_duoc - kq["nang_luong_Wh"]
    tong = kq["nang_luong_Wh"] + (kq_ve["nang_luong_Wh"] if kq_ve else np.inf)
    du_kh = pin_dung_duoc - tong
    dong = [f"# BÁO CÁO LỘ TRÌNH – {nv.get('ten', '')}", "",
            f"- Thời điểm chạy: {datetime.now():%d/%m/%Y %H:%M} · Máy: không Internet (công cụ không dùng mạng)",
            f"- Tệp dữ liệu: `{Path(tham_so.du_lieu).name}` · SHA-256: `{sha256(tham_so.du_lieu)}`",
            f"- Cấu hình: `{Path(tham_so.cau_hinh).name}` · SHA-256: `{sha256(tham_so.cau_hinh)}`", "",
            "## Kết quả", "",
            "| Chỉ tiêu | Lộ trình tối ưu – chiều đi | Đường thẳng – chiều đi | Lộ trình tối ưu – chiều về |",
            "|---|---|---|---|",
            f"| Quãng đường (km) | {kq['quang_duong_km']:.1f} | {kq_thang['quang_duong_km']:.1f} | {kq_ve['quang_duong_km'] if kq_ve else float('nan'):.1f} |",
            f"| Thời gian bay (phút) | {kq['thoi_gian_phut']:.1f} | {kq_thang['thoi_gian_phut']:.1f} | {kq_ve['thoi_gian_phut'] if kq_ve else float('nan'):.1f} |",
            f"| Năng lượng (Wh) | {kq['nang_luong_Wh']:.0f} | {kq_thang['nang_luong_Wh']:.0f} | {kq_ve['nang_luong_Wh'] if kq_ve else float('nan'):.0f} |",
            f"| Số ô cấm bay đi qua | 0 | {so_o_cam_thang} | 0 |", "",
            f"Pin dùng được: {pin_dung_duoc:.0f} Wh (đã trừ dự trữ {ch['du_tru_pin_pct']}%).",
            "- Chiều đi: " + (f"**ĐỦ**, còn dư {du:.0f} Wh." if du >= 0 else f"**KHÔNG ĐỦ**, thiếu {-du:.0f} Wh."),
            "- Chiều về: " + (f"**ĐỦ**, còn dư {pin_dung_duoc - kq_ve['nang_luong_Wh']:.0f} Wh." if kq_ve and kq_ve['nang_luong_Wh'] <= pin_dung_duoc else f"**KHÔNG ĐỦ**, thiếu {kq_ve['nang_luong_Wh'] - pin_dung_duoc:.0f} Wh." if kq_ve else "không tìm được lộ trình."),
            "- Khứ hồi: " + (f"**ĐỦ**, còn dư {du_kh:.0f} Wh." if du_kh >= 0 else f"**KHÔNG ĐỦ**, thiếu {-du_kh:.0f} Wh → cần điểm thay pin hoặc đổi nhiệm vụ."), "",
            "## Ảnh hưởng của từng yếu tố trên lộ trình tối ưu – chiều đi", "",
            "| Yếu tố | Năng lượng tăng thêm (Wh) | % tổng |", "|---|---|---|"]
    for ten, v in anh_huong.items():
        dong.append(f"| {ten} | {v:+.1f} | {100 * v / kq['nang_luong_Wh']:+.1f}% |")
    if kq_ve:
        e_ve0 = danh_gia(duong_ve, luoi, ch, nv, cao_bay, ("gio",))["nang_luong_Wh"]
        dong += ["", f"Chiều về (ngược gió): gió làm tăng {kq_ve['nang_luong_Wh'] - e_ve0:+.0f} Wh "
                     f"({100 * (kq_ve['nang_luong_Wh'] - e_ve0) / kq_ve['nang_luong_Wh']:+.0f}% tổng chiều về)."]
    dong += ["", "*Mật độ không khí: so với khí quyển chuẩn mực nước biển 15 °C (ρ = 1,225 kg/m³).*", "",
             "## Lưu ý", "",
             "- Hệ số mưa, ngưỡng cấm bay, công suất bay là **tham số cấu hình** – đơn vị thay bằng số liệu thử nghiệm của thiết bị thật.",
             "- Kết quả là ước lượng để lập kế hoạch; người có thẩm quyền quyết định."]
    (ra / "bao_cao.md").write_text("\n".join(dong), encoding="utf-8")
    print("\n".join(dong))


if __name__ == "__main__":
    main()
