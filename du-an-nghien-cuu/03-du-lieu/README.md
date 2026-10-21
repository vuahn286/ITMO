# 03 – DỮ LIỆU CỦA DỰ ÁN

Tổ chức theo nguyên tắc **FAIR** (dễ tìm – dễ truy cập – liên thông – tái sử dụng): dữ liệu gốc chỉ đọc, mọi bước xử lý bằng mã, mỗi tệp có nguồn và giấy phép.

```
03-du-lieu/
├── 1-du-lieu-tho/        ← GỐC, CHỈ ĐỌC – không bao giờ sửa tay
│   ├── c-olr/            387 số đo ăn mòn thép cacbon năm đầu (xlsx) + LICENSE (MIT) + NGUON.md
│   └── tieu-chuan/       ngưỡng cấp ăn mòn ISO 9223 (csv) + NGUON.md
├── 2-da-xu-ly/           ← SINH RA bởi 04-ma-nguon/01_hop_nhat_kiem_tra.py
│   ├── du_lieu_hop_nhat.csv       bảng hợp nhất 387 dòng, đơn vị đã chuẩn hóa, cấp ISO tính lại
│   └── kiem_tra_chat_luong.csv    nhật ký kiểm tra chất lượng (8 mục)
└── 3-bo-sung/            ← chỗ thả dữ liệu mới (theo MAU_bo_sung.csv.template)
```

## Dòng dữ liệu

```
1-du-lieu-tho/c-olr/C-OLR_datasets.xlsx ─┐
3-bo-sung/*.csv ─────────────────────────┼─► 01_hop_nhat_kiem_tra ─► 2-da-xu-ly/ ─► 02_mo_hinh ─► 03_hieu_chinh ─► 04_mo_hinh_3d ─► 05-ket-qua/
1-du-lieu-tho/tieu-chuan/ (ngưỡng ISO) ──┘
```

## Thống kê bộ dữ liệu

| Tập | Nguồn | Số quan sát |
|---|---|---|
| Huấn luyện | ISOCORRAG (Chico và cs., 2017) | 190 |
| Huấn luyện | MICAT (Pintos và cs., 2000) | 130 |
| Kiểm định độc lập | Việt Nam (Lê Thị Hồng Liên và cs., 2007) | 12 |
| Kiểm định độc lập | Nga (Viễn Đông, Murmansk) | 18 |
| Kiểm định độc lập | Tây Ban Nha, Canary, Colombia | 37 |
| **Tổng** | | **387** |

## Từ điển dữ liệu – `2-da-xu-ly/du_lieu_hop_nhat.csv`

| Cột | Ý nghĩa | Đơn vị / giá trị |
|---|---|---|
| `nguon` | Nhóm nguồn (ISOCORRAG, MICAT, External Validation…) | – |
| `tram` | Tên / mã trạm | – |
| `loai_khi_quyen` | 1 nông thôn · 2 đô thị · 3 công nghiệp · 4 biển (suy ra từ dữ liệu) | 1–4 |
| `T_C` | Nhiệt độ trung bình năm | °C |
| `TOW_h_nam` | Thời gian ẩm ướt | giờ/năm |
| `Cl_mg_m2_ngay`, `SO2_mg_m2_ngay` | Tốc độ lắng đọng clorua, SO₂ | mg/m²/ngày |
| `r_corr_um_nam` | Tốc độ ăn mòn năm đầu thép cacbon | µm/năm |
| `r_corr_g_m2_nam` | Quy đổi (× 7,86) | g/m²/năm |
| `cap_goc`, `cap_tinh_lai` | Cấp ISO 9223 theo nguồn / tính lại theo ngưỡng | C1–CX |
| `tai_lieu`, `quoc_gia` | Công bố gốc, quốc gia | – |
| `tap` | `huan_luyen` / `kiem_dinh_doc_lap` | – |

## Phát hiện chất lượng dữ liệu (chi tiết: `2-da-xu-ly/kiem_tra_chat_luong.csv`)

1. **Lỗi đơn vị trong nguồn:** cột WL ghi g/m² nhưng thực chất µm/năm (99,5% khớp cột cấp ăn mòn nếu hiểu là µm/năm; 33,1% nếu g/m²).
2. **2 trạm ghi sai cấp:** Barcelona (49,9 µm → C3, nguồn ghi C4); El Hierro (263,2 µm → CX, nguồn ghi C5).
3. 2 trạm TOW < 300 h/năm (PE41, PE42) – giữ, đánh dấu. 4 giá trị Cl⁻ hoặc SO₂ = 0 – thay 0,1 khi lấy log.
4. Không có trạm trùng giữa tập huấn luyện và kiểm định (kiểm tra bằng Skill – `05-ket-qua/kiem-tra-bang-skill/`).

## Phân loại và giấy phép

- Toàn bộ thư mục: 🟢 **xanh** – dữ liệu đã công bố, giấy phép MIT (kho C-OLR). Ghi nguồn khi sử dụng.
- `3-bo-sung/`: chỉ thả dữ liệu xanh. Dữ liệu nhóm vàng (số liệu trạm chưa công bố) xử lý trên máy nội bộ.
