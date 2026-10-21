# BỘ CÂU LỆNH DEMO – SAO CHÉP VÀ DÁN TRỰC TIẾP VÀO CLAUDE

> Dùng kèm **Kế hoạch thuyết trình** và **DANH-SACH-SLIDE.md** (số slide theo bản v2.3). Mỗi câu lệnh ghi rõ: dán vào đâu, cần tải tệp nào và kết quả mong đợi (để đối chiếu với thư mục `ket-qua-mau/`).
> Tình huống xuyên suốt: **Đánh giá ăn mòn khí quyển của kim loại tại ba trạm thử nghiệm nhiệt đới** (Phương án A). Toàn bộ dữ liệu là **giả lập, thuộc nhóm xanh**.

---

## 0. Chuẩn bị (làm một lần, trước buổi thuyết trình)

1. Đăng nhập claude.ai. Vào **Settings → Capabilities**, bật **Code execution and file creation** (để Claude tự viết và chạy mã Python; tên mục có thể khác đôi chút tùy phiên bản giao diện). Nếu dùng tìm tài liệu, bật thêm **Web search**.
2. Tạo **Project** tên `Demo – Ăn mòn khí quyển nhiệt đới`.
3. Trong *Project instructions*, dán:

```
Bạn là trợ lý nghiên cứu cho nhóm nghiên cứu độ bền nhiệt đới của vật liệu.
- Luôn trả lời bằng tiếng Việt; thuật ngữ chuyên ngành ghi kèm tiếng Anh trong ngoặc khi xuất hiện lần đầu.
- Khi nêu thông tin từ tài liệu: ghi rõ tác giả, năm, DOI hoặc đường dẫn. Không chắc chắn thì ghi "cần kiểm tra", không tự bịa nguồn.
- Khi xử lý dữ liệu: viết mã Python, chạy mã, báo cáo từng bước đã làm; không tự ý xóa dữ liệu – chỉ đánh dấu và đề xuất.
- Phân biệt rõ "kết quả tính toán" và "diễn giải khoa học (cần nhà khoa học xác nhận)".
```

4. Tải vào *Project knowledge*: `du-lieu-demo/an_mon_tho.csv`, `du-lieu-demo/khi_tuong_tram.csv`, `du-lieu-demo/ke_hoach_cong_viec.csv` và mẫu thuyết minh trống (Mẫu 01A/07/08).

---

## 1. Slide 13 – Tài liệu → khoảng trống nghiên cứu

### Câu lệnh 1.1 – Lập bản đồ chủ đề (bật Web search hoặc dùng Research)
```
Tôi chuẩn bị đề xuất nhiệm vụ về ăn mòn khí quyển của thép cacbon, kẽm, đồng, nhôm trong khí hậu nhiệt đới ẩm ven biển Việt Nam.
Hãy tìm các công bố 2015–2026 và lập bản đồ chủ đề gồm 5–7 hướng nghiên cứu chính. Với mỗi hướng: 2–3 công trình tiêu biểu (tác giả, năm, tạp chí, DOI), phương pháp chủ yếu, kết luận chính.
Chú ý các chương trình/tiêu chuẩn: ISO 9223/9224, ICP Materials (UNECE), MICAT.
Chỉ liệt kê công trình mà bạn tìm thấy đường dẫn thật.
```
**Kết quả mong đợi:** bảng 5–7 hướng (ví dụ: mô hình liều – đáp ứng; vai trò clorua; bản đồ phân vùng ăn mòn; sản phẩm ăn mòn/lớp gỉ; dự báo dài hạn; ảnh hưởng biến đổi khí hậu…).
**Gợi ý nói:** "Việc này trước đây mất 1–2 tuần đọc lướt; AI cho bản nháp trong vài phút. Nhưng **mỗi DOI tôi đều bấm thử**: đây là việc của nhà khoa học."

### Câu lệnh 1.2 – Ma trận bằng chứng (sau khi đã tải 10–15 bài PDF vào Project)
```
Từ các bài báo trong Project, lập ma trận bằng chứng với các cột:
Tác giả–năm | Địa điểm & loại khí hậu | Kim loại | Thời gian phơi mẫu | Biến môi trường đo (T, RH, TOW, Cl-, SO2) | Mô hình sử dụng | Giá trị n (nếu có) | Kết luận chính | Hạn chế tác giả tự nêu.
Sau bảng, chỉ ra: (a) các điểm các nghiên cứu KHÔNG thống nhất; (b) 3 khoảng trống nghiên cứu cho điều kiện Việt Nam, mỗi khoảng trống dẫn chứng bằng ít nhất 2 bài trong bảng.
```
**Kết quả mong đợi:** bảng 10–15 dòng; 3 khoảng trống, ví dụ: "thiếu chuỗi số liệu > 3 năm cho nhôm ở vùng ven biển miền Trung", "hệ số n trong điều kiện nhiệt đới khác ISO 9224 thế nào".

### Câu lệnh 1.3 – Phản biện khoảng trống (mô phỏng cách làm của AI co-scientist)
```
Đóng vai 3 chuyên gia phản biện độc lập (ăn mòn điện hóa; khí tượng – môi trường; thống kê) đánh giá 3 khoảng trống ở trên theo: tính mới, tính khả thi trong 3 năm, giá trị ứng dụng cho Việt Nam. Cho điểm 1–5, nêu lý do, rồi xếp hạng.
```
**Gợi ý nói:** "Google dùng nhiều agent tranh luận với nhau để chọn giả thuyết; ở quy mô nhỏ, ta làm được điều tương tự bằng một câu lệnh."

---

## 2. Slide 14 – Khoảng trống → thuyết minh (DEMO 1, trình diễn trực tiếp câu lệnh 2.2)

### Câu lệnh 2.1 – Soạn các mục thuyết minh
```
Chọn khoảng trống số [1]. Soạn bản nháp các mục: (1) Tính cấp thiết (≤ 300 từ, có trích dẫn từ ma trận bằng chứng); (2) Mục tiêu tổng quát và 2–3 mục tiêu cụ thể đo lường được; (3) Nội dung nghiên cứu (5–7 nội dung); (4) Phương pháp cho từng nội dung; (5) Sản phẩm dự kiến kèm chỉ tiêu định lượng.
Thời gian thực hiện 36 tháng, 3 trạm thử nghiệm, 4 kim loại, 7 mốc thu mẫu, 3 mẫu lặp.
```

### Câu lệnh 2.2 – Kiểm tra logic (trình diễn trực tiếp)
```
Lập bảng đối chiếu: Mục tiêu cụ thể → Nội dung → Phương pháp → Sản phẩm → Chỉ tiêu đánh giá.
Đánh dấu ⚠ ở mọi chỗ: mục tiêu không có nội dung tương ứng; sản phẩm không có chỉ tiêu đo được; phương pháp không đủ để đạt mục tiêu; số mẫu không khớp (3 trạm × 4 kim loại × 7 mốc × 3 lặp = ? mẫu).
```
**Kết quả mong đợi:** bảng 5 cột, có tính tổng **252 mẫu**, chỉ ra ít nhất 1–2 chỗ ⚠ (ví dụ: mục tiêu "bản đồ phân vùng" nhưng chỉ có 3 trạm → không đủ để nội suy).
**Gợi ý nói:** "Hội đồng thường bắt lỗi đúng những chỗ này. Để AI soát trước giúp ta sửa từ sớm."

### Câu lệnh 2.3 – Điền vào biểu mẫu
```
Điền nội dung đã thống nhất vào đúng cấu trúc Mẫu [01A] trong Project. Giữ nguyên số mục, tiêu đề của mẫu; mục nào chưa đủ thông tin thì ghi [CẦN BỔ SUNG: ...]. Xuất ra tệp .docx.
```

---

## 3. Slide 15 – Tiến độ và kinh phí

### Câu lệnh 3.1 (tệp `ke_hoach_cong_viec.csv`)
```
Đọc tệp ke_hoach_cong_viec.csv. Hãy:
1. Vẽ sơ đồ Gantt (trục thời gian theo tháng, ghi kinh phí cuối mỗi thanh).
2. Tính tổng kinh phí và tỷ lệ % theo đơn vị thực hiện.
3. Kiểm tra logic trình tự: nội dung nào bắt đầu trước khi nội dung tiền đề kết thúc; dữ liệu nào không phủ hết thời gian của nội dung dùng dữ liệu đó. Liệt kê và đề xuất điều chỉnh.
```
**Kết quả mong đợi (đã chạy thử):**
- Tổng kinh phí **1.350 triệu đồng**; Gantt như `ket-qua-mau/so_do_gantt.png`.
- AI cần phát hiện 3 điểm (cài sẵn): (1) ND4 *thu mẫu* bắt đầu 04/2027 khi ND2 *lắp đặt giá phơi mẫu* đến 05/2027 mới xong; (2) ND3 *quan trắc khí tượng* kết thúc 03/2030, sớm hơn ND4 (04/2030) → tháng cuối không có số liệu môi trường; (3) ND7 *công bố* bắt đầu 06/2029 khi ND5 *mô hình* chưa xong (chấp nhận được nếu là bài báo kết quả giữa kỳ – **nhà khoa học quyết định**).

---

## 4. Slide 16 – Dữ liệu thô → kết quả (DEMO 2, trình diễn trực tiếp 4.2 – 4.4)

### Câu lệnh 4.1 – Từ điển dữ liệu
```
Đọc an_mon_tho.csv và khi_tuong_tram.csv. Lập từ điển dữ liệu: tên cột | ý nghĩa (suy luận) | kiểu dữ liệu | đơn vị | khoảng giá trị | số ô trống. Những cột bạn không chắc ý nghĩa thì đánh dấu "cần xác nhận".
```

### Câu lệnh 4.2 – Rà soát chất lượng dữ liệu
```
Rà soát an_mon_tho.csv: dòng trùng, tên trạm không thống nhất, ô trống, số sai định dạng (dấu phẩy, dính đơn vị), ngày sai định dạng, giá trị phi vật lý (khối lượng sau > trước), ngoại lệ giữa các mẫu lặp (cùng trạm – kim loại – thời gian), và các ghi chú thực nghiệm cần lưu ý.
Lưu ý: mỗi nhóm chỉ có 3 mẫu lặp – chọn phương pháp phát hiện ngoại lệ phù hợp với cỡ mẫu nhỏ và giải thích lý do.
Xuất báo cáo dạng bảng: loại lỗi | mã mẫu | mô tả | đề xuất xử lý. KHÔNG xóa dữ liệu gốc.
```
**Kết quả mong đợi (đã chạy thử – `ket-qua-mau/bao_cao_chat_luong_du_lieu.csv`):** 14 vấn đề

| Loại | Số lượng | Mã mẫu |
|---|---|---|
| Trùng dòng | 1 | DO-TH-06-2 |
| Tên trạm không thống nhất | 2 | BI-DO-03-3 (`Tram bien`), NO-NH-01-2 (`tram_noidia `) |
| Thiếu số liệu | 3 | BI-TH-12-2, DO-KE-24-3, NO-DO-06-1 |
| Sai định dạng số | 2 | BI-KE-06-2 (`107,1491`), DO-TH-03-1 (`114.2493 g`) |
| Sai định dạng ngày | 2 | DO-NH-12-2 (`14/01/2024`), NO-KE-36-1 (`2026/01/13`) |
| Giá trị phi vật lý | 1 | NO-TH-18-3 (khối lượng sau > trước) |
| Ngoại lệ giữa mẫu lặp | 1 | BI-TH-24-1 (lệch +69% so với 2 mẫu lặp) |
| Ghi chú thực nghiệm | 2 | BI-TH-36-2 (mẫu rơi, mất gỉ), DO-DO-18-1 (tẩy gỉ lần 2) |

**Gợi ý nói (bài học thật khi chạy thử):** "Lần đầu, mã dùng phương pháp z-score/MAD và đánh dấu nhầm **20 giá trị bình thường**, trong khi bỏ sót đúng lỗi gõ nhầm. Lý do: mỗi nhóm chỉ có 3 mẫu lặp. Tôi yêu cầu đổi sang quy tắc 'lệch > 30% so với 2 mẫu lặp còn lại' thì kết quả mới đúng. **AI viết mã rất nhanh, nhưng chọn phương pháp phù hợp là việc của người làm chuyên môn.**" Chính vì vậy câu lệnh 4.2 có thêm dòng "mỗi nhóm chỉ có 3 mẫu lặp".

### Câu lệnh 4.3 – Phân tích và mô hình
```
Làm sạch dữ liệu theo báo cáo trên (loại các dòng lỗi khỏi phân tích, giữ bản gốc). Sau đó:
1. Tính tổn thất khối lượng C (g/m²) = (m_trước − m_sau) / diện tích; quy đổi ra chiều dày (µm) theo khối lượng riêng: thép 7,85; kẽm 7,14; đồng 8,96; nhôm 2,70 g/cm³.
2. Với mỗi trạm × kim loại, hồi quy mô hình C = A·t^n (t tính bằng năm) trên thang log–log; báo cáo A, n, R².
3. Xếp cấp ăn mòn theo ISO 9223:2012 dựa trên A (tổn thất năm đầu).
4. Dự báo tổn thất sau 10 năm theo mô hình.
Lưu toàn bộ mã Python để tái lập.
```
**Kết quả mong đợi (`ket-qua-mau/mo_hinh_A_n.csv`):**

| Trạm | Kim loại | A (g/m²) | n | R² | Cấp ISO 9223 | Dự báo 10 năm (µm) |
|---|---|---|---|---|---|---|
| Ven biển | Thép CT3 | 566,9 | 0,74 | 0,997 | C4 | 397 |
| Đô thị | Thép CT3 | 304,9 | 0,71 | 0,994 | C3 | 201 |
| Nội địa | Thép CT3 | 159,8 | 0,72 | 0,996 | C2 | 108 |
| Ven biển | Kẽm | 22,1 | 0,85 | 0,996 | C4 | 21,8 |
| Ven biển | Đồng | 18,2 | 0,68 | 0,995 | C4 | 9,7 |
| Ven biển | Nhôm | 4,2 | 0,59 | 0,993 | C4 | 6,0 |

(Ngưỡng ISO 9223:2012 đã đối chiếu cho thép và kẽm; với đồng và nhôm, ngưỡng C4 trở lên cần đối chiếu bản gốc tiêu chuẩn trước khi nói "C4". Đầy đủ 12 dòng trong tệp CSV. Do mô hình chạy lại có thể chọn cách làm sạch hơi khác, các số có thể lệch nhẹ – sai khác lớn là dấu hiệu cần xem lại.)

### Câu lệnh 4.4 – Biểu đồ
```
Vẽ: (1) 4 biểu đồ con (mỗi kim loại một ô), trục log–log, điểm đo và đường mô hình theo 3 trạm, chú thích A, n và cấp ISO; (2) biểu đồ cột chiều dày tổn thất (µm) của thép theo trạm và thời gian. Nhãn tiếng Việt, xuất PNG 150 dpi.
```
**Kết quả mong đợi:** `ket-qua-mau/bieu_do_dong_hoc_an_mon.png`, `ket-qua-mau/bieu_do_thep_theo_tram.png`.

### Câu lệnh 4.5 – Liên hệ môi trường và tách diễn giải
```
Ghép số liệu khí tượng năm 2023 (trung bình nhiệt độ, độ ẩm, tổng TOW, trung bình Cl-, SO2) với A của thép theo trạm. Nhận xét yếu tố nào liên quan mạnh nhất đến A.
Trình bày thành 2 phần tách biệt: "Kết quả tính toán" và "Diễn giải khoa học đề xuất – cần nhà khoa học xác nhận". Nêu rõ giới hạn: chỉ có 3 trạm.
```
**Kết quả mong đợi:** trạm ven biển Cl⁻ ≈ 181 mg/m²·ngày, TOW ≈ 5.730 h/năm → A cao nhất; trạm đô thị SO₂ ≈ 38 mg/m²·ngày; AI phải tự nêu được "3 trạm không đủ để kết luận thống kê về tương quan" và n < 1 phù hợp với cơ chế lớp gỉ bảo vệ (diễn giải để nhà khoa học xác nhận).

---

## 5. Slide 17 – Kết quả → bài báo, báo cáo

### Câu lệnh 5.1 – Dàn ý bài báo
```
Dựa trên kết quả phân tích, lập dàn ý bài báo theo cấu trúc IMRaD cho tạp chí [Corrosion Science / Tạp chí Khoa học và Công nghệ Nhiệt đới]: tiêu đề (3 phương án), các ý chính từng phần, danh mục hình – bảng (dùng các hình đã vẽ), và 3 điểm mới (highlights).
Đối chiếu với hướng dẫn tác giả của tạp chí (giới hạn từ, số hình, cách trích dẫn) và liệt kê những điểm chưa đáp ứng.
```

### Câu lệnh 5.2 – Phản biện nội bộ
```
Đóng vai phản biện khó tính của tạp chí. Nêu 5 câu hỏi/nhược điểm lớn nhất của bản thảo (ví dụ: số trạm, thời gian phơi mẫu, cách xử lý ngoại lệ, độ tin cậy của dự báo 10 năm khi chỉ có số liệu 3 năm). Với mỗi điểm, đề xuất cách trả lời hoặc bổ sung.
```

### Câu lệnh 5.3 – Đối chiếu Mẫu 21/22
```
Lập bảng: Mục tiêu (theo thuyết minh đã duyệt) | Sản phẩm cam kết | Sản phẩm đã có | Bằng chứng (tệp, bài báo, biên bản) | Mức độ hoàn thành | Ghi chú. Đánh dấu mọi sản phẩm cam kết chưa có bằng chứng.
```

---

## 6. Slide 20 – Quy trình tự động QT-01 (bản tin công bố hằng tuần)

```
Mỗi sáng thứ Hai: tìm các công bố mới trong 7 ngày qua về "atmospheric corrosion" AND (tropical OR marine OR chloride) trên Crossref, arXiv, ScienceDirect.
Với mỗi bài: tiêu đề, tác giả, tạp chí, DOI, tóm tắt tiếng Việt 3 câu, mức độ liên quan với hướng "ăn mòn khí quyển nhiệt đới" (cao / trung bình / thấp) và lý do.
Sắp xếp theo mức độ liên quan, tối đa 10 bài.
```
(Trên Claude: dùng tính năng tác vụ định kỳ/Routine hoặc chạy thủ công rồi chụp màn hình cho Slide 20.)
