# DỰ ÁN NGHIÊN CỨU: KHẢ NĂNG ÁP DỤNG MÔ HÌNH ĂN MÒN KHÍ QUYỂN QUỐC TẾ CHO KHÍ HẬU NHIỆT ĐỚI VIỆT NAM

> Dự án nghiên cứu **thật**, dùng **dữ liệu thật đã công bố** (387 số đo thực địa), thực hiện với sự hỗ trợ của AI Agent ở mọi giai đoạn – dùng làm ví dụ xuyên suốt cho bài thuyết trình "AI Agent và sự chuyển đổi phương thức nghiên cứu khoa học" (`../thuyet-trinh/`).

**Câu hỏi nghiên cứu:** Mô hình liều – đáp ứng học từ dữ liệu quốc tế có dự báo đúng tốc độ ăn mòn năm đầu của thép cacbon ở Việt Nam không, và sai lệch theo vùng khí hậu lớn đến đâu?

**Trả lời ngắn:** Không. Mô hình quốc tế **dự đoán thấp hơn thực đo khoảng 31%** ở Việt Nam (chỉ 2/12 trạm đúng cấp ăn mòn); hiệu chỉnh vùng nâng lên 9/12. Cần bộ hằng số riêng cho khí hậu nhiệt đới.

---

## Cấu trúc – theo vòng đời một nhiệm vụ khoa học

| Thư mục | Giai đoạn | Nội dung chính | Trạng thái |
|---|---|---|---|
| `00-quan-ly-du-an/` | Quản lý | Kế hoạch, **nhật ký thực hiện** (kể cả các lần sai và sửa), việc còn lại | ✅ |
| `01-tong-quan-tai-lieu/` | Tài liệu → khoảng trống | 13 tài liệu đã xác minh (`.csv`, `.bib`), ma trận bằng chứng, 3 khoảng trống | ✅ |
| `02-de-xuat-thuyet-minh/` | Đề xuất | Bản nháp đề xuất nhiệm vụ; biểu mẫu Trung tâm | 🟡 Chờ biểu mẫu |
| `03-du-lieu/` | Dữ liệu | Thô (chỉ đọc) → đã xử lý → bổ sung; siêu dữ liệu, từ điển dữ liệu | ✅ |
| `04-ma-nguon/` | Phân tích | 4 bước: hợp nhất – kiểm tra → mô hình → hiệu chỉnh vùng → 3D | ✅ |
| `05-ket-qua/` | Kết quả | Bảng, hình, mô hình, mô hình 3D tương tác, kiểm tra bằng Skill | ✅ |
| `06-bai-bao/` | Công bố | Bản thảo bài báo (tóm tắt Việt – Anh, IMRaD) | ✅ Bản thảo |
| `07-bao-cao/` | Báo cáo | Báo cáo tổng hợp kết quả | ✅ Bản đầu |

## Chạy lại toàn bộ

```bash
pip install -r ../requirements.txt
./chay_tat_ca.sh
```
Windows: Git Bash hoặc WSL; hoặc trong thư mục `04-ma-nguon/` chạy lần lượt `python 01_hop_nhat_kiem_tra.py`, `02_mo_hinh.py`, `03_hieu_chinh_dia_phuong.py`, `04_mo_hinh_3d.py`.

## Dữ liệu – phân loại

- `03-du-lieu/1-du-lieu-tho/`, `2-da-xu-ly/`: 🟢 xanh – đã công bố (MIT).
- `02-de-xuat-thuyet-minh/bieu-mau-trung-tam/da-dien/`: 🟡 vàng – **không lên GitHub**.
- 🔴 Dữ liệu đỏ: không bao giờ đặt trong dự án.

## Trích dẫn dữ liệu

C-OLR (github.com/arashrockey/C-OLR, MIT) – số liệu gốc: Chico và cs. (2017), Pintos và cs. (2000), Lê Thị Hồng Liên và cs. (2007)… Xem `03-du-lieu/1-du-lieu-tho/c-olr/NGUON.md`.
