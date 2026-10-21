# DỮ LIỆU – DANH MỤC VÀ PHÂN LOẠI

Toàn bộ dữ liệu của repo nằm trong thư mục này, tách theo **nguồn gốc** và **mức độ được phép chia sẻ**.

| Thư mục | Nội dung | Thật / giả lập | Nhóm dữ liệu | Được đưa lên GitHub / AI trực tuyến? |
|---|---|---|---|---|
| `1-that-da-cong-bo/` | Số liệu đo thực địa đã công bố, kèm giấy phép và nguồn | **Thật** | 🟢 Xanh | Có |
| `2-gia-lap/` | Dữ liệu tạo có chủ đích để minh họa (có cài lỗi) | **Giả lập** | 🟢 Xanh | Có |
| `3-bieu-mau-trung-tam/trong/` | Biểu mẫu trống của Trung tâm | – | 🟢 Xanh | Có (sau khi Trung tâm đồng ý) |
| `3-bieu-mau-trung-tam/da-dien/` | Biểu mẫu đã điền nội dung thật | – | 🟡 Vàng | **Không** – bị chặn bởi `.gitignore` |
| `4-bo-sung/` | Chỗ thả dữ liệu mới cho chuỗi phân tích | Tùy tệp | Phân loại từng tệp trước khi thả | Chỉ tệp nhóm xanh |

> 🔴 **Dữ liệu đỏ** (bí mật nhà nước, quân sự, dữ liệu cá nhân nhạy cảm) **không bao giờ** được đặt trong repo này.
> Quy tắc xanh / vàng / đỏ: xem Mục 6 của `tai-lieu/thuyet-trinh/Ke-hoach-thuyet-trinh-v2.md` – cần bộ phận bảo mật xác nhận.

---

## 1. `1-that-da-cong-bo/` – dữ liệu thật đã công bố

### 1.1. `c-olr/` – 387 số đo ăn mòn khí quyển thép cacbon (dữ liệu gốc, chỉ đọc)

| Tệp | Mô tả |
|---|---|
| `C-OLR_datasets.xlsx` | 3 sheet: `training_dataset` (320: ISOCORRAG 190, MICAT 130), `testing_dataset` (67: Việt Nam 12, Nga 18, Tây Ban Nha 26, Colombia 11), `Read me` |
| `LICENSE.txt` | Giấy phép MIT của kho nguồn |
| `NGUON.md` | Nguồn gốc, trích dẫn, lưu ý chất lượng |

**Lưu ý quan trọng:** cột `WL` được từ điển dữ liệu của nguồn ghi là g/m², nhưng **thực chất là µm/năm** (99,5% khớp cột cấp ăn mòn nếu hiểu là µm/năm, chỉ 33,1% nếu là g/m²). Xem `ket-qua/nghien-cuu-an-mon/kiem_tra_chat_luong.csv`.

### 1.2. `demo-nhieu-nguon/` – bộ dữ liệu cho demo "tổng hợp nhiều nguồn" (Slide 8)

Sinh từ `c-olr/` bằng `ma-nguon/demo-nhieu-nguon/tao_bo_du_lieu.py` (trừ tệp 4 viết tay).

| Tệp | Nội dung | Đặc điểm cố ý |
|---|---|---|
| `nguon1_ISOCORRAG_MICAT_quoc_te.xlsx` | 320 trạm quốc tế | Giữ nguyên tiêu đề gốc, cột WL không ghi đơn vị |
| `nguon2_tram_Viet_Nam.csv` | 12 trạm Việt Nam | Tiêu đề tiếng Việt, có cột Vùng, ghi nguồn |
| `nguon3_tram_Nga.csv` | 18 trạm Nga | Tên cột tiếng Anh, cấu trúc khác |
| `nguon4_nguong_ISO_9223.md` | Ngưỡng cấp ăn mòn ISO 9223 (thép cacbon) | Văn bản |
| `ket_qua_mong_doi_bang_tong_hop.csv` | **Đáp án** để đối chiếu khi demo | – |

---

## 2. `2-gia-lap/` – dữ liệu giả lập (tình huống xuyên suốt, Phần III)

Sinh bằng `ma-nguon/demo-gia-lap/sinh_du_lieu_gia_lap.py` – hạt giống ngẫu nhiên cố định, chạy lại cho kết quả **giống hệt**.

| Tệp | Nội dung | Lỗi / bất hợp lý cài sẵn |
|---|---|---|
| `an_mon_tho.csv` | 253 dòng cân mẫu: 3 trạm × 4 kim loại × 7 mốc × 3 mẫu lặp + 1 dòng trùng | **14 lỗi**: trùng dòng, tên trạm không thống nhất, ô trống, số sai định dạng, ngày sai định dạng, khối lượng sau > trước, ngoại lệ gõ nhầm, ghi chú thực nghiệm |
| `khi_tuong_tram.csv` | 108 dòng khí tượng – môi trường theo tháng (T, RH, mưa, TOW, Cl⁻, SO₂) | 4 ô trống |
| `ke_hoach_cong_viec.csv` | 7 nội dung công việc, tiến độ, kinh phí (1.350 triệu đồng) | **3 bất hợp lý** về trình tự, độ phủ dữ liệu |

Giá trị "đúng" dùng khi sinh dữ liệu (để kiểm chứng mô hình khôi phục được): thép A = 560 / 310 / 160 g/m² (ven biển / đô thị / nội địa), n = 0,72.
**Trên slide luôn ghi "dữ liệu giả lập".**

---

## 3. `3-bieu-mau-trung-tam/` – biểu mẫu của Trung tâm

Xem `3-bieu-mau-trung-tam/README.md` – danh sách biểu mẫu cần cung cấp và cách đặt tên.

---

## 4. `4-bo-sung/` – dữ liệu bổ sung cho chuỗi phân tích ăn mòn

Thả tệp `.csv` theo mẫu `MAU_bo_sung.csv.template` → chạy `./chay_tat_ca.sh` → toàn bộ kết quả trong `ket-qua/nghien-cuu-an-mon/` cập nhật. Xem `4-bo-sung/README.md`.
