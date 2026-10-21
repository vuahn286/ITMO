# DỮ LIỆU BỔ SUNG CHO CHUỖI PHÂN TÍCH ĂN MÒN

Mục đích: mở rộng bộ 387 số đo lên hàng trăm – hàng nghìn số đo (ví dụ: số liệu trạm thử nghiệm của Trung tâm, bảng số liệu gốc của Lê Thị Hồng Liên và cs. 2007, dữ liệu đầy đủ của Chico và cs. 2017).

## Cách dùng

1. Sao chép `MAU_bo_sung.csv.template` thành một tệp `.csv` mới (ví dụ `tram-trung-tam-2020-2025.csv`).
2. Điền theo đúng các cột:

| Cột | Ý nghĩa | Đơn vị |
|---|---|---|
| `nguon` | Nhóm nguồn (ví dụ: TTNĐ Việt-Nga) | – |
| `tram` | Tên trạm | – |
| `loai_khi_quyen` | 1 nông thôn · 2 đô thị · 3 công nghiệp · 4 biển (suy ra từ các trạm trong bộ C-OLR: El Escorial = 1, Madrid = 2, Bilbao = 3, Alicante = 4) | – |
| `T_C` | Nhiệt độ trung bình năm | °C |
| `TOW_h_nam` | Thời gian ẩm ướt | giờ/năm |
| `Cl_mg_m2_ngay`, `SO2_mg_m2_ngay` | Tốc độ lắng đọng | mg/m²/ngày |
| `r_corr_um_nam` | Tốc độ ăn mòn năm đầu của thép cacbon | **µm/năm** |
| `tai_lieu` | Trích dẫn công bố / nguồn số liệu | – |
| `quoc_gia` | Quốc gia (ghi "Việt Nam" để được tính vào hiệu chỉnh vùng Việt Nam) | – |

3. Chạy `./chay_tat_ca.sh` ở gốc repo. Dữ liệu bổ sung được xếp vào **tập kiểm định độc lập**.

> Chỉ thả tệp **nhóm xanh** (đã công bố hoặc được phép công khai). Dữ liệu nhóm vàng: xử lý trên máy nội bộ, không đưa lên GitHub.
