# DANH SÁCH SLIDE ĐỂ CHỈNH SỬA VÀ DUYỆT

**Bài thuyết trình:** AI Agent và sự chuyển đổi phương thức nghiên cứu khoa học
**Đối tượng:** Cán bộ, nhà khoa học Trung tâm Nhiệt đới Việt – Nga · **Thời lượng:** 120 phút · **Số slide:** 20 slide trình bày + 4 phụ lục + trang bìa
**Căn cứ:** Kế hoạch v2.1 (`Ke-hoach-thuyet-trinh-v2.md`), cập nhật 21/10/2026 · **Bản v2.2:** bỏ slide ví dụ Google (chuyển xuống Phụ lục B); tách slide "Năm quyết định" – 5 quyết định gộp vào Slide 17, căn cứ pháp lý gộp vào Slide 7, thông điệp Phần III chuyển sang Slide 15. **Từ v2.2, tệp này là bố cục slide chính thức.**

---

## Cách dùng tệp này

Mỗi slide gồm các phần:
- **Chữ trên slide** – nội dung xuất hiện trên màn hình. Sửa trực tiếp vào đây.
- **Hình ảnh** – hình hoặc biểu đồ cần chuẩn bị.
- **Lời nói** – nội dung người trình bày nói, không hiện trên slide.
- **Nguồn** – mã căn cứ, tra ở Mục 7 của kế hoạch.
- **Duyệt** – đánh dấu `[x]` vào một ô, ghi ý kiến vào dòng "Ghi chú".

Trạng thái: `[ ] Duyệt` · `[ ] Sửa theo ghi chú` · `[ ] Bỏ`

---

## TỔNG QUAN

| # | Tên slide | Phần | Thời lượng | Duyệt |
|---|---|---|---|---|
| – | Trang bìa | – | – | [ ] |
| 1 | AI đang phát triển nhanh đến mức nào? | I | 4′ | [ ] |
| 2 | AI trong các lĩnh vực khoa học: quốc tế và Việt Nam | I | 5′ | [ ] |
| 3 | Năng lực cốt lõi của AI: từ trả lời đến thực hiện | I | 5′ | [ ] |
| 4 | Phương thức nghiên cứu đang thay đổi | I | 4′ | [ ] |
| 5 | Công việc nào cần chatbot, công việc nào cần AI Agent? | II | 5′ | [ ] |
| 6 | Các công cụ AI và vai trò khác nhau | II | 6′ | [ ] |
| 7 | Một cách giao việc chung cho các công cụ AI | II | 6′ | [ ] |
| 8 | Tổ chức một không gian làm việc nghiên cứu | II | 7′ | [ ] |
| 9 | Skill, Subagent và hệ thống nhiều Agent | II | 7′ | [ ] |
| 10 | Một nhiệm vụ khoa học đi qua AI Agent như thế nào? | III | 3′ | [ ] |
| 11 | Từ tài liệu đến khoảng trống nghiên cứu | III | 7′ | [ ] |
| 12 | Từ câu hỏi nghiên cứu đến thuyết minh – DEMO 1 | III | 10′ | [ ] |
| 13 | Tổ chức công việc, tiến độ và kinh phí | III | 5′ | [ ] |
| 14 | Từ dữ liệu thô đến kết quả: nhà khoa học dùng AI viết và chạy mã – DEMO 2 | III | 10′ | [ ] |
| 15 | Từ kết quả đến bài báo và báo cáo tổng hợp | III | 6′ | [ ] |
| 16 | Skill và khoa học mở: nền móng của tự động hóa | IV | 4′ | [ ] |
| 17 | Từ hỗ trợ từng bước đến tự động hóa toàn trình, và năm quyết định của nhà khoa học | IV | 6′ | [ ] |
| 18 | Bản đồ quy trình tự động của Trung tâm | IV | 5′ | [ ] |
| 19 | Lộ trình triển khai và kết luận | IV | 3′ | [ ] |
| 20 | Trao đổi và thảo luận | – | 12′ | [ ] |
| 21 | Phụ lục A: AI lập trình (không trình bày) | – | – | [ ] |
| 22 | Phụ lục B: Ví dụ Google và các nhà khoa học dùng AI (không trình bày – dự phòng khi được hỏi) | – | – | [ ] |
| 23 | Phụ lục C: Nguồn tham khảo (không trình bày) | – | – | [ ] |
| 24 | Phụ lục D: Dự án và bộ Skill khoa học mở (không trình bày) | – | – | [ ] |
| | **Tổng** | | **120′** = 108′ trình bày + 12′ thảo luận. Khi tập dượt, nói trong khoảng 100′ để còn dự phòng cho demo. | |

---

## TRANG BÌA

**Chữ trên slide:**
> **AI AGENT VÀ SỰ CHUYỂN ĐỔI PHƯƠNG THỨC NGHIÊN CỨU KHOA HỌC**
> Người trình bày: ______________________
> Trung tâm Nhiệt đới Việt – Nga · ____ / ____ / 2026

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

# PHẦN I. TỔNG QUAN (18 phút)

---

## Slide 1 – AI đang phát triển nhanh đến mức nào? (4′)

**Chữ trên slide:** 3 ô số liệu lớn

| Ô | Số lớn | Dòng chữ dưới số |
|---|---|---|
| 1 | **≈ 1/2** | Chỉ 3 năm sau khi ra mắt đại chúng, khoảng một nửa dân số đã dùng AI tạo sinh – nhanh hơn tốc độ phổ cập của máy tính cá nhân và Internet |
| 2 | **5/6 bài** | AI giải được 5/6 bài thi Olympic Toán quốc tế 2025 – đạt mức huy chương vàng |
| 3 | **Vài giây → hơn 16 giờ** | AI tự làm được những việc mà chuyên gia cần: vài giây (2019) → gần 1 giờ (đầu 2025) → khoảng 12 giờ (đầu 2026) → hơn 16 giờ (giữa 2026). Từ 2024, cứ khoảng 3–4 tháng lại tăng gấp đôi |

> *Câu chốt (cuối slide):* Chỉ trong vài năm, AI đi từ trả lời câu hỏi đến tự thực hiện những công việc kéo dài nhiều giờ.

**Hình ảnh:** biểu đồ METR (trục tung logarit, từ giây đến giờ) – hình chính của slide.

**Lời nói:**
- AI tạo sinh là loại AI viết được văn bản, vẽ hình… như ChatGPT, Gemini, Claude. ChatGPT ra mắt cuối 2022; khoảng 3 năm sau, theo Đại học Stanford, mức phổ cập đạt khoảng 53% dân số. Tỷ lệ chênh lệch lớn giữa các nước.
- Olympic Toán quốc tế là kỳ thi cho học sinh giỏi toán nhất thế giới; AI viết lời giải bằng ngôn ngữ tự nhiên, được chấm như thí sinh (35/42 điểm). Cả Google và OpenAI đều công bố kết quả này.
- Độ dài công việc đo bằng thời gian một chuyên gia cần để làm xong; AI được tính là "làm được" nếu thành công ít nhất một nửa số lần. "Làm được một nửa số lần" không có nghĩa là giao hẳn việc 16 giờ cho AI. 16 giờ cũng là giới hạn đo của bộ bài kiểm tra hiện tại.

**Lưu ý:** không viết "53% dân số thế giới"; không nêu con số lớn hơn 16 giờ. Xem lại metr.org/time-horizons ngay trước ngày thuyết trình.

**Nguồn:** N1 (AI Index 2026), N2 (IMO 2025), N3 (METR)

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 2 – AI trong các lĩnh vực khoa học: quốc tế và Việt Nam (5′)

**Chữ trên slide:**

| Lĩnh vực | Ví dụ | Gần với Trung tâm |
|---|---|---|
| Viễn thám | **Prithvi-EO-2.0** (NASA – IBM, mã nguồn mở): nhận dạng lũ, cháy rừng, cây trồng từ ảnh vệ tinh · **AlphaEarth** (Google): lập bản đồ toàn cầu ô 10 m với rất ít mẫu thực địa | Rừng, sử dụng đất, sinh thái |
| Khí tượng | **AIFS** (Trung tâm Dự báo Thời tiết châu Âu): dự báo thời tiết bằng AI, chạy nghiệp vụ từ 02/2025; dự báo đường đi bão chính xác hơn tới ~20% | Môi trường, khí hậu nhiệt đới |
| Robotics | **Gemini Robotics**: robot học thao tác mới sau ~100 lần người làm mẫu | Tự động hóa thí nghiệm |
| Sinh học | **AlphaFold**: dự đoán cấu trúc 3D của protein – Nobel Hóa học 2024 | Y sinh nhiệt đới |
| Vật liệu | **GNoME**: đề xuất 2,2 triệu cấu trúc tinh thể mới · **A-Lab**: phòng thí nghiệm robot tự tổng hợp 41 hợp chất mới trong 17 ngày | Vật liệu, ăn mòn, độ bền |

> **Việt Nam:** Luật Trí tuệ nhân tạo số 134/2025/QH15, hiệu lực từ 01/3/2026.
> *Câu chốt:* AI đang trở thành một thành phần của hạ tầng nghiên cứu.

**Hình ảnh:** mỗi lĩnh vực một hình nhỏ (ảnh vệ tinh, bản đồ bão, robot, protein, tinh thể).

**Lời nói:** hỏi người nghe: "Lĩnh vực nào gần với công việc của anh chị nhất?"; nhấn mạnh Prithvi là mã nguồn mở – Trung tâm có thể dùng ngay.

**Nguồn:** N4–N10

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 3 – Năng lực cốt lõi của AI: từ trả lời đến thực hiện (5′)

**Chữ trên slide:**

Sáu năng lực cốt lõi:
1. Đọc và tổng hợp hàng trăm tài liệu trong một lần làm việc
2. Suy luận, tự chia nhiệm vụ lớn thành các bước
3. **Dùng công cụ: tìm kiếm, đọc – tạo tệp, viết và chạy mã**
4. Làm việc với văn bản, bảng số liệu, hình ảnh, biểu đồ
5. Thành thạo tiếng Việt, tiếng Nga, tiếng Anh
6. Đóng gói quy trình thành Skill để dùng lại; nhiều trợ lý phối hợp

| | Chatbot AI | AI Agent |
|---|---|---|
| Đầu vào | Một câu hỏi | Một nhiệm vụ có mục tiêu |
| Lập kế hoạch | Hạn chế | Tự lập và điều chỉnh |
| Công cụ | Ít | Tìm kiếm, chạy mã, làm việc với tệp |
| Kiểm tra kết quả | Người dùng tự làm | Tự kiểm tra từng bước |
| Chi phí – thời gian | Thấp | Cao hơn |

> *Ô nhỏ:* Lập trình là lĩnh vực AI Agent phát triển sớm nhất – 84% lập trình viên đang dùng hoặc dự định dùng AI. Nhà khoa học không cần giỏi lập trình vẫn có thể yêu cầu AI viết và chạy mã xử lý dữ liệu → Slide 14.
> *Câu chốt:* Không phải công việc nào cũng cần Agent.

**Hình ảnh:** sơ đồ tiến hóa: AI phân tích → AI tạo sinh → AI dùng công cụ → AI Agent.

**Lời nói:** năng lực 5 là lợi thế riêng của Trung tâm Việt – Nga. Phần AI lập trình nói không quá 1 phút.

**Nguồn:** N11

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 4 – Phương thức nghiên cứu đang thay đổi (4′)

**Chữ trên slide:**

| Trước đây | Hiện nay | Ví dụ |
|---|---|---|
| Tìm kiếm thủ công | Tổng hợp bằng chứng có hệ thống | AI co-scientist (Google) đọc tài liệu, đề xuất giả thuyết – kể kỹ ở Phần III |
| Thao tác riêng lẻ | Quy trình liên tục | ERA (Google): AI viết mã → chạy → chấm điểm → cải tiến – kể kỹ ở Phần III |
| Câu lệnh dùng một lần | Quy trình mẫu (Skill) dùng lại | Thư viện Skill khoa học mở |
| Một chatbot | Nhiều trợ lý phối hợp | Co-scientist: các trợ lý đề xuất, phản biện, xếp hạng giả thuyết |

> **Nhà khoa học dẫn dắt:** câu hỏi, phương pháp, diễn giải và công bố.
> **Thông điệp Phần I:** AI không thay thế nhà khoa học; AI đang thay đổi cách nhà khoa học đặt giả thuyết, xử lý dữ liệu và kiểm chứng kết quả.

**Hình ảnh:** mũi tên "trước → nay" cho 4 dòng.

**Nguồn:** G2, G5

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

# PHẦN II. LỰA CHỌN VÀ SỬ DỤNG CÔNG CỤ AI PHÙ HỢP (31 phút)

---

## Slide 5 – Công việc nào cần chatbot, công việc nào cần AI Agent? (5′)

**Chữ trên slide:** bậc thang 5 bậc – càng lên cao càng phức tạp, tốn thời gian và chi phí

| Bậc | Loại việc | Ví dụ (tình huống ăn mòn) | Công cụ phù hợp |
|---|---|---|---|
| 1 | Hỏi – đáp | "Cấp ăn mòn C4 theo ISO 9223 nghĩa là gì?" | Chatbot |
| 2 | Phân tích một tài liệu | Tóm tắt một bài báo về ăn mòn thép ven biển | Chatbot |
| 3 | Tổng hợp nhiều nguồn | Ma trận bằng chứng từ 15 bài báo | Chatbot có dự án / nghiên cứu chuyên sâu |
| 4 | Xử lý nhiều tệp | Làm sạch và phân tích 2 tệp số liệu | AI Agent |
| 5 | Chuỗi nhiệm vụ | Dữ liệu → mô hình → biểu đồ → bản thảo bài báo | AI Agent |

> *Câu chốt:* Chọn đúng bậc – không dùng "dao mổ trâu giết gà".

**Hình ảnh:** bậc thang, mỗi bậc một biểu tượng.

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 6 – Các công cụ AI và vai trò khác nhau (6′)

**Chữ trên slide:** *(cập nhật 10/2026)*

| Công cụ | Thế mạnh | Ví dụ công việc | Dữ liệu có bị dùng để huấn luyện? |
|---|---|---|---|
| Perplexity | Tìm thông tin trên web, có dẫn nguồn | Tìm nhanh tài liệu mới | **☐ cần điền** |
| NotebookLM | Hỏi – đáp trên bộ tài liệu tự chọn | Hỏi đáp trên 50 bài báo đã tải | **☐ cần điền** |
| ChatGPT | Tổng hợp, phân tích, viết; nghiên cứu chuyên sâu | Nghiên cứu chuyên sâu một chủ đề | **☐ cần điền** |
| Gemini | Gắn với hệ sinh thái Google | Tổng hợp tài liệu trên Drive | **☐ cần điền** |
| Claude | Làm việc với tệp, chuỗi nhiệm vụ trong dự án | Soạn thuyết minh từ bộ hồ sơ | **☐ cần điền** |

**Lời nói:** chính sách dữ liệu thay đổi thường xuyên, phân biệt theo gói miễn phí và gói trả phí.

**Việc phải làm:** điền cột cuối từ điều khoản chính thức của từng công cụ trong tuần thuyết trình (N14).

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 7 – Một cách giao việc chung cho các công cụ AI (6′)

**Chữ trên slide:** quy trình 5 bước

1. **Xác định nhiệm vụ** – làm gì, để làm gì
2. **Cung cấp dữ liệu** – theo quy tắc xanh / vàng / đỏ
3. **Quy định đầu ra** – dạng bảng, văn bản, biểu đồ, độ dài
4. **Yêu cầu dẫn nguồn, lưu mã** – để kiểm tra và tái lập
5. **Kiểm tra và xác nhận** – nhà khoa học duyệt

**Khung nhỏ – quy tắc dữ liệu:**
🟢 **Xanh:** đã công bố, công khai, giả lập → dùng được với AI trực tuyến
🟡 **Vàng:** nội bộ chưa công bố → chỉ gói có cam kết không huấn luyện, đã loại thông tin định danh, có phê duyệt
🔴 **Đỏ:** bí mật nhà nước, quân sự, dữ liệu cá nhân nhạy cảm → không đưa lên AI trực tuyến

> *Căn cứ pháp lý (dòng chân slide):* Luật Trí tuệ nhân tạo 134/2025/QH15 · Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 · Luật Bảo vệ bí mật nhà nước 29/2018/QH14 · quy định của Trung tâm và Bộ Quốc phòng

**Ví dụ minh họa:** câu lệnh phân tích dữ liệu ăn mòn (Câu lệnh 4.3), đánh dấu từng phần tương ứng với 5 bước.

**Lời nói:** "Quyết định dữ liệu nào được đưa lên AI là của nhà khoa học và người có thẩm quyền – không phải của AI." Lồng ghép liêm chính khoa học, sở hữu trí tuệ, trách nhiệm giải trình.

**Lưu ý:** quy tắc xanh / vàng / đỏ phải được bộ phận bảo mật xác nhận trước khi trình bày.

**Nguồn:** N10, N12

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 8 – Tổ chức một không gian làm việc nghiên cứu (7′)

**Chữ trên slide:**
- Đưa tài liệu, biểu mẫu, dữ liệu vào **một không gian dự án**
- Viết **hướng dẫn chung** một lần – AI áp dụng cho mọi câu hỏi trong dự án
- Giao nhiệm vụ nhiều bước; yêu cầu tạo sản phẩm (văn bản, bảng, biểu đồ)
- Tiếp tục chỉnh sửa trên kết quả

> *Công cụ tương đương:* Claude Projects ↔ ChatGPT Projects ↔ Gemini Gems ↔ NotebookLM

**Hình ảnh:** ảnh chụp dự án mẫu "Demo – Ăn mòn khí quyển nhiệt đới" (dữ liệu xanh).

**Lời nói:** đọc to đoạn hướng dẫn chung của dự án mẫu (Mục 0 trong `cau-lenh-demo.md`).

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 9 – Skill, Subagent và hệ thống nhiều Agent (7′)

**Chữ trên slide:**
- **Skill:** quy trình mẫu đóng gói sẵn (hướng dẫn + biểu mẫu + mã), AI tự dùng lại
- **Subagent:** trợ lý được giao một việc chuyên biệt
- **Nhiều Agent:** nhiều trợ lý phối hợp như một nhóm

> *Ví dụ thật:* AI co-scientist của Google – các trợ lý đề xuất, tranh luận, xếp hạng giả thuyết.
> **Thông điệp Phần II:** Công cụ tốt nhất là công cụ phù hợp với nhiệm vụ, dữ liệu, chi phí và mức độ kiểm soát cần thiết.

**Hình ảnh:** sơ đồ "nhóm nghiên cứu ảo": nhà khoa học ở vị trí chủ nhiệm; các trợ lý tìm tài liệu → phân tích dữ liệu → kiểm tra biểu mẫu → rà soát báo cáo.

**Nguồn:** G2

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

# PHẦN III. AI AGENT TRONG VÒNG ĐỜI NHIỆM VỤ KHOA HỌC (41 phút)

> Toàn bộ số liệu demo ở Phần III là **dữ liệu giả lập** – ghi rõ trên mọi slide có số liệu.

---

## Slide 10 – Một nhiệm vụ khoa học đi qua AI Agent như thế nào? (3′)

**Chữ trên slide:**
> **Tình huống:** Đánh giá ăn mòn khí quyển của thép CT3, kẽm, đồng, nhôm tại 3 trạm thử nghiệm (ven biển, đô thị, nội địa); xây dựng mô hình dự báo và phân cấp ăn mòn theo ISO 9223.
> 3 trạm × 4 kim loại × 7 mốc thu mẫu × 3 mẫu lặp = **252 mẫu** · số liệu khí tượng 36 tháng · *dữ liệu giả lập*

**Hình ảnh (chính):** sơ đồ vòng đời: Tài liệu → Khoảng trống → Thuyết minh → Tiến độ – kinh phí → Dữ liệu – kết quả → Bài báo – báo cáo; mỗi bước có dấu ✅ "nhà khoa học xác nhận" và số slide (11–15).

**Lời nói:** "Trong 30 phút tới, chúng ta đi hết vòng đời của một nhiệm vụ giả định – dữ liệu giả lập nhưng câu lệnh và cách làm là thật, anh chị về chạy lại được ngay." Giải nghĩa C = A·tⁿ: A là lượng kim loại mất trong năm đầu; n < 1 nghĩa là lớp gỉ che chắn dần.

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 11 – Từ tài liệu đến khoảng trống nghiên cứu (7′)

**Chữ trên slide:**
- 🌍 **Ví dụ thật:** AI co-scientist – nhiều trợ lý đề xuất, phản biện, xếp hạng giả thuyết
- ⌨ **Câu lệnh:**
  > Từ các bài báo trong dự án, lập ma trận bằng chứng (tác giả – năm, địa điểm, kim loại, thời gian phơi mẫu, biến môi trường, mô hình, kết luận, hạn chế). Chỉ ra điểm chưa thống nhất và 3 khoảng trống cho điều kiện Việt Nam, mỗi khoảng trống dẫn chứng ít nhất 2 bài.
- 📂 **Dữ liệu:** 10–15 bài báo truy cập mở về ăn mòn khí quyển
- ✅ **Nhà khoa học xác nhận:** nguồn có thật; khoảng trống có giá trị

**Hình ảnh:** ảnh chụp ma trận bằng chứng và 3 khoảng trống có điểm phản biện.

**Lời nói:** "Câu lệnh 1.3 cho AI đóng vai 3 phản biện độc lập – phiên bản thu nhỏ của AI co-scientist." "Mỗi DOI tôi đều bấm thử – kiểm tra nguồn là việc của nhà khoa học."

**Nguồn:** G2 · Câu lệnh 1.1–1.3

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 12 – Từ câu hỏi nghiên cứu đến thuyết minh – DEMO 1 (10′)

**Chữ trên slide:**
- Khoảng trống → tính cấp thiết, mục tiêu, nội dung, phương pháp, sản phẩm
- ⌨ **Câu lệnh (trình diễn trực tiếp):**
  > Lập bảng đối chiếu: Mục tiêu → Nội dung → Phương pháp → Sản phẩm → Chỉ tiêu. Đánh dấu ⚠ mọi chỗ không khớp; kiểm tra số mẫu (3 × 4 × 7 × 3 = ?).
- 📊 **Kết quả mong đợi:** AI tính đúng 252 mẫu; chỉ ra chỗ chưa khớp (ví dụ: mục tiêu "bản đồ phân vùng" nhưng chỉ có 3 trạm)
- Mẫu 01A, 07, 08 là **sản phẩm đầu ra** của tư duy khoa học
- ✅ **Nhà khoa học xác nhận:** tính mới, tính khả thi, chỉ tiêu

**Hình ảnh:** ảnh chụp bảng đối chiếu có dấu ⚠.

**Lời nói:** "Hội đồng thường bắt lỗi đúng ở những chỗ này. Để AI rà trước giúp ta sửa sớm – nhưng chọn mục tiêu nào là quyết định của chủ nhiệm."

**Demo:** trực tiếp ~2 phút (Câu lệnh 2.2); các bước khác dùng ảnh chụp.

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 13 – Tổ chức công việc, tiến độ và kinh phí (5′)

**Chữ trên slide:**
- ⌨ **Câu lệnh:** Đọc kế hoạch công việc, vẽ sơ đồ Gantt, tính tổng kinh phí, kiểm tra logic trình tự; liệt kê bất hợp lý và đề xuất điều chỉnh
- 📊 **AI phát hiện 3 bất hợp lý:**
  1. Thu mẫu bắt đầu trước khi lắp xong giá phơi mẫu
  2. Quan trắc khí tượng kết thúc trước mốc thu mẫu cuối
  3. Công bố bắt đầu khi mô hình chưa xong (chấp nhận nếu là bài báo giữa kỳ)
- ✅ **Xác nhận:** số liệu tài chính do cán bộ tài chính xác nhận

**Hình ảnh:** `ket-qua-mau/so_do_gantt.png` (tổng kinh phí 1.350 triệu đồng – *giả lập*).

**Lời nói:** "Ba lỗi này tôi cố ý cài vào – AI tìm ra trong vài giây."

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 14 – Từ dữ liệu thô đến kết quả: nhà khoa học dùng AI viết và chạy mã – DEMO 2 (10′)

**Chữ trên slide:**
- 🌍 **Ví dụ thật:** ERA (Google, *Nature* 2026) – AI tự viết, chạy, chấm điểm, cải tiến mã
- ⌨ **Câu lệnh (trình diễn trực tiếp):** rà soát dữ liệu → tính tổn thất và mô hình C = A·tⁿ → vẽ biểu đồ
- 📊 **Kết quả (dữ liệu giả lập):**
  - Phát hiện đủ **14/14 lỗi** cài sẵn (trùng dòng, ô trống, sai định dạng, giá trị vô lý, ngoại lệ…)
  - Thép CT3: ven biển **C4** · đô thị **C3** · nội địa **C2** (R² > 0,99)
- 💡 **Bài học:** AI viết mã rất nhanh – nhưng chọn phương pháp phù hợp với thiết kế thí nghiệm là việc của người làm chuyên môn
- 📌 **Với dữ liệu thật:** 387 số đo thực địa đã công bố (có 12 trạm Việt Nam) – AI phát hiện lỗi đơn vị trong bộ dữ liệu công bố; mô hình quốc tế dự đoán thấp hơn thực đo ở Việt Nam khoảng 31%

**Hình ảnh:** `ket-qua-mau/bieu_do_dong_hoc_an_mon.png`; (tùy chọn) `nghien-cuu-an-mon/ket-qua/do_vs_du_doan.png`.

**Lời nói – bài học thật:** "Lần chạy đầu, mã dùng phương pháp thống kê z-score/MAD – vốn cần nhiều số liệu – để tìm ngoại lệ. Kết quả: đánh dấu nhầm 20 giá trị bình thường, bỏ sót đúng lỗi cần tìm, vì mỗi nhóm chỉ có 3 mẫu lặp. Đổi sang quy tắc 'lệch quá 30% so với 2 mẫu còn lại' thì mới đúng." Kết thúc bằng ô dữ liệu thật: "Đây là lý do số liệu trạm của Trung tâm có giá trị lớn."

**Demo:** trực tiếp ~3 phút (Câu lệnh 4.2 → 4.3 → 4.4).

**Nguồn:** G5 · `nghien-cuu-an-mon/BAO-CAO.md`

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 15 – Từ kết quả đến bài báo và báo cáo tổng hợp (6′)

**Chữ trên slide:**
- 🌍 Các công trình dùng AI vừa nêu (AI co-scientist, ERA) đều do **nhà khoa học đứng tên và chịu trách nhiệm**; AI không được đứng tên tác giả, việc sử dụng AI phải được khai báo
- ⌨ **Câu lệnh:**
  1. Lập dàn ý bài báo; đối chiếu hướng dẫn tác giả của tạp chí
  2. Đóng vai phản biện khó tính: 5 nhược điểm lớn nhất và cách trả lời
  3. Bảng đối chiếu: Mục tiêu – Sản phẩm cam kết – Sản phẩm đã có – Bằng chứng (Mẫu 21, 22)
- ✅ **Xác nhận:** nội dung khoa học, trích dẫn, quyền tác giả, khai báo việc sử dụng AI

**Hình ảnh:** ảnh chụp dàn ý và danh sách câu hỏi phản biện.

> **Thông điệp Phần III:** AI Agent nối tài liệu, dữ liệu, biểu mẫu và sản phẩm thành một quá trình liên tục; các quyết định khoa học thuộc về nhà nghiên cứu.

**Lời nói:** "Để AI phản biện mình trước khi gửi bài – rẻ hơn rất nhiều so với một lần bị từ chối."

**Nguồn:** N15 (cần trích nguyên văn chính sách của tạp chí)

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

# PHẦN IV. SKILL, KHOA HỌC MỞ VÀ TỰ ĐỘNG HÓA (18 phút)

---

## Slide 16 – Skill và khoa học mở: nền móng của tự động hóa (4′)

**Chữ trên slide:**
- **Skill** = hướng dẫn quy trình + tri thức chuyên môn + biểu mẫu + mã; AI tự dùng khi cần, cho kết quả nhất quán
- **Vì sao quan trọng:** biến kinh nghiệm cá nhân thành tài sản chung · chuẩn hóa chất lượng · là "viên gạch" của quy trình tự động
- **Thư viện Skill khoa học mở:** AI4S, AIPOCH, K-Dense Scientific Agent Skills, CES Global
- **Phù hợp khoa học mở:** nguyên tắc FAIR (dễ tìm, dễ truy cập, liên thông, tái sử dụng) · tái lập · minh bạch
- **Chiến lược:** Kế thừa → Bản địa hóa (biểu mẫu, thuật ngữ Việt – Nga – Anh) → Chia sẻ nội bộ

> *Ví dụ:* Skill "Kiểm tra chất lượng dữ liệu cân mẫu ăn mòn" – đóng gói câu lệnh ở Slide 14, đã sửa bài học về 3 mẫu lặp → lần sau ai chạy cũng đúng ngay.

**Hình ảnh:** sơ đồ "Thư viện Skill mở → Bản địa hóa → Thư viện Skill của Trung tâm".

**Việc phải làm:** bổ sung URL và số lượng Skill của từng thư viện (N17).

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 17 – Từ hỗ trợ từng bước đến tự động hóa toàn trình, và năm quyết định của nhà khoa học (6′)

**Chữ trên slide:**

| Mức | Mô tả | Ví dụ |
|---|---|---|
| 1 – Hỗ trợ từng bước | Nhà khoa học giao từng việc | Tóm tắt một bài báo |
| 2 – Bán tự động | Chuỗi Skill chạy liên tiếp, dừng ở điểm xác nhận | Bộ tài liệu → ma trận bằng chứng → khoảng trống |
| 3 – Tự động toàn trình | Tự kích hoạt theo lịch hoặc khi có dữ liệu mới, gửi sản phẩm để duyệt | Sáng thứ Hai hằng tuần tự gửi bản tin công bố mới |

> Kích hoạt → Kiểm soát dữ liệu → Agent điều phối → Chuỗi Skill → Sản phẩm → **Nhà khoa học xác nhận** → Lưu trữ

**Năm quyết định luôn thuộc về nhà khoa học – năm điểm phê duyệt trong mọi quy trình:**

| Quyết định | Điểm phê duyệt trong quy trình | Đã thấy trong demo |
|---|---|---|
| 1. Dữ liệu nào được đưa lên AI | Trước khi dữ liệu vào quy trình | Chỉ dùng dữ liệu xanh |
| 2. Nguồn nào được chấp nhận | Sau bước tìm và tổng hợp tài liệu | Bấm thử từng DOI |
| 3. Khoảng trống nào có giá trị | Trước khi soạn đề xuất nhiệm vụ | Chọn 1 trong 3 khoảng trống |
| 4. Phương pháp nào phù hợp | Trước khi phân tích dữ liệu | Đổi cách tìm ngoại lệ khi chỉ có 3 mẫu lặp |
| 5. Kết quả được diễn giải thế nào | Trước khi viết bài báo, báo cáo | Tách "kết quả tính toán" và "diễn giải đề xuất" |

> *Câu chốt:* Tự động hóa không bỏ qua nhà khoa học – nó đưa nhà khoa học lên vị trí đặt mục tiêu và phê duyệt.

**Lời nói:** nhắc lại từng khoảnh khắc trong demo Phần III – mỗi quyết định là một chỗ quy trình **dừng lại chờ người duyệt**.

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 18 – Bản đồ quy trình tự động của Trung tâm (5′)

**Chữ trên slide:**

| Mã | Quy trình | Kích hoạt | Sản phẩm |
|---|---|---|---|
| QT-00 | Kiểm soát dữ liệu xanh / vàng / đỏ | Mỗi khi có đầu vào | Nhãn phân loại, nhật ký |
| QT-01 | Theo dõi công bố khoa học | Hằng tuần | Bản tin theo hướng nghiên cứu |
| QT-02 | Tổng quan tài liệu, khoảng trống | Khi có ý tưởng | Ma trận bằng chứng |
| QT-03 | Đề xuất, thuyết minh | Khi khoảng trống được duyệt | Bản nháp Mẫu 01A, 07, 08 |
| QT-04 | Xử lý – phân tích dữ liệu | Khi có dữ liệu mới | Báo cáo chất lượng, bảng, biểu đồ, mã |
| QT-05 | Theo dõi tiến độ – kinh phí | Hằng tháng | Báo cáo, cảnh báo chậm mốc |
| QT-06 | Bài báo, báo cáo tổng kết | Khi có kết quả | Bản thảo, Mẫu 21, 22 |

**Hình ảnh (chính):** sơ đồ dòng chảy, mỗi quy trình gắn điểm phê duyệt tương ứng với năm quyết định ở Slide 17: QT-01 → QT-02 → QT-03 → QT-04 → QT-06, QT-05 chạy song song, tất cả đi qua QT-00; ảnh chụp bản tin QT-01 chạy thật với chủ đề ăn mòn khí quyển.

**Việc phải làm:** chạy thử QT-01 để có ảnh bản tin thật.

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 19 – Lộ trình triển khai và kết luận (3′)

**Chữ trên slide:**

| Giai đoạn | Thời gian | Nội dung |
|---|---|---|
| 1. Thí điểm | Tháng 1–3 | Thư viện Skill nền; QT-00, QT-01, QT-04 tại 1–2 phòng, dữ liệu xanh |
| 2. Đánh giá – mở rộng | Tháng 4–6 | QT-02, QT-03, QT-06 bán tự động; đo thời gian tiết kiệm |
| 3. Nhân rộng – liên thông | Tháng 7–12 | Nối chuỗi toàn trình; QT-05; mô hình chạy cục bộ cho dữ liệu vàng / đỏ |

> **Đề nghị:** mỗi phòng đề xuất **một quy trình lặp lại** để tự động hóa trong giai đoạn thí điểm.
> **Kết luận:** chọn đúng nhiệm vụ → đóng gói thành Skill → tổ chức thành quy trình → giữ trách nhiệm khoa học.
> **Thông điệp Phần IV:** Đóng gói kinh nghiệm thành Skill, kế thừa khoa học mở, nối thành quy trình tự động; nhà khoa học đặt mục tiêu và phê duyệt.

**Lời nói:** tổ chức thực hiện – nhóm triển khai; nhà khoa học đầu mối mỗi phòng; bộ phận bảo mật phê duyệt quy tắc dữ liệu.

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

# TRAO ĐỔI VÀ PHỤ LỤC

---

## Slide 20 – Trao đổi và thảo luận (12′)

**Chữ trên slide:**
- Kết quả phiếu khảo sát trước buổi học (biểu đồ)
- Các quy trình các phòng muốn tự động hóa
- Câu hỏi – góp ý – đề xuất thí điểm
- Đầu mối liên hệ: ______________________

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 21 – Phụ lục A: AI lập trình (không trình bày)

**Chữ trên slide:**
- GitHub Octoverse 2025: hơn 180 triệu lập trình viên; hơn 36 triệu người mới trong một năm; 630 triệu kho mã; gần 1 tỷ lần đẩy mã; 4,3 triệu dự án AI
- Stack Overflow 2025: 84% lập trình viên dùng hoặc dự định dùng AI; 51% lập trình viên chuyên nghiệp dùng hằng ngày
- SWE-bench Verified (năng lực sửa lỗi phần mềm thật) tăng mạnh trong một năm – *kiểm tra số liệu trong bản gốc AI Index 2026 trước khi dùng*
- Các AI Agent lập trình: Claude Code, OpenAI Codex, GitHub Copilot, Cursor

**Nguồn:** N1, N11, N13

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 22 – Phụ lục B: Ví dụ Google và các nhà khoa học dùng AI (không trình bày – dự phòng khi được hỏi)

**Chữ trên slide:** dòng thời gian ngang, 5 thẻ; thẻ ① phóng to

| # | Thời điểm | Tên | Một dòng kết quả |
|---|---|---|---|
| ① | 10/2026 · *Science* | **AlphaProof Nexus** | Giải 9 bài toán mở của Erdős, trong đó 2 bài tồn tại 56 năm; máy kiểm chứng từng bước chứng minh |
| ② | 2025 · *Cell*, *Nature* | **AI co-scientist** + Imperial College London | Trong khoảng 2 ngày, AI đưa ra đúng giả thuyết mà nhóm nghiên cứu mất nhiều năm thí nghiệm mới chứng minh (khi chưa công bố) |
| ③ | 10/2025 · bioRxiv | **C2S-Scale** + Đại học Yale | Sàng lọc hơn 4.000 thuốc, tìm ra một tổ hợp giúp tế bào ung thư "lộ diện" trước hệ miễn dịch – đã kiểm chứng trên tế bào |
| ④ | 05/2025 | **AlphaEvolve** | Phá kỷ lục 56 năm về phép nhân ma trận (49 → 48 phép nhân); thu hồi 0,7% năng lực tính toán bị bỏ phí của Google |
| ⑤ | 2025 · *Nature* 2026 | **ERA** – AI viết phần mềm khoa học | AI tự viết – chạy – chấm điểm mã; 14 mô hình dự báo nhập viện COVID-19 tốt hơn mô hình chuẩn của CDC Mỹ (đánh giá hồi cứu) |

> *Câu chốt:* Nhà khoa học đặt bài toán – AI đề xuất và thực hiện – kết quả được kiểm chứng độc lập.

**Hình ảnh:** logo hoặc hình minh họa nhỏ cho mỗi thẻ; ảnh bìa bài báo *Science*, *Cell*, *Nature*.

**Dùng khi được hỏi – gợi ý trả lời:**
- ① Bài toán Erdős: hàng trăm bài toán mở do nhà toán học Paul Erdős để lại. Lean là phần mềm kiểm tra chứng minh từng bước, như "trọng tài máy". AI giải được khoảng 2,5% số bài đã thử – còn khiêm tốn, nhưng là bài toán mở thật.
- ② Nhóm Imperial nghiên cứu vì sao gen kháng kháng sinh lan được giữa các loài vi khuẩn. Họ phát hiện một loại đoạn gen tự tạo "vỏ" nhưng "mượn đuôi" của nhiều loại virus để xâm nhập nhiều loài. Trước khi công bố, họ hỏi AI cùng câu hỏi – giả thuyết số 1 của AI trùng với kết quả của họ. AI không phát hiện điều mới ở đây, nhưng đi đến cùng kết luận trong vài ngày. Nhóm cho biết nếu có giả thuyết này từ đầu, họ đã tiết kiệm được nhiều năm.
- ③ Thuốc silmitasertib (đã có sẵn) dùng cùng interferon liều thấp. Mới thử trên tế bào, **chưa thử trên người**.
- ④ Phép nhân ma trận là phép tính nền tảng của phần mềm khoa học, lặp lại hàng tỷ lần.
- ⑤ Đánh giá hồi cứu: chạy lại trên dữ liệu các tuần đã qua để so sánh công bằng. Ví dụ này đã nêu ở slide Demo 2.

**Nguồn:** G1–G5

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 23 – Phụ lục C: Nguồn tham khảo (không trình bày)

**Chữ trên slide:** danh mục nguồn theo Mục 11 của kế hoạch – 5 công bố ví dụ ở Phụ lục B (kèm DOI), số liệu bối cảnh, pháp lý Việt Nam, tiêu chuẩn ISO 9223 / 9224, khoa học mở.

**Việc phải làm:** kiểm tra mã số bài arXiv 2609.00065 (N18).

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 24 – Phụ lục D: Dự án và bộ Skill khoa học mở (không trình bày)

**Chữ trên slide:** AI4S Open Science · AIPOCH Open Science · K-Dense Scientific Agent Skills · CES Global – kèm URL và lĩnh vực của từng bộ.

**Việc phải làm:** bổ sung URL (N17).

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Ý KIẾN CHUNG CỦA NGƯỜI DUYỆT

- Bố cục và thời lượng:
- Nội dung cần thêm:
- Nội dung cần bớt:
- Người duyệt: ______________________ · Ngày: ____ / ____ / 2026
