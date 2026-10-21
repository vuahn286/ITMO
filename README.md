# AI Agent và sự chuyển đổi phương thức nghiên cứu khoa học

Tài liệu, dữ liệu và mã nguồn cho bài thuyết trình **"AI Agent và sự chuyển đổi phương thức nghiên cứu khoa học"** (120 phút) dành cho cán bộ, nhà khoa học **Trung tâm Nhiệt đới Việt – Nga**, kèm một nghiên cứu minh họa với dữ liệu thật: **ăn mòn khí quyển của thép cacbon**.

> Phiên bản bố cục slide: **v2.4** (21/10/2026) – 22 slide trình bày + 4 phụ lục.
> **Đang chờ:** biểu mẫu của Trung tâm → `du-lieu/3-bieu-mau-trung-tam/` (xem README trong thư mục đó).

---

## Bắt đầu từ đâu?

| Bạn cần | Mở tệp |
|---|---|
| Duyệt, sửa nội dung từng slide | `tai-lieu/thuyet-trinh/DANH-SACH-SLIDE.md` (bản Word: `DANH-SACH-SLIDE-v2.4.docx`) – **bố cục chính thức** |
| Câu lệnh để sao chép vào Claude khi demo | `tai-lieu/thuyet-trinh/cau-lenh-demo.md` |
| Kế hoạch đầy đủ, bảng căn cứ – nguồn số liệu | `tai-lieu/thuyet-trinh/Ke-hoach-thuyet-trinh-v2.md` (Mục 7) |
| Đề xuất bổ sung theo góp ý gần nhất | `tai-lieu/thuyet-trinh/DE-XUAT-BO-SUNG-v2.4.md` |
| Báo cáo nghiên cứu ăn mòn (dữ liệu thật, mô hình, 3D) | `tai-lieu/bao-cao/BAO-CAO-nghien-cuu-an-mon.md` |
| Danh mục dữ liệu, phân loại xanh / vàng / đỏ | `du-lieu/README.md` |

---

## Cấu trúc repo

```
├── du-lieu/                          ← TOÀN BỘ dữ liệu, tách riêng và phân loại (xem du-lieu/README.md)
│   ├── 1-that-da-cong-bo/            🟢 dữ liệu thật đã công bố
│   │   ├── c-olr/                       387 số đo ăn mòn thép (ISOCORRAG, MICAT, Việt Nam, Nga…) + giấy phép + nguồn
│   │   └── demo-nhieu-nguon/            4 tệp, 3 nguồn – demo "tổng hợp nhiều nguồn" (Slide 8) + đáp án
│   ├── 2-gia-lap/                    🟢 dữ liệu giả lập có cài lỗi – tình huống xuyên suốt (Phần III)
│   ├── 3-bieu-mau-trung-tam/         biểu mẫu Trung tâm
│   │   ├── trong/                    🟢 biểu mẫu trống  ← CHỜ CUNG CẤP
│   │   └── da-dien/                  🟡 biểu mẫu đã điền – KHÔNG lên GitHub (.gitignore)
│   └── 4-bo-sung/                    chỗ thả dữ liệu mới cho nghiên cứu ăn mòn (theo tệp mẫu)
│
├── ma-nguon/
│   ├── demo-gia-lap/                 sinh dữ liệu giả lập · phân tích mẫu · sơ đồ Gantt
│   ├── demo-nhieu-nguon/             tạo bộ dữ liệu demo Slide 8 từ c-olr
│   └── nghien-cuu-an-mon/            01 hợp nhất – kiểm tra → 02 mô hình → 03 hiệu chỉnh vùng → 04 mô hình 3D
│
├── ket-qua/                          ← sinh lại được hoàn toàn bằng chay_tat_ca.sh
│   ├── demo-gia-lap/                 báo cáo chất lượng dữ liệu, mô hình C = A·tⁿ, biểu đồ, Gantt
│   └── nghien-cuu-an-mon/            bảng, biểu đồ, mô hình 3D (HTML tương tác), skill-eda/ (thí nghiệm Skill)
│
├── tai-lieu/
│   ├── thuyet-trinh/                 danh sách slide, kế hoạch, câu lệnh demo, rà soát, đề xuất
│   ├── bao-cao/                      báo cáo nghiên cứu ăn mòn
│   └── luu-tru/                      kế hoạch v1 (bản gốc ban đầu)
│
├── chay_tat_ca.sh                    chạy lại toàn bộ
├── requirements.txt
└── .gitignore
```

---

## Chạy lại toàn bộ

```bash
pip install -r requirements.txt
./chay_tat_ca.sh
```

Trên Windows: chạy trong Git Bash hoặc WSL, hoặc gọi lần lượt các lệnh `python` trong `chay_tat_ca.sh`.

- Dữ liệu giả lập sinh lại **giống hệt từng byte** (hạt giống ngẫu nhiên cố định).
- Thêm dữ liệu thật vào `du-lieu/4-bo-sung/` rồi chạy lại → mọi bảng, biểu đồ, mô hình 3D trong `ket-qua/nghien-cuu-an-mon/` tự cập nhật.

---

## Kết quả chính của nghiên cứu ăn mòn (dữ liệu thật)

- Phát hiện **lỗi đơn vị trong bộ dữ liệu đã công bố** (ghi g/m², thực tế µm/năm) và 2 trạm ghi sai cấp ăn mòn.
- Mô hình học từ dữ liệu quốc tế **dự đoán thấp hơn thực đo ở Việt Nam ~31%**, cao hơn ở Viễn Đông Nga ~80% → cần hiệu chỉnh cho khí hậu nhiệt đới.
- Sau hiệu chỉnh vùng (kiểm định bỏ-một-trạm): đúng cấp ăn mòn ở **9/12 trạm Việt Nam** (trước là 2/12).
- Thí nghiệm Skill `exploratory-data-analysis` (K-Dense, MIT): bổ sung 3 kiểm tra mà phân tích ban đầu bỏ qua – xem `ket-qua/nghien-cuu-an-mon/skill-eda/README.md`.

Chi tiết và hạn chế: `tai-lieu/bao-cao/BAO-CAO-nghien-cuu-an-mon.md`.

---

## Nguồn dữ liệu và giấy phép

- **C-OLR** (https://github.com/arashrockey/C-OLR) – giấy phép MIT; số liệu gốc từ Chico và cs. (2017), Pintos và cs. (2000), Lê Thị Hồng Liên và cs. (2007) và các công bố khác – xem `du-lieu/1-that-da-cong-bo/c-olr/NGUON.md`.
- **K-Dense Scientific Agent Skills** (https://github.com/K-Dense-AI/claude-scientific-skills) – giấy phép MIT; chỉ dùng để chạy thí nghiệm, không sao chép mã vào repo. Trích dẫn: Kassis và cs. (2026), arXiv:2609.00065.
- Dữ liệu giả lập, mã nguồn và tài liệu trong repo: do nhóm soạn bài thuyết trình xây dựng.

## Quy tắc dữ liệu

🟢 xanh – được đưa lên GitHub và công cụ AI trực tuyến · 🟡 vàng – chỉ xử lý nội bộ / gói AI tổ chức, **không lên GitHub** · 🔴 đỏ – **không bao giờ** đặt trong repo.
