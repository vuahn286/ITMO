# AI Agent trong nghiên cứu khoa học – bài thuyết trình và dự án nghiên cứu minh họa

Repo gồm **hai phần**:

| Thư mục | Là gì | Bắt đầu từ |
|---|---|---|
| **`du-an-nghien-cuu/`** | **Dự án nghiên cứu thật** – *Khả năng áp dụng mô hình ăn mòn khí quyển quốc tế cho khí hậu nhiệt đới Việt Nam* – dữ liệu thật đã công bố (387 số đo), cấu trúc theo vòng đời nhiệm vụ: tài liệu → đề xuất → dữ liệu → mã → kết quả → bài báo → báo cáo | `du-an-nghien-cuu/README.md` |
| **`thuyet-trinh/`** | Bài thuyết trình *"AI Agent và sự chuyển đổi phương thức nghiên cứu khoa học"* (120 phút, Trung tâm Nhiệt đới Việt – Nga): danh sách slide, kế hoạch, câu lệnh demo, dữ liệu demo | `thuyet-trinh/README.md` |

```
du-an-nghien-cuu/
├── 00-quan-ly-du-an/        kế hoạch · nhật ký thực hiện · việc còn lại
├── 01-tong-quan-tai-lieu/   13 tài liệu đã xác minh (.csv, .bib) · ma trận bằng chứng · khoảng trống
├── 02-de-xuat-thuyet-minh/  bản nháp đề xuất · bieu-mau-trung-tam/ (trong/ ← CHỜ CUNG CẤP; da-dien/ 🟡 không lên GitHub)
├── 03-du-lieu/              1-du-lieu-tho/ (chỉ đọc) · 2-da-xu-ly/ · 3-bo-sung/ · README (từ điển dữ liệu, FAIR)
├── 04-ma-nguon/             01 hợp nhất – kiểm tra → 02 mô hình → 03 hiệu chỉnh vùng → 04, 05 mô hình 3D
├── 05-ket-qua/              bang/ · hinh/ · mo-hinh/ · mo-hinh-3d/ (HTML tương tác) · kiem-tra-bang-skill/
├── 06-bai-bao/              bản thảo bài báo (tóm tắt Việt – Anh)
├── 07-bao-cao/              báo cáo tổng hợp
└── chay_tat_ca.sh
thuyet-trinh/
├── DANH-SACH-SLIDE.md (+ .docx)   bố cục slide chính thức v2.5 (24 slide, 3 demo)
├── cau-lenh-demo.md · Ke-hoach-thuyet-trinh-v2.md · DE-XUAT-BO-SUNG-v2.4 · RA-SOAT-v2 · luu-tru/
├── du-lieu-demo/ (nhieu-nguon/ thật · gia-lap/ · may-cach-ly/) · ma-nguon-demo/ · ket-qua-demo/
└── chay_demo.sh
```

## Chạy lại

```bash
pip install -r requirements.txt
./du-an-nghien-cuu/chay_tat_ca.sh   # dự án nghiên cứu
./thuyet-trinh/chay_demo.sh         # dữ liệu, kết quả demo
```
Windows: Git Bash hoặc WSL, hoặc gọi lần lượt các lệnh `python` trong hai script.

## Kết quả chính của dự án

- Phát hiện **lỗi đơn vị** trong bộ dữ liệu đã công bố (ghi g/m², thực tế µm/năm) và 2 trạm ghi sai cấp.
- Mô hình quốc tế **dự đoán thấp hơn thực đo ~31%** ở Việt Nam, cao hơn ~80% ở Viễn Đông Nga.
- Hiệu chỉnh vùng: đúng cấp ăn mòn **9/12 trạm Việt Nam** (trước 2/12).
- Mô hình 3D hoạt hình quá trình ăn mòn (kim loại mất, lớp gỉ, hố) và so sánh thép – kẽm – đồng – nhôm.
- Kiểm tra bằng Skill khoa học mở (K-Dense): bổ sung 3 kiểm tra mà phân tích ban đầu bỏ qua.

## Dữ liệu và giấy phép

- Dữ liệu: C-OLR (github.com/arashrockey/C-OLR, MIT) – nguồn gốc ở `du-an-nghien-cuu/03-du-lieu/1-du-lieu-tho/c-olr/NGUON.md`.
- Skill: K-Dense Scientific Agent Skills (MIT) – chỉ chạy, không sao chép vào repo; Kassis và cs. (2026), arXiv:2609.00065.
- 🟢 xanh: lên GitHub và AI trực tuyến · 🟡 vàng: chỉ nội bộ, **không lên GitHub** · 🔴 đỏ: **không bao giờ** đặt trong repo.
