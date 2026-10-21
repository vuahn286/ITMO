# BẢN THẢO BÀI BÁO

> **Trạng thái:** bản thảo minh họa, **soạn với hỗ trợ của AI** từ kết quả trong `../05-ket-qua/`; **chưa phản biện nội bộ, chưa nộp**. Tác giả chịu trách nhiệm kiểm tra toàn bộ nội dung, số liệu, trích dẫn trước khi dùng.
> **Tạp chí dự kiến:** Tạp chí Khoa học và Công nghệ nhiệt đới (ISSN 0866-7535) – theo thể lệ của tạp chí. Bản tiếng Anh / tiếng Nga cho tạp chí Scopus / ВАК: xem câu lệnh mục 10, `thuyet-trinh/cau-lenh-demo.md`.

---

## ĐÁNH GIÁ KHẢ NĂNG ÁP DỤNG MÔ HÌNH LIỀU – ĐÁP ỨNG QUỐC TẾ CHO DỰ BÁO ĂN MÒN KHÍ QUYỂN CỦA THÉP CACBON TRONG KHÍ HẬU NHIỆT ĐỚI VIỆT NAM

**Tác giả:** [CẦN BỔ SUNG] · **Đơn vị:** Trung tâm Nhiệt đới Việt – Nga [CẦN BỔ SUNG]

### Tóm tắt

Hàm liều – đáp ứng của tiêu chuẩn ISO 9223 được dùng rộng rãi để ước lượng tốc độ ăn mòn khí quyển năm đầu của kim loại từ số liệu môi trường, nhưng được xây dựng chủ yếu từ dữ liệu vùng ôn đới. Nghiên cứu này đánh giá khả năng áp dụng các mô hình học từ dữ liệu quốc tế cho khí hậu nhiệt đới Việt Nam, sử dụng 387 số đo thực địa đã công bố về tốc độ ăn mòn năm đầu của thép cacbon. Hai mô hình – hàm liều – đáp ứng dạng ISO 9223 (dùng thời gian ẩm ướt thay độ ẩm tương đối) và mô hình gradient boosting có ràng buộc đơn điệu – được huấn luyện trên 320 trạm của các chương trình ISOCORRAG và MICAT, kiểm định độc lập trên 67 trạm, trong đó có 12 trạm Việt Nam và 18 trạm Nga. Mô hình quốc tế dự đoán thấp hơn thực đo khoảng 31% tại các trạm Việt Nam (11/12 trạm) và cao hơn khoảng 80% tại các trạm lạnh của Nga; chỉ 2/12 trạm Việt Nam được xếp đúng cấp ăn mòn. Hệ số hiệu chỉnh vùng, đánh giá bằng kiểm định bỏ-một-trạm, giảm sai số tương đối trung vị tại Việt Nam từ 26,8% xuống 18,6% và nâng số trạm đúng cấp lên 9/12. Quá trình kiểm tra dữ liệu phát hiện lỗi nhãn đơn vị trong bộ dữ liệu công bố. Kết quả cho thấy cần bộ hằng số liều – đáp ứng riêng cho khí hậu nhiệt đới Việt Nam.

**Từ khóa:** ăn mòn khí quyển; thép cacbon; ISO 9223; hàm liều – đáp ứng; khí hậu nhiệt đới; Việt Nam.

### Abstract

*Assessing the applicability of international dose–response models for predicting atmospheric corrosion of carbon steel in the tropical climate of Vietnam.* The ISO 9223 dose–response function is widely used to estimate first-year atmospheric corrosion rates from environmental data, but it was derived mostly from temperate-climate exposure programmes. Using 387 published field measurements of first-year carbon-steel corrosion, we trained a dose–response function of the ISO 9223 form (with time of wetness in place of relative humidity) and a monotonic-constrained gradient-boosting model on 320 ISOCORRAG and MICAT sites, and tested them on 67 independent sites, including 12 in Vietnam and 18 in Russia. The international models under-predicted corrosion in Vietnam by about 31% (11 of 12 sites) and over-predicted it at cold Russian sites by about 80%; only 2 of 12 Vietnamese sites were assigned the correct ISO category. A regional correction factor, evaluated by leave-one-site-out validation, reduced the median relative error in Vietnam from 26.8% to 18.6% and raised correct classification to 9 of 12 sites. Data screening also revealed a unit-label error in the published dataset. Tropical-specific dose–response constants are needed for Vietnam.

**Keywords:** atmospheric corrosion; carbon steel; ISO 9223; dose–response function; tropical climate; Vietnam.

---

### 1. Mở đầu

Ăn mòn khí quyển là nguyên nhân chính gây suy giảm độ bền của kết cấu và trang thiết bị thép trong khí hậu nhiệt đới. Tiêu chuẩn ISO 9223:2012 phân cấp độ ăn mòn khí quyển (C1–CX) theo tốc độ ăn mòn năm đầu của kim loại chuẩn và cung cấp hàm liều – đáp ứng để ước lượng tốc độ này từ nhiệt độ, độ ẩm, tốc độ lắng đọng clorua và SO₂ [10]; ISO 9224:2012 cho phép ngoại suy dài hạn theo dạng D = r·tᵇ [11].

Các hàm này được xây dựng chủ yếu từ dữ liệu các chương trình phơi mẫu quốc tế như ISOCORRAG, ICP/UNECE và MICAT [6, 7]. Một số nghiên cứu đã chỉ ra hạn chế khi áp dụng ngoài vùng khí hậu gốc: ở quần đảo Canary (cận nhiệt đới), hàm ISO 9223 cho ước lượng kém và cần bộ hằng số mới [9]. Ở Việt Nam, kết quả phơi mẫu 1995–2005 cho thấy thời gian ẩm ướt dài là yếu tố chi phối, đưa thép cacbon vào cấp C3 dù nồng độ clorua và SO₂ không cao [1]; các nghiên cứu khác đã xây dựng mô hình và bản đồ ăn mòn cho Việt Nam [3–5].

Bài báo này trả lời câu hỏi: **mô hình liều – đáp ứng học từ dữ liệu quốc tế có dự báo đúng tốc độ ăn mòn năm đầu của thép cacbon ở Việt Nam không, và sai lệch theo vùng khí hậu lớn đến đâu?**

### 2. Dữ liệu và phương pháp

**2.1. Dữ liệu.** Sử dụng bộ dữ liệu công bố mở C-OLR [12] gồm 387 quan sát tốc độ ăn mòn năm đầu của thép cacbon cùng nhiệt độ trung bình năm (T), thời gian ẩm ướt (TOW), tốc độ lắng đọng Cl⁻ và SO₂: 190 trạm ISOCORRAG [6] và 130 trạm MICAT [7] (tập huấn luyện); 67 trạm từ các công bố độc lập (tập kiểm định), gồm 12 trạm Việt Nam [1], 18 trạm Nga, 26 trạm Tây Ban Nha và 11 trạm Colombia.

**2.2. Kiểm tra chất lượng dữ liệu.** Đơn vị của biến tốc độ ăn mòn được kiểm tra bằng cách đối chiếu với cấp ăn mòn ghi trong nguồn theo ngưỡng ISO 9223; cấp ăn mòn được tính lại; các giá trị bằng 0 của Cl⁻, SO₂ được thay bằng 0,1 mg/m²·ngày khi lấy logarit. Phân bố, độ nhạy ngoại lệ và rò rỉ giữa tập huấn luyện – kiểm định được kiểm tra bằng bộ công cụ `exploratory-data-analysis` [13], không xóa hay biến đổi dữ liệu gốc.

**2.3. Mô hình.** (i) Hàm liều – đáp ứng (DRF) dạng ISO 9223:

r = a·SO₂ᵇ·exp(c·τ + f(T)) + d·Cl⁻ᵉ·exp(g·τ + h·T), với τ = TOW/1000, f(T) tuyến tính từng đoạn quanh 10 °C,

ước lượng bằng bình phương tối thiểu bền vững (hàm mất mát soft-L1) trên thang log; (ii) gradient boosting với ràng buộc đơn điệu tăng theo Cl⁻, SO₂ và TOW; (iii) trung bình hình học của hai mô hình.

**2.4. Kiểm định.** Kiểm định chéo 10 lần trên tập huấn luyện; kiểm định độc lập trên 67 trạm; chỉ số: R² và RMSE trên thang log, sai số tương đối trung vị, tỷ lệ đúng cấp ISO và lệch tối đa 1 cấp. Sai lệch theo vùng được hiệu chỉnh bằng hệ số k (trung bình hình học của tỉ số đo/dự đoán), đánh giá bằng kiểm định bỏ-một-trạm. Ngoại suy dài hạn theo ISO 9224 với b = 0,523 [11]. Toàn bộ mã nguồn được lưu để tái lập [14].

### 3. Kết quả và thảo luận

**3.1. Chất lượng dữ liệu.** Biến tốc độ ăn mòn được mô tả trong nguồn là g/m², nhưng chỉ 33,1% quan sát khớp với cấp ăn mòn đi kèm nếu hiểu theo g/m², so với 99,5% nếu hiểu là µm/năm – xác nhận đơn vị thực là µm/năm. Hai trạm có cấp ghi trong nguồn không khớp ngưỡng ISO (Barcelona: 49,9 µm/năm → C3; El Hierro: 263,2 µm/năm → CX). Phân bố tốc độ ăn mòn lệch phải mạnh (hệ số bất đối xứng 4,66; sau biến đổi log còn −0,02), là căn cứ để mô hình hóa trên thang log; 31/387 giá trị nằm ngoài ngưỡng IQR (trung bình 37,7 µm/năm, giảm còn 29,2 µm/năm nếu loại các giá trị này; trung vị 28,1). Không có trạm nào xuất hiện đồng thời ở cả hai tập.

**3.2. Hiệu năng mô hình quốc tế.**

*Bảng 1. Hiệu năng mô hình*

| Mô hình | Tập | R² (log) | Sai số tương đối trung vị | Đúng cấp ISO | Lệch ≤ 1 cấp |
|---|---|---|---|---|---|
| DRF | Kiểm định chéo (n = 320) | 0,61 | 27,1% | 63,1% | 97,5% |
| Gradient boosting | Kiểm định chéo (n = 320) | 0,71 | 23,1% | 67,5% | 98,1% |
| DRF | Kiểm định độc lập (n = 67) | 0,44 | 34,4% | 55,2% | 98,5% |
| Gradient boosting | Kiểm định độc lập (n = 67) | 0,39 | 30,6% | 59,7% | 97,0% |

Mức độ quan trọng của biến (hoán vị, tập kiểm định): log Cl⁻ 0,57 > log SO₂ 0,53 > TOW 0,38; nhiệt độ không đóng góp. Số mũ ước lượng của Cl⁻ (e = 0,88) và SO₂ (b = 0,46) cùng bậc với dạng hàm ISO 9223.

**3.3. Sai lệch theo vùng khí hậu.**

*Bảng 2. Sai lệch và hiệu chỉnh vùng (trung bình hình học hai mô hình)*

| Vùng | Sai lệch trung bình của mô hình quốc tế | k | Sai số trung vị: trước → sau hiệu chỉnh (bỏ-một-trạm) | Đúng cấp ISO: trước → sau |
|---|---|---|---|---|
| Việt Nam (n = 12) | −31,5% | 1,46 | 26,8% → 18,6% | 2/12 → 9/12 |
| Nga (n = 18) | +80,1% | 0,56 | 85,9% → 32,0% | 14/18 → 15/18 |

Mô hình quốc tế đánh giá thấp ăn mòn ở 11/12 trạm Việt Nam. Sai lệch lớn nhất ở Huế (Cl⁻ 1,3 mg/m²·ngày, thực đo 31,5 µm/năm) và Nha Trang (Cl⁻ 13,8 mg/m²·ngày, thực đo 40,6 µm/năm). Phù hợp với nhận định rằng thời gian ẩm ướt dài chi phối ăn mòn ở Việt Nam [1], điều này gợi ý các yếu tố chưa có trong bộ biến – như mưa, độ ẩm tương đối liên tục, chu kỳ khô – ướt [3] – đóng vai trò đáng kể (*diễn giải đề xuất, cần kiểm chứng*). Ở Nga, nhiệt độ trung bình −13 đến 5 °C phần lớn nằm ngoài miền dữ liệu huấn luyện, nên mô hình ngoại suy và đánh giá quá cao. Kết quả phù hợp với nhận định về hạn chế của hàm ISO 9223 ngoài vùng khí hậu gốc [9].

**3.4. Dự báo dài hạn.** Với T = 25 °C, TOW = 5.500 giờ/năm, SO₂ = 5 mg/m²·ngày, hàm liều – đáp ứng đã hiệu chỉnh vùng cho tốc độ năm đầu 28 µm/năm (Cl⁻ 2,2 – kiểu Hà Nội) và 45 µm/năm (Cl⁻ 17,5 – kiểu Đồ Sơn); chiều dày tổn thất ngoại suy theo ISO 9224 sau 10, 25, 50 năm lần lượt khoảng 94, 153, 242 µm và 149, 243, 383 µm. Số mũ b = 0,523 là giá trị trung bình toàn cầu, chưa được kiểm chứng cho khí hậu nhiệt đới.

**3.5. Hạn chế.** (i) Chỉ có 12 trạm Việt Nam, từ giai đoạn 1995–2005, chỉ tốc độ năm đầu của thép cacbon; (ii) không có độ ẩm tương đối, lượng mưa nên chưa áp dụng nguyên văn hàm ISO 9223; (iii) hệ số hiệu chỉnh vùng là một hằng số nhân, chưa phải bộ hằng số mới; (iv) nguồn gốc 18 trạm Nga chưa được xác định chắc chắn.

### 4. Kết luận

1. Bộ dữ liệu công bố mở chứa lỗi nhãn đơn vị và 2 cấp ăn mòn ghi sai; kiểm tra chéo giữa các cột phát hiện được lỗi này.
2. Mô hình liều – đáp ứng học từ dữ liệu quốc tế dự đoán thấp hơn thực đo khoảng 31% tốc độ ăn mòn năm đầu của thép cacbon ở Việt Nam, và chỉ xếp đúng cấp 2/12 trạm.
3. Hiệu chỉnh vùng đơn giản cải thiện rõ dự báo (đúng cấp 9/12 trạm), nhưng cần một bộ hằng số liều – đáp ứng riêng, có thêm biến độ ẩm, mưa, cho khí hậu nhiệt đới Việt Nam – dựa trên số liệu phơi mẫu mới.

### Khai báo sử dụng trí tuệ nhân tạo

Công cụ AI (Claude, Anthropic) được dùng để hỗ trợ viết mã phân tích, kiểm tra dữ liệu và soạn bản thảo. Bộ công cụ `exploratory-data-analysis` [13] được dùng để kiểm tra dữ liệu. Tác giả đã kiểm tra và chịu trách nhiệm toàn bộ nội dung. Công cụ AI không đứng tên tác giả. *[Điều chỉnh theo quy định của tạp chí.]*

### Dữ liệu và mã nguồn

Dữ liệu: bộ C-OLR (giấy phép MIT) [12]. Mã nguồn, dữ liệu đã xử lý và kết quả: [CẦN BỔ SUNG – kho lưu trữ có DOI, ví dụ Zenodo].

### Tài liệu tham khảo

[1] Le Thi Hong Lien, Pham Thy San, Hoang Lam Hong (2007). Results of studying atmospheric corrosion in Vietnam 1995–2005. *Sci. Technol. Adv. Mater.* 8(7–8):552–558. doi:10.1016/j.stam.2007.08.011
[2] Le Thi Hong Lien (2013). Summarize the results of study on atmospheric corrosion in Vietnam. *Vietnam J. Sci. Technol.*
[3] Tran T.N.L., Nguyen T.P.T., Nishimura R., Tsujino Y., Yokoi M., Maeda Y. (2006). Atmospheric corrosion of carbon steel under field exposure in the southern part of Vietnam. *Corros. Sci.* 48(1):179–192. doi:10.1016/j.corsci.2004.11.018
[4] Karpov V.A., Lapiga A.G., Kalinina E.V., Mikhailova O.L., Koval'chuk Yu.L. (2017). Modeling of atmospheric corrosion in the tropical climate of Vietnam. *Prot. Met. Phys. Chem. Surf.* 53(7):1205. doi:10.1134/S2070205117070085
[5] Cole I., Nguyễn Việt Huệ (2010). Steel corrosion map of Vietnam. *Tạp chí Khoa học và Công nghệ* 48(6):109–115.
[6] Chico B., de la Fuente D., Díaz I., Simancas J., Morcillo M. (2017). Annual atmospheric corrosion of carbon steel worldwide. An integration of ISOCORRAG, ICP/UNECE and MICAT databases. *Materials* 10(6):601. doi:10.3390/ma10060601
[7] Pintos S., Queipo N.V., de Rincón O.T., Rincón A., Morcillo M. (2000). Artificial neural network modeling of atmospheric corrosion in the MICAT project. *Corros. Sci.* 42:35–52. doi:10.1016/S0010-938X(99)00054-2
[8] Panchenko Yu.M., Marshakov A.I. (2017). Prediction of first-year corrosion losses of carbon steel and zinc in continental regions. *Materials* 10(4):422. doi:10.3390/ma10040422
[9] Santana J.J., Ramos A., Rodriguez-Gonzalez A., Vasconcelos H.C., Mena V., Fernández-Pérez B.M., Souto R.M. (2019). Shortcomings of International Standard ISO 9223 for the classification, determination, and estimation of atmosphere corrosivities in subtropical archipelagic conditions — The case of the Canary Islands (Spain). *Metals* 9(10):1105. doi:10.3390/met9101105
[10] ISO 9223:2012. Corrosion of metals and alloys — Corrosivity of atmospheres — Classification, determination and estimation.
[11] ISO 9224:2012. Corrosion of metals and alloys — Corrosivity of atmospheres — Guiding values for the corrosivity categories.
[12] C-OLR: Constrained Ordinal Logistic Regression for Atmospheric Corrosivity Classification (2026). https://github.com/arashrockey/C-OLR
[13] Kassis T., Agarwal V., He Y., Patel D., Brueckner A.M. (2026). Scientific Agent Skills: A Library of Procedural Knowledge for Research Agents. arXiv:2609.00065.
[14] [CẦN BỔ SUNG – kho mã của dự án]

*Ghi chú cho tác giả: [2] và [8] có trong danh mục nhưng chưa được trích trong bài – trích hoặc bỏ khi hoàn thiện.*
