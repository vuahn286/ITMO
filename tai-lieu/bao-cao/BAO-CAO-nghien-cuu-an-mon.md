# BÁO CÁO NGHIÊN CỨU: ĂN MÒN KHÍ QUYỂN CỦA THÉP CACBON – PHÂN TÍCH DỮ LIỆU ĐO THỰC ĐỊA, MÔ HÌNH DỰ BÁO VÀ MÔ HÌNH 3D

**Phiên bản:** 1.1 – 21/10/2026 (thêm tóm tắt dễ hiểu và giải nghĩa thuật ngữ)
**Phạm vi:** thép cacbon, tốc độ ăn mòn năm đầu, 387 quan sát đo thực địa từ các chương trình quốc tế và các công bố độc lập, trong đó có 12 trạm ở Việt Nam và 18 trạm ở Nga.
**Tính chất dữ liệu:** 100% là **số đo thực địa đã công bố**. Không có số liệu giả lập trong phân tích định lượng. Riêng phần độ nhám bề mặt ở mô hình 3D-3 là minh họa có tham số giả định, được ghi rõ.

> **Lưu ý về quy mô:** yêu cầu ban đầu là "vài nghìn mẫu". Môi trường làm việc hiện chỉ truy cập được GitHub, còn Zenodo, Mendeley Data, Figshare, Kaggle, các tạp chí… đều bị chặn. Trên GitHub, nguồn dữ liệu đo thực địa về ăn mòn khí quyển duy nhất tìm được là bộ C-OLR (387 quan sát). Các kho khác là dữ liệu ăn mòn trong nước biển, ống dẫn, phòng thí nghiệm hoặc dữ liệu giả lập, nên **không được trộn vào**. Mục 7 nêu cách mở rộng lên hàng nghìn mẫu; chuỗi xử lý đã sẵn sàng nhận thêm dữ liệu.

## Tóm tắt dễ hiểu (đọc trong 1 phút)

1. Tổng hợp **387 lần đo thật** về mức gỉ của thép cacbon sau 1 năm để ngoài trời, ở nhiều nước, trong đó có 12 trạm ở Việt Nam và 18 trạm ở Nga.
2. Phát hiện **một lỗi trong bộ dữ liệu đã công bố**: đơn vị được ghi là g/m², nhưng thực chất là µm/năm (micromet chiều dày mất đi mỗi năm).
3. Xây dựng mô hình dự đoán mức gỉ từ 4 yếu tố môi trường: **muối biển (clorua)**, **khí SO₂**, **số giờ bề mặt bị ẩm** và **nhiệt độ**. Muối biển và SO₂ ảnh hưởng mạnh nhất.
4. **Kết quả quan trọng nhất:** mô hình học từ dữ liệu quốc tế **dự đoán thấp hơn thực tế khoảng 31% ở Việt Nam**, và cao hơn thực tế khoảng 80% ở vùng lạnh của Nga. Muốn dự báo đúng cho Việt Nam phải hiệu chỉnh bằng số liệu trong nước; sau hiệu chỉnh, mô hình xếp đúng cấp ăn mòn ở 9/12 trạm Việt Nam (trước đó là 2/12).
5. Mô hình 3D cho thấy: tấm thép cacbon không sơn ở Nha Trang mất trung bình khoảng **0,14 mm sau 10 năm** và **0,19 mm sau 20 năm**; ở Hà Nội khoảng 0,11 mm và 0,15 mm.

**Giải nghĩa thuật ngữ dùng trong báo cáo:**

| Thuật ngữ | Ý nghĩa |
|---|---|
| r_corr, tốc độ ăn mòn năm đầu | Chiều dày kim loại mất đi trong năm đầu tiên để ngoài trời (µm/năm) |
| TOW | Thời gian ẩm ướt – số giờ trong năm bề mặt kim loại bị ẩm |
| Cl⁻, SO₂ | Lượng muối (clorua) và khí lưu huỳnh đioxit lắng đọng lên bề mặt mỗi ngày |
| C1–CX | Cấp ăn mòn theo ISO 9223, từ rất thấp (C1) đến cực cao (CX) |
| DRF (hàm liều – đáp ứng) | Công thức tính mức gỉ từ các yếu tố môi trường, dạng giống công thức của ISO 9223 |
| GBM (gradient boosting) | Một mô hình học máy; ở đây bị ràng buộc để mức gỉ chỉ tăng khi muối, SO₂, độ ẩm tăng |
| R² | Mô hình giải thích được bao nhiêu phần sự khác nhau giữa các trạm (1 = hoàn toàn, 0 = không) |
| Kiểm định chéo / kiểm định độc lập | Thử mô hình trên dữ liệu nó chưa từng thấy khi học |
| Bỏ-một-trạm (LOO) | Dự đoán từng trạm mà không dùng số đo của chính trạm đó, để đánh giá trung thực |
| Hệ số hiệu chỉnh vùng k | Hệ số nhân để đưa mô hình quốc tế về đúng mức của một vùng khí hậu |

---

## 1. Câu hỏi nghiên cứu

1. Các yếu tố môi trường (clorua, SO₂, thời gian ẩm ướt TOW, nhiệt độ) giải thích được bao nhiêu phần biến thiên của tốc độ ăn mòn năm đầu của thép cacbon trên phạm vi toàn cầu?
2. Mô hình học từ các chương trình quốc tế (ISOCORRAG, MICAT) có áp dụng được **nguyên trạng** cho Việt Nam và Viễn Đông Nga không?
3. Quá trình ăn mòn diễn tiến thế nào theo **môi trường** và theo **thời gian** (biểu diễn 3D)?

## 2. Dữ liệu

| Tập | Nguồn | Số quan sát | Ghi chú |
|---|---|---|---|
| Huấn luyện | ISOCORRAG – Chico et al. (2017) | 190 | Nhiều nước |
| Huấn luyện | MICAT – Pintos et al. (2000) | 130 | Ibero-America |
| Kiểm định độc lập | Việt Nam – "Lien et al." [¹] | 12 | Việt Trì, Sơn Tây, Đồ Sơn, Hải Dương, Hà Nội, Thanh Hóa, Đồng Hới, Huế, Đà Nẵng, Nha Trang, TP.HCM, Vũng Tàu |
| Kiểm định độc lập | Nga (Viễn Đông, Murmansk) – "Mikhailov et al." [²] | 18 | Murmansk, Vladivostok, Okhotsk, Kamchatka… |
| Kiểm định độc lập | Tây Ban Nha, quần đảo Canary, Colombia | 37 | de la Fuente, Morales, Castaño, Santa et al. |
| **Tổng** | | **387** | |

**Truy xuất nguồn:** kho GitHub [arashrockey/C-OLR](https://github.com/arashrockey/C-OLR) (giấy phép MIT), commit `107ffa4`, tệp `datasets.xlsx`. Bản sao đặt tại `du-lieu/1-that-da-cong-bo/c-olr/`.

[¹] Nhiều khả năng là: Le Thi Hong Lien, Pham Thy San, Hoang Lam Hong (2007). *Results of studying atmospheric corrosion in Vietnam 1995–2005*. Science and Technology of Advanced Materials 8(7–8), 552–558. Kết luận của bài báo ("TOW ở Việt Nam đủ dài để đưa thép cacbon vào cấp C3") khớp với dữ liệu: 11/12 trạm thuộc C3. **Cần đối chiếu bảng số liệu gốc.**
[²] Chưa xác định chắc chắn công bố gốc. Có thể thuộc chương trình thử nghiệm Viễn Đông của Liên Xô/Nga (nhóm Mikhailovsky, Panchenko và cộng sự). **Cần xác minh.**

**Biến số:** T (°C), TOW (h/năm), Cl⁻ và SO₂ (tốc độ lắng đọng, mg/m²·ngày), r_corr (µm/năm).

## 3. Kiểm tra chất lượng dữ liệu – các phát hiện

| # | Phát hiện | Xử lý |
|---|---|---|
| 1 | **Lỗi đơn vị trong từ điển dữ liệu của nguồn:** cột WL được ghi là g/m², nhưng nếu hiểu là µm/năm thì 99,5% quan sát khớp cột cấp ăn mòn; nếu là g/m² chỉ 33,1% khớp | WL là **µm/năm**; quy đổi sang g/m² với 7,86 g/cm³ |
| 2 | 2 trạm ghi sai cấp ăn mòn: Barcelona 49,9 µm (nguồn ghi C4, đúng là C3); El Hierro 263,2 µm (nguồn ghi C5, đúng là CX) | Dùng cấp tính lại theo ngưỡng ISO 9223; giữ cột gốc |
| 3 | 2 trạm có TOW rất thấp (PE41, PE42 < 300 h/năm) | Giữ lại, đánh dấu |
| 4 | 4 quan sát có Cl⁻ hoặc SO₂ = 0 | Thay bằng 0,1 khi lấy logarit |
| 5 | Murmansk, Vladivostok mỗi trạm có 2 quan sát | Giữ – các đợt phơi mẫu khác nhau |

*Tệp:* `ket-qua/nghien-cuu-an-mon/kiem_tra_chat_luong.csv`. Phát hiện số 1 là một ví dụ điển hình: lỗi trong nguồn công bố chỉ lộ ra khi đối chiếu chéo các cột.

## 4. Phương pháp

- **M1 – Hàm liều – đáp ứng (DRF)** cùng dạng với ISO 9223:2012, hiệu chỉnh lại trên dữ liệu. Dữ liệu có TOW thay cho RH nên không dùng nguyên văn hệ số ISO.
  `r = a·SO₂^b·exp(c·τ + f(T)) + d·Cl^e·exp(g·τ + h·T)`, τ = TOW/1000, f(T) tuyến tính từng đoạn quanh 10 °C. Ước lượng bằng bình phương tối thiểu bền vững trên log r.
- **M2 – Gradient boosting có ràng buộc đơn điệu:** r chỉ được phép tăng theo Cl⁻, SO₂ và TOW, để giữ quan hệ vật lý.
- **Kiểm định:** kiểm định chéo 10 lần trên tập huấn luyện, và kiểm định **độc lập** trên 67 quan sát không dùng khi huấn luyện.
- **Hiệu chỉnh vùng:** nhân với hệ số k là trung bình hình học của tỉ số đo/dự đoán của các trạm cùng vùng. Kiểm định bằng phương pháp **bỏ-một-trạm (LOO)**: mỗi trạm được dự đoán mà không dùng số đo của chính nó.
- **Diễn tiến theo thời gian:** ISO 9224:2012, `D = r·t^b` với b = 0,523 (B1, thép cacbon) khi t ≤ 20 năm; sau 20 năm tuyến tính.

*Mã nguồn tái lập:* `ma-nguon/nghien-cuu-an-mon/01…04_*.py`.

## 5. Kết quả

### 5.1. Mô hình toàn cầu

| Mô hình | Tập | R² (log) | Sai số tương đối trung vị | Đúng cấp ISO | Lệch ≤ 1 cấp |
|---|---|---|---|---|---|
| M1 DRF | CV 10 lần (320) | 0,61 | 27% | 63% | 98% |
| M2 GBM | CV 10 lần (320) | 0,71 | 23% | 68% | 98% |
| M1 DRF | Kiểm định độc lập (67) | 0,44 | 34% | 55% | 99% |
| M2 GBM | Kiểm định độc lập (67) | 0,39 | 31% | 60% | 97% |

**Mức độ quan trọng của biến** (mức giảm R² khi xáo trộn biến): log Cl⁻ 0,57 > log SO₂ 0,53 > TOW 0,38 > nhiệt độ (≈ 0).
**Hệ số DRF:** số mũ của Cl⁻ e = 0,88, của SO₂ b = 0,46. Cùng bậc với dạng hàm ISO 9223 (0,62 và 0,52).

Hình: `ket-qua/nghien-cuu-an-mon/do_vs_du_doan.png`.

### 5.2. Phát hiện chính: mô hình toàn cầu sai lệch có hệ thống theo vùng khí hậu

| Vùng | Sai lệch của mô hình toàn cầu | Hệ số vùng k | Sai số trung vị: trước → sau hiệu chỉnh (LOO) | Đúng cấp ISO: trước → sau |
|---|---|---|---|---|
| **Việt Nam** (12 trạm) | **dự đoán thấp hơn thực đo 31%**; 11/12 trạm bị dự đoán thấp | 1,46 | 26,8% → **18,6%** | 17% → **75%** |
| **Viễn Đông Nga** (18 trạm) | **dự đoán cao hơn thực đo 80%** | 0,56 | 85,9% → **32,0%** | 78% → **83%** |

*(Mô hình trung bình hình học M1 và M2. Tệp: `ket-qua/nghien-cuu-an-mon/hieu_chinh_dia_phuong.csv`, `ket-qua/nghien-cuu-an-mon/du_doan_hieu_chinh_VN_RU.csv`.)*

**Diễn giải đề xuất (cần nhà khoa học xác nhận):**
- **Việt Nam:** thép ăn mòn **nhanh hơn** mức các yếu tố Cl⁻, SO₂, TOW dự báo. Các trạm có Cl⁻ thấp nhưng ăn mòn cao (Huế: Cl⁻ 1,3, r = 31,5 µm; Nha Trang: Cl⁻ 13,8, r = 40,6 µm) gợi ý vai trò của các yếu tố mà bộ biến chưa nắm được: độ ẩm tương đối liên tục, mưa, thời gian khô – ướt luân phiên, hoặc khác biệt về cách đo TOW và Cl⁻ giữa các chương trình.
- **Viễn Đông Nga:** nhiệt độ trung bình −13 đến 5 °C, phần lớn nằm **ngoài miền dữ liệu huấn luyện**. Mô hình ngoại suy nên đánh giá quá cao.
- **Hàm ý cho Trung tâm Nhiệt đới Việt – Nga:** không nên dùng nguyên trạng hàm ISO 9223 hay mô hình học từ dữ liệu quốc tế cho Việt Nam. Cần **bộ hệ số hiệu chỉnh nhiệt đới** từ số liệu trạm của chính Trung tâm.

### 5.3. Dự báo dài hạn cho điều kiện Việt Nam (DRF hiệu chỉnh vùng + ISO 9224)

Điều kiện: T = 25 °C, TOW = 5.500 h/năm, SO₂ = 5 mg/m²·ngày.

| Môi trường | Cl⁻ (mg/m²·ngày) | r (µm/năm) | D sau 10 năm | D sau 25 năm | D sau 50 năm |
|---|---|---|---|---|---|
| Nội địa (kiểu Hà Nội) | 2,2 | 28 | 94 µm | 153 µm | 242 µm |
| Ven biển (kiểu Đồ Sơn) | 17,5 | 45 | 149 µm | 243 µm | 383 µm |
| Ven biển mạnh (ngoại suy) | 100 | 117 | 391 µm | 636 µm | ≈ 1,0 mm |

Hàng cuối nằm ngoài miền số đo Việt Nam (Cl⁻ tối đa đo được là 17,5), chỉ để tham khảo.

## 6. Mô hình 3D

| Mô hình | Mô tả | Mức căn cứ | Tệp |
|---|---|---|---|
| **3D-1. Mặt đáp ứng** | r(Cl⁻, TOW) cho khí hậu Việt Nam và Viễn Đông Nga; điểm trên hình là số đo thật | Định lượng: DRF hiệu chỉnh vùng | `3D_1_mat_dap_ung.html` (tương tác), `.png` |
| **3D-2. Diễn tiến theo thời gian** | D(t, Cl⁻) trong 0–50 năm, khí hậu Việt Nam; 3 đường cho Hà Nội, Đồ Sơn, ven biển mạnh | Định lượng: DRF + ISO 9224 | `3D_2_dien_tien_theo_thoi_gian.html` |
| **3D-3. Bề mặt tấm thép** | Bề mặt tấm 40×40 mm tại Nha Trang và Hà Nội sau 1, 5, 10, 20 năm (thanh trượt) | **Độ sâu trung bình:** định lượng (số đo năm đầu + ISO 9224). **Độ nhám, hố cục bộ:** minh họa, tham số giả định | `3D_3_be_mat_tam_thep.html`, `.png` |

**Đọc mô hình 3D-3:**

| Trạm | 1 năm | 5 năm | 10 năm | 20 năm |
|---|---|---|---|---|
| Nha Trang (r đo = 40,6 µm) | 41 µm | 94 µm | 135 µm | 194 µm |
| Hà Nội (r đo = 31,8 µm) | 32 µm | 74 µm | 106 µm | 152 µm |

Đây là độ sâu trung bình. Độ sâu cục bộ lớn nhất trên hình (Nha Trang 20 năm khoảng 450 µm) phụ thuộc vào tham số độ nhám giả định, **không dùng để kết luận**. Để mô hình 3D-3 trở thành kết quả định lượng, cần đo biên dạng bề mặt (profilometry hoặc quét 3D) các mẫu thực tại trạm của Trung tâm, rồi hiệu chỉnh hai tham số: hệ số biến thiên độ sâu và độ dài tương quan.

Các tệp `.html` mở bằng trình duyệt, xoay và phóng to được; cần Internet để tải thư viện Plotly.

## 7. Hạn chế và hướng mở rộng lên hàng nghìn mẫu

**Hạn chế:**
1. Mới có 387 quan sát, chỉ cho thép cacbon, chỉ tốc độ năm đầu.
2. Không có RH, lượng mưa, bức xạ nên chưa áp dụng được nguyên văn hàm ISO 9223.
3. Số trạm Việt Nam (12) đủ để phát hiện sai lệch hệ thống, chưa đủ để xây mô hình riêng.
4. ISO 9224 b = 0,523 là giá trị trung bình toàn cầu, chưa kiểm chứng cho nhiệt đới.

**Nguồn dữ liệu để mở rộng** (tải từ máy có Internet, lưu theo mẫu `du-lieu/4-bo-sung/MAU_bo_sung.csv.template`, đặt vào `du-lieu/4-bo-sung/`, rồi chạy lại 4 script):

| Nguồn | Nội dung | Ưu tiên |
|---|---|---|
| **Số liệu trạm của Trung tâm Nhiệt đới Việt – Nga** | Nhiều kim loại, nhiều năm, có RH | ★★★ – giá trị cao nhất |
| Chico et al. (2017), *Materials* 10(6):601, truy cập mở | ISOCORRAG + ICP/UNECE + MICAT đầy đủ | ★★★ |
| Lien et al. (2007, 2013) – bảng số liệu gốc | Việt Nam 1995–2005, có cả kẽm, đồng | ★★★ |
| Panchenko & Marshakov (2017, 2020) | Nga, lục địa và ven biển | ★★ |
| Zenodo 20973741 "List of sites and their respective data" (2026) | Tổn thất ăn mòn nhiều trạm | ★★ – cần kiểm tra nội dung |
| Dữ liệu cảm biến ACM (Fe/Cu) của Trung tâm, nếu có | Chuỗi thời gian theo phút → hàng triệu điểm | ★★★ cho nghiên cứu động học |

## 8. Tài liệu tham khảo

- Chico B., de la Fuente D., Díaz I., Simancas J., Morcillo M. (2017). Annual atmospheric corrosion of carbon steel worldwide. An integration of ISOCORRAG, ICP/UNECE and MICAT databases. *Materials* 10(6), 601. https://doi.org/10.3390/ma10060601
- Pintos S., Queipo N.V., de Rincón O.T., Rincón A., Morcillo M. (2000). Artificial neural network modeling of atmospheric corrosion in the MICAT project. *Corrosion Science* 42, 35–52. https://doi.org/10.1016/S0010-938X(99)00054-2
- Le Thi Hong Lien, Pham Thy San, Hoang Lam Hong (2007). Results of studying atmospheric corrosion in Vietnam 1995–2005. *Science and Technology of Advanced Materials* 8(7–8), 552–558.
- Panchenko Yu.M., Marshakov A.I. (2017). Prediction of first-year corrosion losses of carbon steel and zinc in continental regions. *Materials* 10(4), 422. https://doi.org/10.3390/ma10040422
- ISO 9223:2012 – Corrosivity of atmospheres – Classification, determination and estimation.
- ISO 9224:2012 – Guiding values for the corrosivity categories (b = 0,523 cho thép cacbon, B1).
- Kho dữ liệu: arashrockey/C-OLR, https://github.com/arashrockey/C-OLR (MIT).
