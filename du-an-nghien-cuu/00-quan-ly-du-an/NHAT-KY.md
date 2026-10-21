# NHẬT KÝ THỰC HIỆN

Ghi lại các bước thật đã làm (có AI Agent hỗ trợ), kể cả các lần sai và sửa – phục vụ minh bạch và tái lập.

| Ngày | Bước | Kết quả / quyết định |
|---|---|---|
| 20/10/2026 | Tìm dữ liệu đo thực địa về ăn mòn khí quyển có thể truy cập | Môi trường làm việc chỉ truy cập được GitHub; tìm được bộ C-OLR (387 số đo, MIT). Các kho khác là dữ liệu nước biển / phòng thí nghiệm / giả lập → **không trộn vào** |
| 20/10/2026 | Hợp nhất dữ liệu, kiểm tra chất lượng | **Phát hiện lỗi đơn vị**: cột WL ghi g/m² nhưng thực chất µm/năm (99,5% so với 33,1% khớp cột cấp ăn mòn). 2 trạm ghi sai cấp |
| 20/10/2026 | Xây dựng mô hình (DRF, gradient boosting), kiểm định độc lập | Mô hình quốc tế dự đoán thấp ~31% ở Việt Nam, cao ~80% ở Nga |
| 20/10/2026 | Hiệu chỉnh vùng, kiểm định bỏ-một-trạm | Việt Nam: đúng cấp 2/12 → 9/12 |
| 20/10/2026 | Mô hình 3D | Mặt 3D ban đầu dùng gradient boosting bị "bậc thang", vượt khung → **đổi sang DRF hiệu chỉnh vùng** (trơn, có ý nghĩa vật lý). Bề mặt tấm thép ban đầu dùng tốc độ dự đoán → **đổi sang số đo năm đầu** (Nha Trang dự đoán 21,6 so với đo 40,6 µm) |
| 20/10/2026 | (Demo giả lập) phát hiện ngoại lệ | Lần đầu dùng z-score/MAD với 3 mẫu lặp → đánh dấu nhầm 20 giá trị, bỏ sót lỗi thật → **đổi quy tắc "lệch > 30% so với 2 mẫu lặp"** |
| 21/10/2026 | Kiểm tra dữ liệu bằng Skill `exploratory-data-analysis` (K-Dense, MIT) | Độ lệch 4,66 → −0,02 sau log; 31/387 ngoài ngưỡng IQR; không rò rỉ giữa hai tập – bổ sung 3 kiểm tra mà phân tích ban đầu bỏ qua |
| 21/10/2026 | Tổng quan tài liệu | 13 tài liệu xác minh tồn tại (tóm tắt / trang tạp chí); tìm thêm bằng chứng độc lập Santana và cs. 2019 (Canary) |
| 21/10/2026 | Soạn đề xuất, bản thảo bài báo, báo cáo | Bản nháp – chờ chủ nhiệm duyệt, chờ biểu mẫu Trung tâm |
