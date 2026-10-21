# ĐỀ XUẤT NHIỆM VỤ KHOA HỌC VÀ CÔNG NGHỆ – BẢN NHÁP

> **Trạng thái:** bản nháp nội dung, soạn với hỗ trợ của AI từ khoảng trống K1 (`../01-tong-quan-tai-lieu/KHOANG-TRONG-NGHIEN-CUU.md`) và kết quả dữ liệu thật (`../05-ket-qua/`).
> **Chưa theo biểu mẫu Trung tâm** – sẽ chuyển vào biểu mẫu khi có (`bieu-mau-trung-tam/trong/`). Mọi mục ghi **[CẦN BỔ SUNG]** do chủ nhiệm điền; AI không tự đặt số liệu kinh phí, nhân lực.
> **Phân loại dữ liệu:** bản nháp minh họa này = 🟢 xanh (chỉ dùng dữ liệu đã công bố). Bản đề xuất thật nộp Trung tâm = 🟡 vàng → lưu ở `bieu-mau-trung-tam/da-dien/` (không lên GitHub).

---

## 1. Tên nhiệm vụ

**Xây dựng hàm liều – đáp ứng hiệu chỉnh cho dự báo ăn mòn khí quyển của thép cacbon trong điều kiện khí hậu nhiệt đới Việt Nam**

## 2. Tính cấp thiết

- Tiêu chuẩn ISO 9223:2012 cung cấp hàm liều – đáp ứng để ước lượng tốc độ ăn mòn năm đầu từ số liệu môi trường; hàm này được xây dựng chủ yếu từ dữ liệu vùng ôn đới (T10).
- Kiểm định trên **387 số đo thực địa đã công bố** (ISOCORRAG, MICAT, Việt Nam, Nga…) cho thấy mô hình học từ dữ liệu quốc tế **dự đoán thấp hơn thực đo khoảng 31%** tại 12 trạm Việt Nam; chỉ 2/12 trạm được xếp đúng cấp ăn mòn (`../05-ket-qua/bang/hieu_chinh_dia_phuong.csv`).
- Kết quả độc lập ở quần đảo Canary (cận nhiệt đới) cũng kết luận hàm ISO 9223 ước lượng kém và cần bộ hằng số mới (T09).
- Ở Việt Nam, thời gian ẩm ướt (TOW) dài là yếu tố chi phối, đưa thép cacbon vào cấp C3 ngay cả khi clorua, SO₂ không cao (T01); số liệu trạm chủ yếu từ giai đoạn 1995–2005.
- Hệ quả: dùng nguyên hàm quốc tế có thể **đánh giá thấp mức ăn mòn** khi thiết kế bảo vệ công trình thép, trang thiết bị trong khí hậu nhiệt đới.

## 3. Mục tiêu

**Mục tiêu tổng quát:** Xây dựng và kiểm định hàm liều – đáp ứng dự báo tốc độ ăn mòn khí quyển của thép cacbon phù hợp khí hậu nhiệt đới Việt Nam.

**Mục tiêu cụ thể:**
1. Cập nhật bộ số liệu ăn mòn năm đầu và môi trường tại tối thiểu **[CẦN BỔ SUNG]** trạm đại diện các vùng khí hậu Việt Nam.
2. Xác định bộ hằng số (và biến bổ sung: độ ẩm tương đối, mưa, chu kỳ khô – ướt) của hàm liều – đáp ứng cho Việt Nam; sai số dự báo trung vị ≤ **[CẦN BỔ SUNG, gợi ý 20%]**, đúng cấp ISO ≥ **[CẦN BỔ SUNG]** số trạm kiểm định.
3. Ước lượng số mũ thời gian b (ISO 9224) cho thép cacbon trong khí hậu nhiệt đới.

## 4. Nội dung nghiên cứu

| ND | Nội dung | Gắn mục tiêu |
|---|---|---|
| 1 | Tổng quan, hợp nhất dữ liệu đã công bố (đã có nền: 387 số đo, 13 tài liệu) | 1 |
| 2 | Phơi mẫu thép cacbon tại các trạm, 7 mốc thu mẫu đến 36 tháng, 3 mẫu lặp | 1, 3 |
| 3 | Quan trắc môi trường: T, RH, mưa, TOW, Cl⁻, SO₂ | 1, 2 |
| 4 | Xây dựng, hiệu chỉnh hàm liều – đáp ứng; kiểm định độc lập (bỏ-một-trạm) | 2 |
| 5 | Xác định số mũ b; dự báo dài hạn; bản đồ cấp ăn mòn | 3 |
| 6 | Công bố, chuyển giao | 1–3 |

## 5. Phương pháp

- Phơi mẫu và đánh giá theo ISO 9223, ISO 9224 (và ISO 8565, ISO 8407 cho phơi mẫu, tẩy gỉ – **[CẦN BỔ SUNG: xác nhận tiêu chuẩn áp dụng]**).
- Hàm liều – đáp ứng dạng ISO 9223, ước lượng bằng hồi quy phi tuyến bền vững trên thang log; mô hình học máy có ràng buộc đơn điệu để đối chứng.
- Kiểm định: kiểm định chéo; kiểm định độc lập theo vùng; bỏ-một-trạm.
- Kiểm tra chất lượng dữ liệu tự động (độ lệch phân bố, ngoại lệ, rò rỉ giữa tập huấn luyện và kiểm định) – quy trình đã thử với Skill `exploratory-data-analysis` (`../05-ket-qua/kiem-tra-bang-skill/`).
- Toàn bộ mã và dữ liệu được lưu để tái lập (`../04-ma-nguon/`, `../chay_tat_ca.sh`).

## 6. Sản phẩm dự kiến

| Sản phẩm | Chỉ tiêu |
|---|---|
| Bộ dữ liệu ăn mòn – môi trường các trạm | [CẦN BỔ SUNG] trạm × 36 tháng; công bố mở phần được phép (FAIR, có DOI) |
| Hàm liều – đáp ứng hiệu chỉnh cho Việt Nam | Sai số, tỷ lệ đúng cấp theo mục tiêu 2 |
| Bản đồ cấp ăn mòn thép cacbon | [CẦN BỔ SUNG] |
| Bài báo | [CẦN BỔ SUNG]: Scopus / ВАК / trong nước (xem `../06-bai-bao/`) |
| Mã nguồn tái lập | Kho mã kèm hướng dẫn |

## 7. Thời gian, kinh phí, nhân lực

- Thời gian: **[CẦN BỔ SUNG]** (gợi ý 36 tháng để có chuỗi 3 năm).
- Kinh phí: **[CẦN BỔ SUNG]** – lập theo biểu mẫu dự toán của Trung tâm, căn cứ Thông tư 03/2023/TT-BTC và định mức của Bộ Quốc phòng; **đơn giá do cán bộ tài chính cung cấp**.
- Nhân lực, phối hợp: **[CẦN BỔ SUNG]**.

## 8. Kiểm tra logic (AI hỗ trợ – nhà khoa học xác nhận)

| Mục tiêu | Nội dung | Phương pháp | Sản phẩm | ⚠ |
|---|---|---|---|---|
| 1 | ND1, 2, 3 | Phơi mẫu, quan trắc | Bộ dữ liệu | Số trạm chưa xác định → chưa đánh giá được độ phủ vùng khí hậu |
| 2 | ND3, 4 | Hồi quy, kiểm định | Hàm hiệu chỉnh | Cần ≥ 2 trạm mỗi vùng để kiểm định bỏ-một-trạm có ý nghĩa |
| 3 | ND2, 5 | Hồi quy theo thời gian | Số mũ b, bản đồ | Chuỗi 36 tháng ngắn để ước lượng b dài hạn → nêu rõ giới hạn |
