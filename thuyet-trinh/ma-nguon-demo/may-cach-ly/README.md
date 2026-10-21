# CÔNG CỤ CHẠY TRÊN MÁY KHÔNG INTERNET – DEMO 3 (đề tài có dữ liệu mật)

**Ý tưởng:** AI **viết công cụ**, nhưng **không bao giờ thấy dữ liệu thật**.
Dùng AI trên máy có Internet để viết và thử công cụ với **dữ liệu giả**, kiểm tra mã, rồi chép **chỉ công cụ** sang máy không Internet. Dữ liệu mật chỉ được nạp vào công cụ trên máy đó.

```
 MÁY CÓ INTERNET (AI)                          │  MÁY KHÔNG INTERNET (dữ liệu 🔴)
 1. Mô tả cấu trúc dữ liệu (tên cột, đơn vị)    │
 2. AI viết công cụ + sinh dữ liệu giả + chạy thử│
 3. Nhà khoa học đọc lại, chạy kiem_tra_an_toan  │
 4. Đóng gói (dong_goi.sh) + mã băm SHA-256      │ ──── chuyển theo quy định của đơn vị ───▶
                                                 │  5. Đối chiếu mã băm → chạy với dữ liệu thật
                                                 │  6. Kết quả ở lại máy này; không mang ngược ra
```

## Tệp

| Tệp | Vai trò |
|---|---|
| `cong_cu_lo_trinh.py` | Công cụ: ước lượng lộ trình UAV tốn ít năng lượng nhất theo địa hình, gió, mưa, nhiệt độ, độ ẩm; tránh vùng cấm bay; kiểm tra pin chiều đi, chiều về, khứ hồi; tách ảnh hưởng từng yếu tố |
| `cau_hinh_mac_dinh.json` | Thông số thiết bị bay, ngưỡng cấm bay – **giả định**, thay bằng thông số thật trên máy không Internet |
| `sinh_du_lieu_gia.py` | Sinh dữ liệu GIẢ (địa hình 12 × 12 km, khí hậu nhiệt đới) → `../../du-lieu-demo/may-cach-ly/` |
| `kiem_tra_an_toan.py` | Quét mã: thư viện mạng, lệnh hệ thống, địa chỉ web → lập `MANIFEST.sha256`; `--doi-chieu` kiểm mã băm trên máy đích |
| `dong_goi.sh` | Tạo thư mục `goi-may-cach-ly/` để chép đi (thêm `--thu-vien` để kèm bộ cài numpy, matplotlib cho Windows) |

Thư viện: Python ≥ 3.9, `numpy`, `matplotlib` (không cần Internet khi chạy).

## Chạy thử với dữ liệu giả

```bash
python sinh_du_lieu_gia.py
python cong_cu_lo_trinh.py --du-lieu ../../du-lieu-demo/may-cach-ly/luoi_dia_hinh_khi_hau.csv \
       --nhiem-vu ../../du-lieu-demo/may-cach-ly/nhiem_vu_bay.json --ra ../../ket-qua-demo/may-cach-ly
```

Kết quả mong đợi (`../../ket-qua-demo/may-cach-ly/bao_cao.md`, `ban_do_lo_trinh.png`):
- Đường thẳng cắt qua 8 ô cấm bay (núi vượt trần bay, ổ mưa dông) → lộ trình tối ưu vòng qua đèo, 14,5 km, 240 Wh.
- Chiều đi xuôi gió mùa Tây Nam: gió **giảm** 64 Wh (−27%). Chiều về ngược gió: 422 Wh, gió **tăng** 118 Wh → **không đủ pin** (thiếu 38 Wh), khứ hồi thiếu 278 Wh.
- Thông điệp: cùng một tuyến, khí hậu (gió mùa) làm năng lượng chiều về gần **gấp 1,8 lần** chiều đi.

## Trên máy không Internet

1. Cài thư viện từ tệp `.whl` đi kèm: `python -m pip install --no-index --find-links . numpy matplotlib`
2. `python kiem_tra_an_toan.py --doi-chieu .` → phải báo **KHỚP**.
3. Chuyển dữ liệu thật sang đúng định dạng cột trong `cong_cu_lo_trinh.py`; sửa `cau_hinh_mac_dinh.json`.
4. Chạy `chay.bat` (Windows) hoặc lệnh `python cong_cu_lo_trinh.py …`.
5. Báo cáo ghi mã băm SHA-256 của tệp dữ liệu và cấu hình → truy vết được kết quả.

## Quy tắc

- Chỉ đưa cho AI **cấu trúc** dữ liệu – đặt tên cột chung chung, **không** đưa giá trị, tọa độ, tên khu vực, thông số thiết bị thật.
- Mọi việc chuyển tệp giữa hai máy theo **quy định bảo vệ bí mật nhà nước và quy chế của đơn vị** (thiết bị lưu trữ được cấp phép, kiểm tra mã độc, sổ theo dõi). Công cụ này không thay thế quy định đó.
- Khi cần sửa công cụ: sửa trên máy có Internet với dữ liệu giả → kiểm tra → đóng gói lại. Không mang lỗi kèm dữ liệu thật ra ngoài để hỏi AI – chỉ mô tả lỗi bằng lời hoặc tái tạo bằng dữ liệu giả.
- Mô hình năng lượng là mô hình đơn giản để minh họa; hệ số mưa, công suất, ngưỡng cấm bay cần hiệu chỉnh bằng thử nghiệm.
