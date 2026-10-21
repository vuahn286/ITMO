# RÀ SOÁT KẾ HOẠCH THUYẾT TRÌNH v2.0 VÀ BÁO CÁO NGHIÊN CỨU

**Ngày rà soát:** 21/10/2026
**Phạm vi:**
- `Ke-hoach-thuyet-trinh-v2.md` (sau rà soát nâng lên v2.1)
- `cau-lenh-demo.md`
- `../tai-lieu/bao-cao/BAO-CAO-nghien-cuu-an-mon.md` (sau rà soát nâng lên v1.1)

**Tiêu chí:** (1) đúng nguồn, (2) dễ hiểu với nhà khoa học không chuyên AI, (3) phù hợp đối tượng và thời lượng, (4) nhất quán giữa các tệp.

---

## 1. Kết luận chung

| Tiêu chí | Đánh giá trước rà soát | Sau rà soát |
|---|---|---|
| Đúng nguồn | Tốt – các số liệu chính đã đối chiếu nguồn gốc. Còn 4 chỗ **nói chưa đúng mức** (mục 2.2) | Đã sửa |
| Dễ hiểu | **Chưa đạt** ở Slide 1–3: nhiều câu nén, dùng thuật ngữ chuyên ngành AI, toán, sinh học mà không giải nghĩa | Đã viết lại; thêm Mục 12 – Giải nghĩa thuật ngữ |
| Phù hợp đối tượng | Khá – tình huống ăn mòn gần với Trung tâm. Slide 2 quá dày (5 ví dụ khó trong 7 phút) | Đã phân bổ: nói kỹ 2 ví dụ, lướt 3 ví dụ |
| Nhất quán | Tốt; một lỗi thuật ngữ ("hàm mũ") | Đã sửa |
| Liên hệ thực tế | Demo dùng dữ liệu giả lập, chưa nối với kết quả nghiên cứu dữ liệu thật vừa làm | Đã thêm ô "Kết quả với dữ liệu thật" ở Slide 15 |

**Nhận xét về kiến thức:** nội dung phù hợp với mục tiêu "nhận thức là chính". Mạch Phần I → IV hợp lý. Các ví dụ quốc tế đều có công bố khoa học kiểm chứng được. Điểm yếu lớn nhất là **ngôn ngữ**: nhiều câu viết theo kiểu ghi chú cho người soạn, chưa phải câu nói cho người nghe.

---

## 2. Chi tiết các vấn đề và cách xử lý

### 2.1. Câu khó hiểu (viết lại bằng lời thường)

| # | Vị trí | Câu cũ | Vấn đề | Câu mới |
|---|---|---|---|---|
| 1 | Slide 1 | "AI tạo sinh đạt 53% dân số chỉ sau 3 năm – nhanh hơn máy tính cá nhân và Internet" | (a) "đạt 53% dân số" sai ngữ pháp và không rõ là dân số nào; (b) "3 năm" không rõ tính từ mốc nào; (c) "nhanh hơn" – nhanh hơn ở điểm gì; (d) người nghe có thể không biết "AI tạo sinh" là gì | "Chỉ 3 năm sau khi ra mắt đại chúng, **khoảng một nửa dân số** đã dùng AI tạo sinh – nhanh hơn tốc độ phổ cập của máy tính cá nhân và Internet." Lời nói kèm theo giải thích AI tạo sinh, mốc ChatGPT cuối 2022, và nói rõ tỷ lệ khác nhau giữa các nước. Nguyên văn nguồn: *"gần 53% mức phổ cập trong dân số trong vòng 3 năm kể từ khi ra mắt đại chúng"* (AI Index 2026, Chương 4) |
| 2 | Slide 1 | "độ dài công việc AI tự hoàn thành (đo bằng thời gian chuyên gia cần) tăng gấp đôi khoảng mỗi 7 tháng" | Câu trừu tượng, người nghe không hình dung được | "AI tự làm được những việc mà chuyên gia cần: **vài giây** (2019) → **gần 1 giờ** (đầu 2025) → **khoảng 12 giờ** (đầu 2026) → **hơn 16 giờ** (giữa 2026). Từ 2024, cứ khoảng **3–4 tháng** độ dài này lại tăng gấp đôi." (METR: GPT-2 ≈ 2 giây; Claude 3.7 Sonnet ≈ 50–59 phút; mô hình công khai mạnh nhất 02–03/2026 ≈ 12 giờ; Claude Mythos Preview 05/2026 ≥ 16 giờ; gấp đôi mỗi 105 ngày cho mô hình từ 2024) |
| 3 | Slide 1 | "đạt chuẩn huy chương vàng IMO 2025" | "IMO" không phải ai cũng biết | "AI giải được 5/6 bài thi Olympic Toán quốc tế 2025 – đạt mức huy chương vàng" |
| 4 | Slide 2 ① | "9/353 bài toán Erdős… 44/492 giả thuyết OEIS… kiểm chứng hình thức bằng Lean" | Ba thuật ngữ toán học/tin học liền nhau | Thêm giải thích: bài toán mở do Paul Erdős để lại; "bách khoa toàn thư dãy số"; "trọng tài máy" kiểm tra từng bước |
| 5 | Slide 2 ② | "cơ chế cf-PICI 'mượn đuôi phage'" | Thuật ngữ vi sinh hẹp | "Một loại đoạn gen di động tự tạo 'vỏ' nhưng 'mượn đuôi' của nhiều loại virus để xâm nhập nhiều loài vi khuẩn – giải thích vì sao gen kháng kháng sinh lan giữa các loài" |
| 6 | Slide 2 ③ | "silmitasertib chỉ khuếch đại trình diện kháng nguyên khi có interferon" | Thuật ngữ miễn dịch học | "Thuốc có sẵn, dùng cùng interferon liều thấp, giúp tế bào ung thư 'lộ diện' trước hệ miễn dịch; mới thử trên tế bào" |
| 7 | Slide 2 ④ | "tiết kiệm trung bình 0,7% tài nguyên tính toán" | "Tiết kiệm" dễ hiểu nhầm là giảm chi phí | "Thu hồi trung bình 0,7% năng lực tính toán trước đó bị bỏ phí" (đúng nguyên văn "recovers… stranded") |
| 8 | Slide 3 | "bộ embedding toàn cầu độ phân giải 10 m"; "huấn luyện trên 4,2 triệu chuỗi thời gian HLS" | Thuật ngữ học máy | "Mỗi ô 10 m × 10 m trên Trái Đất được AI tóm tắt thành một 'dấu vân tay số'"; nêu ứng dụng cụ thể (lũ, cháy rừng, cây trồng) |
| 9 | Slide 3 | "AIFS… cải thiện tới ~20% với đường đi bão" | Không rõ cải thiện cái gì; không rõ ECMWF là ai | "Mô hình dự báo thời tiết bằng AI của Trung tâm Dự báo Thời tiết Hạn vừa châu Âu… dự báo đường đi bão chính xác hơn tới khoảng 20%" |
| 10 | Slide 11, 15 | "C = A·tⁿ"; "n < 1 phù hợp với cơ chế lớp gỉ bảo vệ"; "z-score/MAD" | Công thức, thuật ngữ thống kê không giải nghĩa | Thêm giải nghĩa A, n tại Slide 11; giải thích z-score/MAD bằng một câu tại Slide 15 |

### 2.2. Độ chính xác và cách nói đúng mức

| # | Vị trí | Vấn đề | Đã sửa thành |
|---|---|---|---|
| 1 | Slide 2 – tiêu đề | "Các nhà khoa học Google…" – nhưng ví dụ ② do Imperial College, ③ do Đại học Yale chủ trì | "Google **và** các nhà khoa học dùng AI…" |
| 2 | Slide 2 ② | Câu "GS. Penadés nói…" – nguồn gốc của câu nói chưa xác định chắc (*Nature* gán cho đồng tác giả T. Costa; báo chí gán cho Penadés) | "Nhóm nghiên cứu cho biết…" |
| 3 | Slide 2 ⑤ | Không nói rõ kết quả COVID-19 là **đánh giá hồi cứu** (mô hình "Google Retrospective"), dễ hiểu nhầm là AI dự báo trực tiếp trong mùa dịch | Ghi rõ "trong đánh giá hồi cứu" và "trên một bảng xếp hạng công khai" |
| 4 | Mục 4.1 | "C = A·tⁿ (dạng **hàm mũ**…)" – sai thuật ngữ toán: A·tⁿ là **hàm lũy thừa** | "dạng hàm lũy thừa" |
| 5 | Slide 1 | Chỉ nêu Google đạt IMO – chưa trung lập công cụ (OpenAI cũng công bố kết quả tương tự) | Ghi cả hai |
| 6 | Slide 3 | AlphaFold chưa có mã nguồn trong bảng căn cứ | Thêm N4 |
| 7 | Mục 6 | "Luật Bảo vệ bí mật nhà nước 2018" thiếu số hiệu | "số 29/2018/QH14" |
| 8 | Slide 1 | Số liệu METR dừng ở đầu 2025 – đã cũ so với thời điểm thuyết trình (10/2026); bản v2.0 còn ghi nhầm câu "4 tháng từ 2023" của v1 là sai | Cập nhật đến 05/2026 (≈ 12 giờ → ≥ 16 giờ; gấp đôi mỗi 3–4 tháng từ 2024); đính chính nhận định về v1 |

### 2.3. Phù hợp đối tượng và thời lượng

| Vấn đề | Đề xuất (đã đưa vào v2.1) |
|---|---|
| Slide 2 có 5 ví dụ từ 4 lĩnh vực khó (toán, vi sinh, ung thư, tin học) trong 7 phút | Nói kỹ ② (AI đề xuất giả thuyết) và ⑤ (AI viết – chạy mã xử lý dữ liệu) – gần công việc của Trung tâm nhất; ①, ③, ④ mỗi ví dụ ≤ 40 giây |
| Đối tượng là nhà khoa học vật liệu, môi trường, y sinh – không chuyên AI | Mục 12 – bảng giải nghĩa 15 thuật ngữ; nguyên tắc "trên slide dùng lời thường" |
| Demo chỉ dùng dữ liệu giả lập – có thể bị hỏi "với dữ liệu thật thì sao?" | Ô "Kết quả với dữ liệu thật" (Slide 15): 387 số đo, lỗi đơn vị trong dữ liệu công bố, mô hình quốc tế dự đoán thấp ở Việt Nam 31% |

### 2.4. Những điểm giữ nguyên (đã kiểm tra, phù hợp)

- Cấu trúc 4 phần, 25 slide, 120 phút; thông điệp từng phần.
- Năm ví dụ Slide 2 – đều có công bố trên *Science*, *Cell*, *Nature* hoặc bioRxiv, DOI ở Mục 7.1.
- Tình huống A, dữ liệu demo, bộ câu lệnh, kết quả chạy thử – số liệu khớp giữa kế hoạch, `cau-lenh-demo.md` và `ket-qua/demo-gia-lap/`.
- Căn cứ pháp lý Việt Nam (Luật 134/2025/QH15, Luật 91/2025/QH15).

---

## 3. Việc còn lại trước buổi thuyết trình

| # | Việc | Ghi chú |
|---|---|---|
| 1 | Mở trực tiếp các DOI Mục 7.1, nhất là G1 (*Science*, 08/10/2026) | Rà soát này đối chiếu qua công cụ tìm kiếm |
| 2 | Kiểm tra số liệu SWE-bench (Phụ lục) trong bản gốc AI Index 2026 | Hiện mới có nguồn thứ cấp |
| 3 | Điền N14 – chính sách dữ liệu của 5 công cụ AI | Kiểm tra trong tuần thuyết trình |
| 4 | Ngưỡng ISO 9223 cho đồng, nhôm từ cấp C4 | Cần bản gốc tiêu chuẩn |
| 5 | URL các bộ Skill khoa học mở (N17); mã số arXiv 2609.00065 (N18) | Từ v1 |
| 6 | Xác minh nguồn gốc dữ liệu Việt Nam ("Lien et al.") và Nga ("Mikhailov et al.") trong báo cáo nghiên cứu | Nếu dùng ô "Kết quả với dữ liệu thật" |
| 7 | **Tập nói thử Slide 1–3 với 1–2 đồng nghiệp không chuyên AI** – câu nào họ hỏi lại thì viết lại | Cách kiểm tra "dễ hiểu" hiệu quả nhất |

---

## 4. Nguồn đã dùng khi rà soát

- Stanford HAI, AI Index Report 2026 – Chương 4 Kinh tế: https://hai.stanford.edu/assets/files/ai_index_report_2026_chapter_4_economy.pdf
- METR (2025), Measuring AI Ability to Complete Long Tasks: https://arxiv.org/abs/2503.14499
- Aygün E. et al. (2026), *Nature* – ERA; preprint arXiv:2509.06503 (mô hình "Google Retrospective" trên bảng xếp hạng COVID-19 Forecast Hub)
- Imperial College London (02/2025); *Nature* (2026) – tin về AI co-scientist
- DeepMind blog AlphaEvolve (05/2025) – "recovers, on average, 0.7% of Google's worldwide compute resources"
