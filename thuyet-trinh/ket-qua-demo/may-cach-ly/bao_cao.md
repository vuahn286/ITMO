# BÁO CÁO LỘ TRÌNH – Nhiệm vụ thử – DỮ LIỆU GIẢ LẬP

- Thời điểm chạy: 21/10/2026 21:04 · Máy: không Internet (công cụ không dùng mạng)
- Tệp dữ liệu: `luoi_dia_hinh_khi_hau.csv` · SHA-256: `03a049c1523795623a2b6e55fc6ef7aca6b2c3e6e04e7487b7960b3f0a324ee6`
- Cấu hình: `cau_hinh_mac_dinh.json` · SHA-256: `d001bdb169aec30cdc250dbdf9fe85de1a5e1ba99c7c64baac2b46b9bf137520`

## Kết quả

| Chỉ tiêu | Lộ trình tối ưu – chiều đi | Đường thẳng – chiều đi | Lộ trình tối ưu – chiều về |
|---|---|---|---|
| Quãng đường (km) | 14.5 | 13.6 | 14.5 |
| Thời gian bay (phút) | 12.5 | 11.3 | 22.9 |
| Năng lượng (Wh) | 240 | 250 | 422 |
| Số ô cấm bay đi qua | 0 | 8 | 0 |

Pin dùng được: 384 Wh (đã trừ dự trữ 20%).
- Chiều đi: **ĐỦ**, còn dư 144 Wh.
- Chiều về: **KHÔNG ĐỦ**, thiếu 38 Wh.
- Khứ hồi: **KHÔNG ĐỦ**, thiếu 278 Wh → cần điểm thay pin hoặc đổi nhiệm vụ.

## Ảnh hưởng của từng yếu tố trên lộ trình tối ưu – chiều đi

| Yếu tố | Năng lượng tăng thêm (Wh) | % tổng |
|---|---|---|
| Gió | -63.7 | -26.5% |
| Mưa | +0.6 | +0.2% |
| Mật độ không khí (nóng, ẩm, độ cao) | +10.2 | +4.3% |
| Leo cao theo địa hình | +20.6 | +8.6% |

Chiều về (ngược gió): gió làm tăng +118 Wh (+28% tổng chiều về).

*Mật độ không khí: so với khí quyển chuẩn mực nước biển 15 °C (ρ = 1,225 kg/m³).*

## Lưu ý

- Hệ số mưa, ngưỡng cấm bay, công suất bay là **tham số cấu hình** – đơn vị thay bằng số liệu thử nghiệm của thiết bị thật.
- Kết quả là ước lượng để lập kế hoạch; người có thẩm quyền quyết định.