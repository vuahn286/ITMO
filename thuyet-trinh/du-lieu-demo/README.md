# DỮ LIỆU DEMO CHO BÀI THUYẾT TRÌNH

Dữ liệu ở đây **chỉ phục vụ trình diễn**. Dữ liệu của dự án nghiên cứu thật nằm ở `../../du-an-nghien-cuu/03-du-lieu/`.

| Thư mục | Nội dung | Thật / giả lập | Dùng ở |
|---|---|---|---|
| `nhieu-nguon/` | 4 tệp, 3 nguồn công bố (quốc tế 320 trạm · Việt Nam 12 · Nga 18) + ngưỡng ISO + **đáp án** `ket_qua_mong_doi_bang_tong_hop.csv` | 🟢 **Thật** (trích từ C-OLR) | Slide 9 – tổng hợp nhiều nguồn |
| `gia-lap/` | `an_mon_tho.csv` (253 dòng, **14 lỗi cài sẵn**) · `khi_tuong_tram.csv` (108 dòng) · `ke_hoach_cong_viec.csv` (**3 bất hợp lý**) | 🟢 **Giả lập** | Slide 15, 16 – minh họa phát hiện lỗi |
| `may-cach-ly/` | `luoi_dia_hinh_khi_hau.csv` (lưới 120 × 120 ô, 100 m: độ cao, gió, mưa, nhiệt độ, độ ẩm) · `nhiem_vu_bay.json` | 🟢 **Giả lập** – thay cho dữ liệu mật | Slide 20 – Demo 3, công cụ cho máy không Internet |

- `nhieu-nguon/` sinh bằng `../ma-nguon-demo/nhieu-nguon/tao_bo_du_lieu.py` (trừ `nguon4_nguong_ISO_9223.md`). Tệp 1 cố ý giữ nguyên tiêu đề gốc (cột WL không ghi đơn vị) để AI phát hiện.
- `gia-lap/` sinh bằng `../ma-nguon-demo/gia-lap/sinh_du_lieu_gia_lap.py` – hạt giống cố định, chạy lại **giống hệt**. Giá trị "đúng": thép A = 560 / 310 / 160 g/m², n = 0,72. Trên slide luôn ghi "dữ liệu giả lập".
- Kết quả mẫu để đối chiếu: `../ket-qua-demo/gia-lap/`.
