# 05 – KẾT QUẢ

Toàn bộ thư mục **sinh lại được** bằng `../chay_tat_ca.sh` (trừ `kiem-tra-bang-skill/` – chạy bằng Skill bên ngoài, xem README trong đó).

| Thư mục / tệp | Nội dung | Sinh bởi |
|---|---|---|
| **bang/** | | |
| `danh_gia_mo_hinh.csv` | R², sai số, tỷ lệ đúng cấp ISO: kiểm định chéo 10 lần + kiểm định độc lập (tất cả, Việt Nam, Nga) | 02 |
| `du_doan_kiem_dinh.csv` | Đo – dự đoán cho 67 trạm kiểm định độc lập | 02 |
| `muc_do_quan_trong_bien.csv` | Mức độ quan trọng của biến (hoán vị) | 02 |
| `hieu_chinh_dia_phuong.csv` | Sai lệch trước / sau hiệu chỉnh vùng (bỏ-một-trạm) | 03 |
| `du_doan_hieu_chinh_VN_RU.csv` | Dự đoán đã hiệu chỉnh cho 12 trạm Việt Nam, 18 trạm Nga | 03 |
| `be_mat_theo_thoi_gian.csv` | Chiều dày ăn mòn trung bình, sâu nhất theo thời gian (Nha Trang, Hà Nội) | 04 |
| **hinh/** `do_vs_du_doan.png` | Biểu đồ đo – dự đoán (thang log, ngưỡng cấp ISO) | 02 |
| **mo-hinh/** `he_so_DRF.json` | Hệ số hàm liều – đáp ứng | 02 |
| **mo-hinh/** `mo_hinh.pkl` | Mô hình đã huấn luyện (không lên GitHub – sinh lại khi chạy) | 02 |
| **mo-hinh-3d/** | 3D-1 mặt đáp ứng; 3D-2 diễn tiến theo thời gian; 3D-3 bề mặt tấm thép (HTML tương tác + PNG cho slide) | 04 |
| **mo-hinh-3d/** (tiếp) | **3D-4 quá trình ăn mòn hoạt hình** (`3D_4_qua_trinh_an_mon_dong.html`, nút ▶ Chạy; PNG 4 thời điểm + mặt cắt); **3D-5 so sánh 4 kim loại** cấp C3; bảng `bang/qua_trinh_an_mon_Nha_Trang.csv`, `bang/so_sanh_vat_lieu_C3.csv` | 05 |
| **kiem-tra-bang-skill/** | Kiểm tra dữ liệu bằng Skill `exploratory-data-analysis` (K-Dense) | Skill bên ngoài |

## Kết quả chính

| Chỉ số | Giá trị |
|---|---|
| Kiểm định chéo (320 trạm): R² trên thang log | 0,61 (hàm liều – đáp ứng) · 0,71 (gradient boosting) |
| Kiểm định độc lập (67 trạm): lệch ≤ 1 cấp ISO | 97–99% |
| Mức độ quan trọng của biến | log Cl⁻ 0,57 > log SO₂ 0,53 > TOW 0,38 > nhiệt độ (≈ 0) |
| Việt Nam (12 trạm): sai lệch của mô hình quốc tế | **thấp hơn thực đo ~31%**; hệ số vùng k = 1,46 |
| Việt Nam sau hiệu chỉnh (bỏ-một-trạm) | sai số trung vị 26,8% → **18,6%**; đúng cấp 2/12 → **9/12** |
| Nga (18 trạm) | mô hình quốc tế **cao hơn thực đo ~80%**; sai số trung vị 85,9% → 32,0% sau hiệu chỉnh |
| Dự báo 10 năm, khí hậu Việt Nam (ISO 9224, b = 0,523) | Hà Nội ~94 µm · Đồ Sơn ~149 µm |

Các tệp HTML 3D dùng `mo-hinh-3d/plotly.min.js` cùng thư mục → **mở được không cần Internet** (chép cả thư mục khi mang đi trình chiếu).

⚠ **3D-3:** độ sâu trung bình là định lượng (số đo năm đầu + ISO 9224); độ nhám, hố cục bộ là **minh họa với tham số giả định** – không dùng để kết luận.
⚠ **3D-4:** tương tự 3D-3 – lớp gỉ dày 3 × thép đã mất và hố sâu 3 × trung bình là **giả định** (`mo-hinh-3d/tham_so_3D_4.json`). **3D-5:** tốc độ theo khoảng cấp C3 của ISO 9223 Bảng 2 (đã đối chiếu C1–C3), số mũ b theo ISO 9224 – so sánh xu hướng, không phải số đo cùng trạm; nhôm ăn mòn chủ yếu cục bộ nên chiều dày trung bình đánh giá thấp mức hư hại.
