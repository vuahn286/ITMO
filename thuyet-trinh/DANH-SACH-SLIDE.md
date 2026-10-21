# DANH SÁCH SLIDE ĐỂ CHỈNH SỬA VÀ DUYỆT

**Bài thuyết trình:** AI Agent và sự chuyển đổi phương thức nghiên cứu khoa học
**Đối tượng:** Cán bộ, nhà khoa học Trung tâm Nhiệt đới Việt – Nga · **Thời lượng:** 120 phút · **Số slide:** 23 slide trình bày + 4 phụ lục + trang bìa
**Căn cứ:** Kế hoạch v2.1 · **Bản v2.5 (21/10/2026):** giữ đúng các phần anh/chị đã xóa trong tệp Word (không đưa lại); bỏ toàn bộ phần lời nói (người trình bày tự soạn); bỏ slide "Lộ trình triển khai và kết luận"; Slide 3 thêm tính năng mới của AI Agent và ô giới hạn (6′, thảo luận còn 12′). **Cập nhật:** thêm Slide 16 (mô hình 3D quá trình ăn mòn) và Slide 17 (Demo 3 – công cụ cho máy không Internet); từ slide cũ 16 trở đi số slide cộng 2; thảo luận còn 9′. **Tệp này là bố cục slide chính thức.**

---

## Cách dùng tệp này

Mỗi slide gồm các phần:
- **Chữ trên slide** – nội dung xuất hiện trên màn hình. Sửa trực tiếp vào đây.
- **Hình ảnh** – hình hoặc biểu đồ cần chuẩn bị.
- **Nguồn** – mã căn cứ, tra ở Mục 7 của kế hoạch.

Trạng thái: `[ ] Duyệt` · `[ ] Sửa theo ghi chú` · `[ ] Bỏ`

---

## TỔNG QUAN

| # | Tên slide | Phần | Thời lượng | Duyệt |
|---|---|---|---|---|
| – | Trang bìa | – | – | [ ] |
| 1 | AI đang phát triển nhanh đến mức nào? | I | 4′ | [ ] |
| 2 | AI trong các lĩnh vực khoa học: quốc tế và Việt Nam | I | 5′ | [ ] |
| 3 | Năng lực cốt lõi của AI: từ trả lời đến thực hiện | I | 6′ | [ ] |
| 4 | Phương thức nghiên cứu đang thay đổi | I | 4′ | [ ] |
| 5 | Công việc nào cần chatbot, công việc nào cần AI Agent? | II | 5′ | [ ] |
| 6 | Các công cụ AI và vai trò khác nhau | II | 4′ | [ ] |
| 7 | Claude là gì? Các tính năng nổi bật | II | 7′ | [ ] |
| 8 | Dùng Claude cơ bản: 6 bước đầu tiên | II | 7′ | [ ] |
| 9 | Một cách giao việc chung cho các công cụ AI Agent | II | 6′ | [ ] |
| 10 | Tổ chức một không gian làm việc nghiên cứu | II | 3′ | [ ] |
| 11 | Skill, Subagent và hệ thống nhiều Agent | II | 3′ | [ ] |
| 12 | Từ tài liệu đến khoảng trống nghiên cứu | III | 7′ | [ ] |
| 13 | Từ khoảng trống đến phiếu đề xuất và thuyết minh – DEMO 1 với biểu mẫu thật của Trung tâm | III | 7′ | [ ] |
| 14 | Thuyết minh, tiến độ và kinh phí theo biểu mẫu Trung tâm | III | 5′ | [ ] |
| 15 | Xử lý dữ liệu bằng mã Python – DEMO 2 | III | 8′ | [ ] |
| 16 | 🆕 Dựng mô hình 3D mô tả quá trình ăn mòn | III | 3′ | [ ] |
| 17 | 🆕 Đề tài có dữ liệu mật: AI viết công cụ, máy không Internet xử lý dữ liệu – DEMO 3 | III | 5′ | [ ] |
| 18 | Xây dựng bài báo và báo cáo tổng hợp kết quả | III | 5′ | [ ] |
| 19 | Toàn cảnh: một nhiệm vụ khoa học đi qua AI Agent | III | 2′ | [ ] |
| 20 | Skill và khoa học mở: nền móng của tự động hóa | IV | 6′ | [ ] |
| 21 | Ứng dụng khoa học mở và tự động hóa từng bước đến toàn trình | IV | 5′ | [ ] |
| 22 | Bản đồ quy trình tự động của Trung tâm và năm quyết định của nhà khoa học | IV | 4′ | [ ] |
| 23 | Trao đổi và thảo luận | IV | 9′ | [ ] |
| 24 | Phụ lục A: AI lập trình (không trình bày) | IV | – | [ ] |
| 25 | Phụ lục B: Ví dụ Google và các nhà khoa học dùng AI (không trình bày – dự phòng khi được hỏi) | IV | – | [ ] |
| 26 | Phụ lục C: Nguồn tham khảo (không trình bày) | IV | – | [ ] |
| 27 | Phụ lục D: Dự án và bộ Skill khoa học mở (không trình bày) | IV | – | [ ] |
| | **Tổng** | | **120′** = 111′ trình bày + 9′ thảo luận | |

---

## TRANG BÌA

**Chữ trên slide:**
> **AI AGENT VÀ SỰ CHUYỂN ĐỔI PHƯƠNG THỨC NGHIÊN CỨU KHOA HỌC**
> Người trình bày: ______________________
> Trung tâm Nhiệt đới Việt – Nga · ____ / ____ / 2026

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

# PHẦN I. TỔNG QUAN (19 phút)

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

> *Câu chốt:* AI đang trở thành một thành phần của hạ tầng nghiên cứu.

**Hình ảnh:** mỗi lĩnh vực một hình nhỏ (ảnh vệ tinh, bản đồ bão, robot, protein, tinh thể).

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 3 – Năng lực cốt lõi của AI: từ trả lời đến thực hiện (6′)

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
| Kiểm tra kết quả | Người dùng tự làm | Tự kiểm tra từng bước – vẫn cần người xác nhận |
| Chi phí – thời gian | Thấp | Cao hơn |

🆕 **Tính năng mới của AI Agent (2024–2026):**

| Tính năng | Làm được gì cho nhà khoa học | Mốc |
|---|---|---|
| **Làm việc tự chủ nhiều giờ** | Giao cả chuỗi việc (đọc dữ liệu → phân tích → vẽ biểu đồ → viết báo cáo); AI tự làm, tự sửa lỗi | Độ dài việc AI làm được: ~1 giờ (02/2025) → ≥ 16 giờ (05/2026) |
| **Nghiên cứu chuyên sâu (Deep Research)** | Tự tìm, đọc hàng chục – hàng trăm nguồn, viết báo cáo có trích dẫn | Google 12/2024 · OpenAI 02/2025 · Claude 04/2025 |
| **Sử dụng máy tính** | Tự nhìn màn hình, bấm chuột, gõ phím – thao tác trên trang web, phần mềm như người dùng | Anthropic thử nghiệm công khai 10/2024 |
| **Kết nối chuẩn mở MCP** | Một "ổ cắm chung" để AI kết nối cơ sở dữ liệu, kho tài liệu, phần mềm | Ra mắt 11/2024; > 10.000 máy chủ kết nối công khai; chuyển cho Linux Foundation 12/2025 |
| **Skill – chuẩn mở** | Quy trình mẫu đóng gói một lần, dùng được trên nhiều công cụ AI khác nhau | Chuẩn mở 12/2025 (agentskills.io) |
| **Chạy nền, theo lịch** | Tự chạy định kỳ (ví dụ: bản tin công bố mới mỗi sáng thứ Hai) – không cần ngồi canh | Tác vụ theo lịch trong Cowork (Claude cho Windows, 04/2026) |

> *Ô nhỏ:* Lập trình là lĩnh vực AI Agent phát triển sớm nhất – 84% lập trình viên đang dùng hoặc dự định dùng AI. Nhà khoa học không cần giỏi lập trình vẫn có thể yêu cầu AI viết và chạy mã xử lý dữ liệu → Slide 15.

> ⚠ **AI vẫn có thể sai:** bịa tài liệu tham khảo, tính nhầm, chọn sai phương pháp mà vẫn trả lời rất tự tin → nhà khoa học kiểm tra lại mọi kết quả.
> *Ví dụ từ dự án ăn mòn của bài này:* AI **phát hiện** lỗi đơn vị trong bộ dữ liệu đã công bố (ghi g/m², thực tế µm/năm) – nhưng cách tìm số đo bất thường AI chọn lần đầu lại **đánh dấu nhầm** 20 giá trị bình thường và bỏ sót lỗi gõ nhầm.

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 4 – Phương thức nghiên cứu đang thay đổi (4′)

**Chữ trên slide:**

| Trước đây | Hiện nay | Ví dụ |
|---|---|---|
| Tìm kiếm thủ công | Tổng hợp bằng chứng có hệ thống | AI co-scientist (Google) đọc tài liệu, đề xuất giả thuyết |
| Thao tác riêng lẻ | Quy trình liên tục | ERA (Google): AI viết mã → chạy → chấm điểm → cải tiến |
| Câu lệnh dùng một lần | Quy trình mẫu (Skill) dùng lại | Thư viện Skill khoa học mở |
| Một chatbot | Nhiều trợ lý phối hợp | Co-scientist: các trợ lý đề xuất, phản biện, xếp hạng giả thuyết |

> **Nhà khoa học dẫn dắt:** câu hỏi, phương pháp, diễn giải và công bố.
> AI không thay thế nhà khoa học; AI đang thay đổi cách nhà khoa học đặt giả thuyết, xử lý dữ liệu và kiểm chứng kết quả.

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

# PHẦN II. LỰA CHỌN VÀ SỬ DỤNG CÔNG CỤ AI PHÙ HỢP (35 phút)

---

## Slide 5 – Công việc nào cần chatbot, công việc nào cần AI Agent? (5′)

**Chữ trên slide:** bản đồ công việc nghiên cứu theo 5 bậc – càng lên cao càng phức tạp, tốn thời gian và chi phí *(🆕 v2.4: mở rộng từ 5 lên 20 công việc)*

| Bậc | Loại việc | Công việc thường gặp của nhà khoa học | Công cụ phù hợp |
|---|---|---|---|
| 1 | Hỏi – đáp, tra cứu nhanh | Giải thích khái niệm, tiêu chuẩn (ISO 9223 cấp C4 là gì?) · Dịch thuật ngữ Việt – Nga – Anh · Gợi ý từ khóa tìm tài liệu · Kiểm tra công thức, đơn vị | Chatbot |
| 2 | Làm việc với một tài liệu | Tóm tắt bài báo · Dịch bài báo tiếng Nga/Anh · Trích bảng số liệu từ PDF · Sửa văn phong, rút gọn tóm tắt · Soạn công văn, thư mời hội thảo | Chatbot |
| 3 | Tổng hợp nhiều nguồn | Tổng quan tài liệu, ma trận bằng chứng · Tìm khoảng trống nghiên cứu · So sánh tiêu chuẩn Việt Nam – Nga (ГОСТ) – quốc tế · Bản tin công bố mới theo chủ đề | Chatbot có dự án / Research |
| 4 | Xử lý nhiều tệp, dữ liệu | Làm sạch, gộp số liệu từ nhiều trạm · Thống kê, hồi quy, vẽ biểu đồ · Điền biểu mẫu thuyết minh từ bộ hồ sơ · Lập dự toán, sơ đồ tiến độ | AI Agent |
| 5 | Chuỗi nhiệm vụ, tự động hóa | Dữ liệu → mô hình → biểu đồ → bản thảo bài báo · Bộ hồ sơ nghiệm thu (Mẫu 21, 22) · Theo dõi tiến độ hằng tháng · Bản tin tự động hằng tuần | AI Agent + Skill + lịch tự động |

> *Câu chốt:* Chọn đúng bậc – không dùng "dao mổ trâu giết gà".

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 6 – Các công cụ AI và vai trò khác nhau (4′)

**Chữ trên slide:** *(cập nhật 10/2026)*

| Công cụ | Thế mạnh | Ví dụ công việc | Dữ liệu có bị dùng để huấn luyện? |
|---|---|---|---|
| Perplexity | Tìm thông tin trên web, có dẫn nguồn | Tìm nhanh tài liệu mới | **☐ cần điền** |
| NotebookLM | Hỏi – đáp trên bộ tài liệu tự chọn | Hỏi đáp trên 50 bài báo đã tải | **☐ cần điền** |
| ChatGPT | Tổng hợp, phân tích, viết; nghiên cứu chuyên sâu | Nghiên cứu chuyên sâu một chủ đề | **☐ cần điền** |
| Gemini | Gắn với hệ sinh thái Google | Tổng hợp tài liệu trên Drive | **☐ cần điền** |
| Claude | Làm việc với tệp, chuỗi nhiệm vụ trong dự án | Soạn thuyết minh từ bộ hồ sơ | Gói cá nhân: người dùng tự chọn · Team/Enterprise: không, theo mặc định |
| *Công cụ chuyên cho tài liệu khoa học* | Elicit, Consensus, Semantic Scholar, Scite, ResearchRabbit | Tìm, sàng lọc, trích xuất bài báo (xem Slide 12) | **☐ cần điền** |

> *Câu chốt:* Hệ sinh thái AI rất nhiều, nhưng chọn đúng công cụ cho đúng việc mới giúp tối ưu thời gian, chi phí và nâng cao chất lượng công việc.

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 7 – Claude là gì? Các tính năng nổi bật (7′)

**Chữ trên slide:**
- **Claude** – trợ lý AI của công ty Anthropic (Mỹ). Trên máy tính Windows có hai cách dùng: **trình duyệt web (claude.ai)** hoặc **ứng dụng Claude cho Windows**; hội thoại và dự án đồng bộ giữa hai cách.
- **Bốn mô hình** *(cập nhật 10/2026)*:

| Mô hình | Dùng khi | Gói |
|---|---|---|
| Haiku 5.5 | Câu hỏi nhanh, việc đơn giản | Mọi gói |
| Sonnet 5.5 | Công việc hằng ngày – cân bằng tốc độ và chất lượng | Mọi gói |
| Opus 5.5 | Phân tích phức tạp, chuỗi nhiệm vụ dài | Từ Pro |
| Fable 5.1 | Dự án lớn, AI Agent làm việc dài hơi | Từ Pro |

- 🆕 **Tính năng nổi bật** (đều dùng được trên Windows):

| Tính năng | Làm được gì | Gói |
|---|---|---|
| **Dự án (Projects)** | Gom tài liệu + hướng dẫn chung cho một nhiệm vụ | Mọi gói (Free tối đa 5 dự án) |
| **Tạo tệp, chạy mã** | Viết – chạy Python; xuất Word, Excel, PowerPoint, PDF | Mọi gói |
| **Research** | Nghiên cứu chuyên sâu: tự tìm hàng chục nguồn, tổng hợp có trích dẫn | Từ Pro |
| **Kết nối (Connectors)** | Đọc tệp trên Google Drive, Gmail… với quyền của chính người dùng | Tùy kết nối |
| **Bộ nhớ (Memory)** | Nhớ bối cảnh làm việc giữa các cuộc trò chuyện; xem và sửa được | Mọi gói |
| **Skill** | "Quy trình mẫu" đóng gói (hướng dẫn + biểu mẫu + mã); tự tạo hoặc tải về (tệp ZIP) | Cần bật chạy mã; kiểm tra theo gói |
| **Cowork** | Trợ lý làm việc trực tiếp với **thư mục trên máy tính**: đọc nhiều tệp, sắp xếp, tạo báo cáo – trong ứng dụng Claude cho Windows (chính thức từ 04/2026) | Gói trả phí |
| **Tác vụ theo lịch (tự động hóa)** | Đặt việc chạy định kỳ – ví dụ sáng thứ Hai tự tổng hợp công bố mới; chạy trên đám mây, không cần bật máy | Gói trả phí (trong Cowork) |
| **Plugin** | Gói gồm nhiều Skill + kết nối + trợ lý con, cài một lần dùng cho cả nhóm | Gói trả phí |
| **Claude Code** | AI Agent lập trình – viết, chạy, sửa mã trong thư mục dự án | Từ Pro |

**Hình ảnh:** ảnh chụp ứng dụng Claude cho Windows: màn hình chính, nút chọn mô hình, thẻ Cowork, trang Scheduled (tác vụ theo lịch), trang Skills.

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 8 – Dùng Claude cơ bản: 6 bước đầu tiên (7′)

**Chữ trên slide:**

| Bước | Làm gì | Ở đâu |
|---|---|---|
| 1. Tạo tài khoản | Đăng nhập bằng email trên trình duyệt; nếu muốn, cài ứng dụng Claude cho Windows | claude.ai · claude.com/download |
| 2. Cài đặt quyền riêng tư **trước tiên** | Chọn có cho dùng hội thoại để cải thiện mô hình hay không; xem và sửa "bộ nhớ" Claude lưu về bạn | Settings → Privacy · Settings → Capabilities |
| 3. Hỏi đáp và tải tệp | Gõ câu hỏi; kéo thả PDF, Word, Excel, ảnh vào khung chat; chọn mô hình | Màn hình chính |
| 4. Bật công cụ | Tìm kiếm web; viết và chạy mã, tạo tệp; Research (gói Pro trở lên) | Settings → Capabilities, hoặc nút công cụ trong khung chat |
| 5. Tạo Dự án (Project) | Viết hướng dẫn chung một lần + tải bộ tài liệu dùng chung cho mọi cuộc trò chuyện trong dự án | Mục Projects |
| 6. Nhận sản phẩm | Văn bản, bảng, biểu đồ hiện ngay bên cạnh; tải về Word, Excel, PowerPoint, PDF | Khung kết quả bên phải |

> **3 thói quen tốt:** nói rõ việc cần làm và dạng kết quả · yêu cầu dẫn nguồn · luôn kiểm tra lại trước khi dùng.

**Hình ảnh:** 6 ảnh chụp màn hình nhỏ theo 6 bước (dùng tài khoản demo, dữ liệu xanh).

**🆕 Demo: tổng hợp dữ liệu từ nhiều nguồn → bảng tổng hợp → báo cáo hoàn chỉnh (3 phút, dữ liệu THẬT)**

📂 Thư mục `thuyet-trinh/du-lieu-demo/nhieu-nguon/` – 4 tệp, 4 định dạng, 3 nguồn công bố khác nhau:

| Tệp | Nội dung | Đặc điểm |
|---|---|---|
| `nguon1_ISOCORRAG_MICAT_quoc_te.xlsx` | 320 trạm quốc tế (ISOCORRAG, MICAT) | Excel, tiêu đề tiếng Anh, **nhãn đơn vị sai trong nguồn** |
| `nguon2_tram_Viet_Nam.csv` | 12 trạm Việt Nam (Lê Thị Hồng Liên và cs., 2007) | CSV, tiêu đề tiếng Việt |
| `nguon3_tram_Nga.csv` | 18 trạm Nga (Murmansk, Viễn Đông) | CSV, tên cột khác hẳn |
| `nguon4_nguong_ISO_9223.md` | Ngưỡng cấp ăn mòn ISO 9223 | Văn bản |

⌨ Câu lệnh:
```
Tôi tải lên 4 tệp từ các nguồn khác nhau về tốc độ ăn mòn năm đầu của thép cacbon.
1. Đọc cả 4 tệp, đối chiếu tên cột và đơn vị; nêu mọi điểm không thống nhất.
2. Gộp thành một bảng chung; xếp cấp ăn mòn theo ngưỡng ISO 9223 trong tệp 4.
3. Lập bảng tổng hợp so sánh Quốc tế – Việt Nam – Nga: số trạm, trung bình, trung vị,
   nhỏ nhất, lớn nhất, số trạm mỗi cấp. Vẽ 1 biểu đồ so sánh.
4. Viết báo cáo 2 trang (Word): mục đích, dữ liệu và nguồn, kết quả, nhận xét, hạn chế.
Ghi nguồn cho mọi số liệu.
```

📊 **Kết quả mong đợi (đã chạy thử – `ket_qua_mong_doi_bang_tong_hop.csv`):**

| Nhóm | Số trạm | Trung bình | Trung vị | Phân cấp |
|---|---|---|---|---|
| Quốc tế | 320 | 38,8 µm/năm | 28,6 | C1: 1 · C2: 124 · C3: 132 · C4: 38 · C5: 23 · CX: 2 |
| Việt Nam | 12 | 31,5 | 31,6 | C2: 1 · **C3: 11** |
| Nga | 18 | 17,8 | 14,1 | **C2: 13** · C3: 5 |

AI cần phát hiện: tệp 1 ghi đơn vị chưa rõ/sai (giá trị thực là µm/năm – đối chiếu với cột cấp ăn mòn) – đây là lỗi thật trong dữ liệu công bố.

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 9 – Một cách giao việc chung cho các công cụ AI Agent (6′)

**Chữ trên slide:** quy trình 5 bước

1. **Xác định nhiệm vụ** – làm gì, để làm gì
2. **Cung cấp dữ liệu** – theo quy tắc xanh / vàng / đỏ
3. **Quy định đầu ra** – dạng bảng, văn bản, biểu đồ, độ dài
4. **Yêu cầu dẫn nguồn, lưu mã** – để kiểm tra và tái lập
5. **Kiểm tra và xác nhận** – nhà khoa học duyệt

**🆕 Ví dụ với dữ liệu thật – câu lệnh đủ 5 bước** (387 số đo thực địa đã công bố):
```
[1. Nhiệm vụ] Đánh giá mô hình quốc tế dự báo tốc độ ăn mòn năm đầu của thép cacbon có
áp dụng được cho Việt Nam không.
[2. Dữ liệu – nhóm xanh, đã công bố] Tệp an_mon_387.csv: 320 trạm ISOCORRAG + MICAT để
học mô hình; 67 trạm độc lập (có 12 trạm Việt Nam, 18 trạm Nga) để kiểm định.
[3. Đầu ra] (a) báo cáo chất lượng dữ liệu; (b) mô hình dạng hàm liều – đáp ứng ISO 9223;
(c) bảng sai số theo vùng; (d) biểu đồ đo – dự đoán; (e) báo cáo Word 3 trang.
[4. Dẫn nguồn, tái lập] Ghi nguồn mọi số liệu; lưu toàn bộ mã Python; không xóa dữ liệu gốc.
[5. Kiểm tra] Tách "kết quả tính toán" và "diễn giải đề xuất"; nêu rõ hạn chế.
```

📊 **Kết quả thật đã chạy (thư mục `du-an-nghien-cuu/05-ket-qua/`):**
- AI phát hiện **lỗi đơn vị trong bộ dữ liệu công bố** (ghi g/m², thực tế µm/năm – 99,5% khớp cột cấp ăn mòn)
- Mô hình quốc tế **dự đoán thấp hơn thực đo ở Việt Nam khoảng 31%**, cao hơn ở Nga khoảng 80%
- Sau hiệu chỉnh theo vùng: đúng cấp ăn mòn ở **9/12 trạm Việt Nam** (trước là 2/12)

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 10 – Tổ chức một không gian làm việc nghiên cứu (3′)

**Chữ trên slide:** *Mỗi nhiệm vụ khoa học – một dự án* (cách tạo dự án: xem Slide 8)

| Thành phần của dự án | Ví dụ – nhiệm vụ ăn mòn khí quyển |
|---|---|
| **Hướng dẫn chung** (viết một lần) | Trả lời tiếng Việt; luôn dẫn nguồn; không tự xóa dữ liệu; tách "kết quả tính toán" và "diễn giải" |
| **Tài liệu nền** | 10–15 bài báo, tiêu chuẩn ISO 9223 / 9224 |
| **Biểu mẫu** | Biểu mẫu của Trung tâm (bản trống) |
| **Dữ liệu** | Chỉ dữ liệu xanh – tệp đặt tên theo quy ước: `ngày_trạm_loại-dữ-liệu` |
| **Các cuộc trò chuyện** | Mỗi công đoạn một cuộc: tổng quan, thuyết minh, phân tích dữ liệu, bài báo |

**🆕 Ví dụ thực tế – dự án nghiên cứu thật đi kèm bài thuyết trình (`du-an-nghien-cuu/`):**
```
du-an-nghien-cuu/
├── 00-quan-ly-du-an/        ← kế hoạch, nhật ký (ghi cả lần sai và sửa), việc còn lại
├── 01-tong-quan-tai-lieu/   ← 13 tài liệu đã xác minh, ma trận bằng chứng, khoảng trống   (Slide 12)
├── 02-de-xuat-thuyet-minh/  ← bản nháp đề xuất + biểu mẫu Trung tâm                       (Slide 13–14)
├── 03-du-lieu/              ← thô (chỉ đọc) → đã xử lý → bổ sung; từ điển dữ liệu           (Slide 15)
├── 04-ma-nguon/             ← 4 bước mã: hợp nhất → mô hình → hiệu chỉnh → 3D
├── 05-ket-qua/              ← bảng, hình, mô hình 3D, kiểm tra bằng Skill                 (Slide 15, 16, 20)
├── 06-bai-bao/              ← bản thảo bài báo                                             (Slide 18)
└── 07-bao-cao/              ← báo cáo tổng hợp
```
→ Mỗi thư mục là một giai đoạn của vòng đời nhiệm vụ; thêm dữ liệu mới vào `03-du-lieu/3-bo-sung/`, chạy lại `chay_tat_ca.sh`: **toàn bộ kết quả tự cập nhật**.

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 11 – Skill, Subagent và hệ thống nhiều Agent (3′) – *chỉ giới thiệu*

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

# PHẦN III. AI AGENT TRONG VÒNG ĐỜI NHIỆM VỤ KHOA HỌC (42 phút)

> 🆕 v2.4: Phần III **bắt đầu ngay bằng tìm khoảng trống nghiên cứu**; slide tổng quan vòng đời chuyển xuống cuối phần (Slide 19) để tổng kết.
> Slide 13–14 dùng **biểu mẫu thật của Trung tâm** (người trình bày cung cấp); Slide 12 và 15 dùng **dữ liệu, tài liệu thật đã công bố**; dữ liệu giả lập chỉ còn dùng để minh họa phát hiện lỗi.

---

## Slide 12 – Từ tài liệu đến khoảng trống nghiên cứu (7′)

**Chữ trên slide:**
- **Tình huống:** ăn mòn khí quyển của kim loại trong khí hậu nhiệt đới Việt Nam
- 🌍 **Ví dụ thật:** AI co-scientist (Google) – nhiều trợ lý đề xuất, phản biện, xếp hạng giả thuyết
- 🧰 **Công cụ tìm và đọc tài liệu:** Claude Research · Elicit (tổng quan hệ thống, trích xuất bảng) · Consensus (câu trả lời có dẫn chứng) · Semantic Scholar (miễn phí) · Scite (trích dẫn ủng hộ hay phản bác) · ResearchRabbit (bản đồ trích dẫn)
- ⌨ **Câu lệnh:**
  > Từ các bài báo trong dự án, lập ma trận bằng chứng (tác giả – năm, địa điểm, kim loại, thời gian phơi mẫu, biến môi trường, mô hình, kết luận, hạn chế). Chỉ ra điểm chưa thống nhất và 3 khoảng trống cho điều kiện Việt Nam, mỗi khoảng trống dẫn chứng ít nhất 2 bài.
- ✅ **Nhà khoa học xác nhận:** nguồn có thật; khoảng trống có giá trị

**🆕 📂 Bộ tài liệu thật để demo** (đã xác minh tồn tại – tải bản đầy đủ trước buổi thuyết trình):

| # | Tài liệu | Ghi chú |
|---|---|---|
| 1 | Lê Thị Hồng Liên, Phạm Thy San, Hoàng Lâm Hồng (2007). Results of studying atmospheric corrosion in Vietnam 1995–2005. *Sci. Technol. Adv. Mater.* 8:552–558 | Tổng kết 10 năm, 6–8 trạm |
| 2 | Lê Thị Hồng Liên (2013). Summarize the results of study on atmospheric corrosion in Vietnam. *Vietnam J. Sci. Technol.* | Mở rộng sang đồng |
| 3 | Tran T.N.L. và cs. (2006). Atmospheric corrosion of carbon steel under field exposure in the southern part of Vietnam. *Corrosion Science* 48(1):179–192 | Nam Bộ, có/không mái che |
| 4 | Karpov V.A., Lapiga A.G., Kalinina E.V. và cs. (2017). Modeling of atmospheric corrosion in the tropical climate of Vietnam. *Protection of Metals and Physical Chemistry of Surfaces* 53(7):1205 | Nhóm tác giả Nga – Việt |
| 5 | Cole I., Nguyễn Việt Huệ. Steel corrosion map of Vietnam. *Vietnam J. Sci. Technol.* | Bản đồ ăn mòn thép |
| 6 | Chico B. và cs. (2017). Annual atmospheric corrosion of carbon steel worldwide… *Materials* 10(6):601 | Dữ liệu quốc tế ISOCORRAG, ICP, MICAT |
| 7 | Panchenko Yu.M., Marshakov A.I. (2017). Prediction of first-year corrosion losses of carbon steel and zinc in continental regions. *Materials* 10(4):422 | Mô hình Nga |
| 8 | ISO 9223:2012; ISO 9224:2012 | Tiêu chuẩn |

**🆕 Khoảng trống gợi ý – có căn cứ từ phân tích dữ liệu thật** *(đề xuất, nhà khoa học quyết định)*:
1. Mô hình quốc tế **đánh giá thấp ~31%** ăn mòn thép ở Việt Nam → cần hàm liều – đáp ứng hiệu chỉnh cho khí hậu nhiệt đới (thêm độ ẩm, mưa, chu kỳ khô – ướt).
2. Huế, Nha Trang ăn mòn cao dù clorua thấp → yếu tố chưa được giải thích.
3. Số liệu Việt Nam chủ yếu 1995–2005, chủ yếu thép cacbon năm đầu → thiếu dữ liệu dài hạn và cập nhật theo biến đổi khí hậu.

**Hình ảnh:** ảnh chụp ma trận bằng chứng và 3 khoảng trống có điểm phản biện.

**Nguồn:** G2 · N25 (công cụ tài liệu) · tài liệu 1–8 · Câu lệnh 1.1–1.3

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 13 – Từ khoảng trống đến phiếu đề xuất và thuyết minh – DEMO 1 với biểu mẫu thật của Trung tâm (7′)

**Chữ trên slide:**
- Khoảng trống → tính cấp thiết, mục tiêu, nội dung, phương pháp, sản phẩm
- 🆕 **Demo trực tiếp:** đưa **biểu mẫu thật của Trung tâm** (phiếu đề xuất, thuyết minh) vào dự án → AI điền theo khoảng trống đã chọn
- ⌨ **Câu lệnh:**
  ```
  Đọc biểu mẫu [tên biểu mẫu] trong dự án. Liệt kê toàn bộ mục và yêu cầu của từng mục.
  Điền nội dung cho khoảng trống số [1]: giữ nguyên số mục, tiêu đề, định dạng của mẫu;
  mục nào thiếu thông tin ghi [CẦN BỔ SUNG: ...]; không tự đặt số liệu.
  Sau đó lập bảng đối chiếu Mục tiêu → Nội dung → Phương pháp → Sản phẩm → Chỉ tiêu,
  đánh dấu ⚠ chỗ không khớp. Xuất tệp .docx.
  ```
- 📊 **Kết quả mong đợi:** biểu mẫu đã điền đúng cấu trúc; danh sách [CẦN BỔ SUNG]; bảng đối chiếu có dấu ⚠
- ✅ **Nhà khoa học xác nhận:** tính mới, tính khả thi, chỉ tiêu

**⚠ Dữ liệu khi demo:** biểu mẫu trống = nhóm xanh; **nội dung đề xuất thật = nhóm vàng** → chỉ dùng tài khoản gói tổ chức (không huấn luyện mô hình) hoặc dùng nội dung đề xuất giả định khi trình diễn trước đông người.

**Hình ảnh:** ảnh chụp bảng đối chiếu có dấu ⚠.

**Việc phải làm:** người trình bày gửi biểu mẫu của Trung tâm → chạy thử 2 lần trước buổi thuyết trình.

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 14 – Thuyết minh, tiến độ và kinh phí theo biểu mẫu Trung tâm (5′)

**Chữ trên slide:**
- 🆕 **Demo:** đưa biểu mẫu thuyết minh – tiến độ – dự toán của Trung tâm vào dự án
- ⌨ **Câu lệnh:**
  ```
  Từ thuyết minh đã duyệt, lập: (1) bảng nội dung công việc – sản phẩm – thời gian – người
  thực hiện; (2) sơ đồ Gantt; (3) dự toán theo biểu mẫu [tên], dùng ĐÚNG đơn giá và định mức
  tôi cung cấp, không tự đặt đơn giá; (4) kiểm tra logic trình tự và tổng kinh phí;
  liệt kê bất hợp lý và đề xuất điều chỉnh. Xuất Word và Excel.
  ```
- 📊 **Minh họa phát hiện lỗi** (dữ liệu giả lập): AI tìm ra 3 bất hợp lý cài sẵn – thu mẫu trước khi lắp xong giá phơi mẫu; quan trắc khí tượng kết thúc trước mốc thu mẫu cuối; công bố trước khi mô hình xong
- **Căn cứ lập dự toán:** Thông tư 03/2023/TT-BTC (định mức tối đa cho nhiệm vụ KH&CN dùng ngân sách nhà nước) và quy định riêng của Bộ Quốc phòng, Trung tâm
- ✅ **Xác nhận:** số liệu tài chính do cán bộ tài chính xác nhận

**Hình ảnh:** biểu mẫu đã điền; `thuyet-trinh/ket-qua-demo/gia-lap/so_do_gantt.png`.

**Việc phải làm:** người trình bày gửi biểu mẫu thuyết minh – tiến độ – dự toán; xác nhận văn bản định mức áp dụng trong Bộ Quốc phòng.

**Nguồn:** N26 (Thông tư 03/2023/TT-BTC)

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 15 – Xử lý dữ liệu bằng mã Python – DEMO 2 (8′)

**Chữ trên slide:**
- 🌍 **Ví dụ thật:** ERA (Google, *Nature* 2026) – AI tự viết, chạy, chấm điểm, cải tiến mã
- **Nhà khoa học không cần biết lập trình:** mô tả việc cần làm → AI viết mã Python → chạy → trả bảng, biểu đồ, **kèm mã để tái lập**
- ⌨ **Câu lệnh (trình diễn trực tiếp):** rà soát dữ liệu → tính toán và lập mô hình → vẽ biểu đồ
- 📊 **Kết quả:**
  - Dữ liệu giả lập: phát hiện đủ **14/14 lỗi** cài sẵn; thép CT3 ven biển C4 · đô thị C3 · nội địa C2
  - Dữ liệu thật (387 số đo): lỗi đơn vị trong dữ liệu công bố; mô hình quốc tế thấp hơn thực đo ở Việt Nam ~31%; mô hình 3D diễn tiến ăn mòn theo thời gian
- 💡 **Bài học:** AI viết mã rất nhanh – nhưng chọn phương pháp phù hợp với thiết kế thí nghiệm là việc của người làm chuyên môn

**Hình ảnh:** `thuyet-trinh/ket-qua-demo/gia-lap/bieu_do_dong_hoc_an_mon.png`; `du-an-nghien-cuu/05-ket-qua/hinh/do_vs_du_doan.png`; `du-an-nghien-cuu/05-ket-qua/mo-hinh-3d/3D_3_be_mat_tam_thep.png`.

**Demo:** trực tiếp ~3 phút (Câu lệnh 4.2 → 4.3 → 4.4); mở mô hình 3D tương tác (tệp HTML) nếu còn thời gian.

**Nguồn:** G5 · `du-an-nghien-cuu/07-bao-cao/BAO-CAO-TONG-HOP.md`

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 16 – Dựng mô hình 3D mô tả quá trình ăn mòn (3′) 🆕

**Chữ trên slide:**
- **Từ con số đến hình ảnh:** AI viết mã dựng mô hình 3D tương tác – mở bằng trình duyệt, xoay, phóng to, bấm ▶ để xem ăn mòn diễn ra theo từng năm

| Mô hình | Mô tả | Căn cứ |
|---|---|---|
| Mặt đáp ứng | Tốc độ ăn mòn năm đầu theo clorua và thời gian ẩm ướt – Việt Nam, Nga; điểm = số đo thật | Hàm liều – đáp ứng hiệu chỉnh vùng, 387 số đo |
| Diễn tiến theo thời gian | Chiều dày thép mất theo năm và mức clorua | ISO 9224: D = r·t^b, b = 0,523 |
| 🆕 **Quá trình ăn mòn (hoạt hình)** | Khối mẫu thép tại Nha Trang, 0 → 30 năm: bề mặt kim loại hạ dần, lớp gỉ dày lên, hố ăn mòn sâu dần; kèm mặt cắt | D(t) từ số đo r = 40,6 µm/năm; hình dạng gỉ, hố: minh họa |
| 🆕 **So sánh vật liệu** | Thép – kẽm – đồng – nhôm trong cùng cấp ăn mòn C3 | ISO 9223 Bảng 2; ISO 9224 |

- 📊 **Kết quả:**
  - Nha Trang: thép mất trung bình **41 µm** sau 1 năm → **135 µm** sau 10 năm → **245 µm** sau 30 năm (≈ 1.926 g/m²)
  - Cấp C3, sau 30 năm: thép ≈ 218 µm · kẽm ≈ 20 µm · đồng ≈ 9 µm · nhôm ≈ 5 µm
- ⚠ **Ghi rõ trên hình:** phần **định lượng** (số đo, tiêu chuẩn) và phần **minh họa** (tham số giả định: lớp gỉ, hố)

**Hình ảnh:** `du-an-nghien-cuu/05-ket-qua/mo-hinh-3d/3D_4_qua_trinh_an_mon.png` (4 thời điểm + mặt cắt); mở `3D_4_qua_trinh_an_mon_dong.html`, bấm **▶ Chạy**; `3D_5_so_sanh_vat_lieu.html`.

**Demo:** mở tệp HTML, chạy hoạt hình ~1 phút (câu lệnh: `cau-lenh-demo.md` mục 12).

**Nguồn:** N16 · ISO 9223:2012, ISO 9224:2012 (T10, T11) · `du-an-nghien-cuu/04-ma-nguon/05_mo_hinh_3d_qua_trinh.py`

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 17 – Đề tài có dữ liệu mật: AI viết công cụ, máy không Internet xử lý dữ liệu – DEMO 3 (5′) 🆕

**Chữ trên slide:**
- **Nguyên tắc: AI viết công cụ – AI không bao giờ thấy dữ liệu thật**

| Máy có Internet (dùng AI) | | Máy không Internet (dữ liệu mật) |
|---|---|---|
| 1. Chỉ mô tả **cấu trúc** dữ liệu (tên cột, đơn vị) | | |
| 2. AI viết công cụ, sinh **dữ liệu giả**, chạy thử | | |
| 3. Nhà khoa học đọc mã; **quét mã** – không có kết nối mạng | | |
| 4. Đóng gói + **mã băm SHA-256** | ➜ chuyển theo quy định ➜ | 5. Đối chiếu mã băm → chạy với **dữ liệu thật** |
| | | 6. Kết quả **ở lại** máy này |

- 🧪 **Ví dụ:** *Ảnh hưởng của địa hình và khí hậu nhiệt đới đến lộ trình của thiết bị bay không người lái* – công cụ tìm lộ trình tốn ít năng lượng nhất, tránh núi cao, ổ mưa dông, gió mạnh; tính ảnh hưởng của gió, mưa, nhiệt độ – độ ẩm, leo cao
- 📊 **Kết quả với dữ liệu giả lập:**
  - Đường thẳng cắt qua **8 ô cấm bay** → lộ trình vòng qua đèo: 14,5 km, 240 Wh
  - Chiều về ngược gió mùa: **422 Wh – gấp 1,8 lần chiều đi** → không đủ pin, phải đổi phương án
  - Công cụ chạy trong ~3 giây trên máy tính thường, không cần mạng
- ⚠ Chuyển tệp giữa hai máy theo **quy định bảo vệ bí mật nhà nước và quy chế của đơn vị**. Khi công cụ lỗi: tái tạo lỗi bằng dữ liệu giả để hỏi AI – không mang dữ liệu thật ra ngoài.

**Hình ảnh:** sơ đồ hai máy; `thuyet-trinh/ket-qua-demo/may-cach-ly/ban_do_lo_trinh.png`.

**Demo:** ~2 phút – chạy công cụ trên dữ liệu giả, mở báo cáo (câu lệnh: `cau-lenh-demo.md` mục 13; mã: `thuyet-trinh/ma-nguon-demo/may-cach-ly/`).

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 18 – Xây dựng bài báo và báo cáo tổng hợp kết quả (5′)

**Chữ trên slide:**
- 🆕 **Một kết quả – nhiều định dạng công bố:**

| Đích công bố | Yêu cầu đặc thù AI cần làm theo | Ví dụ tạp chí (kiểm tra danh mục hiện hành) |
|---|---|---|
| **Scopus / Web of Science** | Theo "Hướng dẫn tác giả" của từng tạp chí: cấu trúc IMRaD, tóm tắt có cấu trúc, highlights, khai báo dữ liệu, khai báo dùng AI, đóng góp tác giả | Corrosion Science; Materials and Corrosion; npj Materials Degradation; Protection of Metals and Physical Chemistry of Surfaces |
| **Danh mục ВАК (Nga)** | Mã УДК; tóm tắt và từ khóa tiếng Nga + tiếng Anh; tài liệu tham khảo theo ГОСТ Р 7.0.5-2008 (theo quy định từng tạp chí); danh mục chia nhóm К1–К3 | Физикохимия поверхности и защита материалов; Коррозия: материалы, защита |
| **Ei Compendex** (kỹ thuật) | Như Scopus; nhấn mạnh ứng dụng kỹ thuật | Kiểm tra tạp chí trong danh mục Ei |
| **Tạp chí trong nước** | Theo thể lệ tạp chí; danh mục Hội đồng Giáo sư Nhà nước | Tạp chí Khoa học và Công nghệ nhiệt đới (ISSN 0866-7535) |
| **Báo cáo của Trung tâm** | Biểu mẫu báo cáo tổng hợp kết quả, Mẫu 21, 22 | Biểu mẫu Trung tâm |

- ⌨ **Câu lệnh:**
  ```
  Từ kết quả trong dự án, soạn bản thảo cho tạp chí [tên]. Đọc "Hướng dẫn tác giả" tôi tải
  lên; lập bảng kiểm tra từng yêu cầu (đạt / chưa đạt). Với tạp chí ВАК: thêm УДК, tóm tắt
  và từ khóa tiếng Nga – Anh, tài liệu tham khảo theo ГОСТ Р 7.0.5-2008.
  Sau đó đóng vai phản biện khó tính: 5 nhược điểm lớn nhất và cách trả lời.
  ```

**Việc phải làm:** kiểm tra danh mục ВАК hiện hành và nhóm К1–К3 của từng tạp chí; xác nhận "EeiE" trong bản góp ý là Ei Compendex hay danh mục khác.

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 19 – Toàn cảnh: một nhiệm vụ khoa học đi qua AI Agent (2′) – *tổng kết Phần III*

**Chữ trên slide:**

**Hình ảnh (chính):** sơ đồ vòng đời: Tài liệu → Khoảng trống (S12) → Phiếu đề xuất, thuyết minh (S13) → Tiến độ – kinh phí (S14) → Dữ liệu – kết quả, mô hình 3D (S15–S16) → Bài báo – báo cáo (S18); nhánh đề tài mật: công cụ chạy trên máy không Internet (S17); mỗi bước có dấu ✅ "nhà khoa học xác nhận".

> Cùng một dự án, cùng một bộ tài liệu – AI nối các công đoạn; nhà khoa học duyệt ở mỗi bước.

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

# PHẦN IV. SKILL, KHOA HỌC MỞ VÀ TỰ ĐỘNG HÓA (15 phút)

---

## Slide 20 – Skill và khoa học mở: nền móng của tự động hóa (6′)

**Chữ trên slide:**
- **Skill** = hướng dẫn quy trình + tri thức chuyên môn + biểu mẫu + mã; AI tự dùng khi cần, cho kết quả nhất quán
- **Vì sao quan trọng:** biến kinh nghiệm cá nhân thành tài sản chung · chuẩn hóa chất lượng · là "viên gạch" của quy trình tự động
- **Thư viện Skill khoa học mở:** K-Dense Scientific Agent Skills (**177 Skill**, giấy phép MIT, GitHub) · AI4S · AIPOCH · CES Global
- **Chiến lược:** Kế thừa → Bản địa hóa (biểu mẫu, thuật ngữ Việt – Nga – Anh) → Chia sẻ nội bộ

**🆕 Thí nghiệm thật: cùng một bộ dữ liệu – không dùng và có dùng Skill**

Dữ liệu: 387 số đo ăn mòn thép (ISOCORRAG, MICAT, Việt Nam, Nga – kho C-OLR, MIT). Skill: `exploratory-data-analysis` của K-Dense (tải từ GitHub, chạy cục bộ, không cần mạng).

| Câu hỏi kiểm tra | Không dùng Skill (phân tích ban đầu) | Có dùng Skill |
|---|---|---|
| Phân bố số liệu có lệch không? | Không kiểm tra – dùng thang log theo kinh nghiệm | **Có:** độ lệch 4,66 → sau log còn −0,02 → căn cứ định lượng cho thang log |
| Ngoại lệ ảnh hưởng thế nào? | Không báo cáo | **31/387** giá trị ngoài ngưỡng IQR; trung bình 37,7 → 29,2 µm/năm nếu bỏ chúng – **chỉ đánh dấu, không xóa** |
| Tập huấn luyện và kiểm định có trùng trạm không (rò rỉ dữ liệu)? | Không kiểm tra | **Không trùng** – xác nhận kiểm định độc lập là hợp lệ |
| Dữ liệu thiếu theo nhóm, theo tập? | Kiểm tra thủ công | Bảng tự động theo từng nhóm, từng tập |
| Quy tắc an toàn | Tùy người làm | Không tự xóa, không tự điền, không tự biến đổi dữ liệu; không kết luận nhân quả |

> **Kết luận:** Skill **không thay** nhà khoa học – Skill bảo đảm **không bỏ sót bước kiểm tra**, và ai chạy cũng theo cùng một chuẩn.

**Lưu ý:** "Không dùng Skill" là phân tích ban đầu của chính bộ mã nghiên cứu; nên chạy lại thí nghiệm trực tiếp trên Claude (tải Skill dạng ZIP) trước buổi thuyết trình.

**Nguồn:** N18 (Kassis và cs., 2026, arXiv:2609.00065), N17 · kết quả: `du-an-nghien-cuu/05-ket-qua/kiem-tra-bang-skill/`

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 21 – Ứng dụng khoa học mở và tự động hóa từng bước đến toàn trình (5′)

**Chữ trên slide:**

🆕 **Khoa học mở trong thực tế – vòng đời của bộ dữ liệu ăn mòn dùng trong bài này:**

| Bước | Điều đã xảy ra | Nguyên tắc |
|---|---|---|
| 1. Dữ liệu được công bố mở | Nhóm C-OLR công bố 387 số đo + mã trên GitHub, giấy phép MIT | FAIR: dễ tìm, dễ truy cập |
| 2. Người khác tái sử dụng | Bài này tải về, hợp nhất, phân tích lại | Tái sử dụng |
| 3. Phát hiện và sửa lỗi | Phát hiện nhãn đơn vị sai, 2 trạm ghi sai cấp | Kiểm chứng độc lập |
| 4. Tạo tri thức mới | Mô hình quốc tế thấp hơn thực đo ở Việt Nam ~31% | Giá trị gia tăng |
| 5. Đóng góp lại cộng đồng | Đề xuất: báo lỗi cho tác giả; công bố mã và kết quả (GitHub, Zenodo có DOI) | Minh bạch, tái lập |

**Ba mức tự động hóa:**

| Mức | Mô tả | Ví dụ trên Claude |
|---|---|---|
| 1 – Hỗ trợ từng bước | Nhà khoa học giao từng việc | Tóm tắt một bài báo |
| 2 – Bán tự động | Chuỗi Skill chạy liên tiếp, dừng ở điểm xác nhận | Dự án + Skill: tài liệu → ma trận bằng chứng → khoảng trống |
| 3 – Tự động toàn trình | Tự chạy theo lịch hoặc khi có dữ liệu mới | **Tác vụ theo lịch** (Cowork): sáng thứ Hai tự gửi bản tin công bố mới |

**Nguồn:** N19 (FAIR, UNESCO) · N24 · kho C-OLR

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 22 – Bản đồ quy trình tự động của Trung tâm và năm quyết định của nhà khoa học (4′)

**Chữ trên slide:**

| Mã | Quy trình | Kích hoạt | Sản phẩm | Quyết định của nhà khoa học |
|---|---|---|---|---|
| QT-00 | Kiểm soát dữ liệu xanh / vàng / đỏ | Mỗi khi có đầu vào | Nhãn phân loại, nhật ký | **1. Dữ liệu nào được đưa lên AI** |
| QT-01 | Theo dõi công bố khoa học | Hằng tuần | Bản tin theo hướng nghiên cứu | **2. Nguồn nào được chấp nhận** |
| QT-02 | Tổng quan tài liệu, khoảng trống | Khi có ý tưởng | Ma trận bằng chứng | **3. Khoảng trống nào có giá trị** |
| QT-03 | Đề xuất, thuyết minh | Khi khoảng trống được duyệt | Bản nháp biểu mẫu Trung tâm | (3) |
| QT-04 | Xử lý – phân tích dữ liệu | Khi có dữ liệu mới | Báo cáo chất lượng, bảng, biểu đồ, mã | **4. Phương pháp nào phù hợp** |
| QT-05 | Theo dõi tiến độ – kinh phí | Hằng tháng | Báo cáo, cảnh báo chậm mốc | Cán bộ tài chính xác nhận |
| QT-06 | Bài báo, báo cáo tổng kết | Khi có kết quả | Bản thảo, báo cáo tổng hợp | **5. Kết quả được diễn giải thế nào** |

**Hình ảnh (chính):** sơ đồ dòng chảy QT-01 → QT-02 → QT-03 → QT-04 → QT-06, QT-05 chạy song song, tất cả đi qua QT-00; mỗi mũi tên có điểm dừng chờ nhà khoa học duyệt; ảnh chụp bản tin QT-01 chạy thật bằng tác vụ theo lịch.

**Việc phải làm:** chạy thử QT-01 bằng tác vụ theo lịch để có ảnh bản tin thật.

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 23 – Trao đổi và thảo luận (9′)

**Chữ trên slide:**
- Kết quả phiếu khảo sát trước buổi học (biểu đồ)
- Các quy trình các phòng muốn tự động hóa
- Câu hỏi – góp ý – đề xuất thí điểm
- Đầu mối liên hệ: ______________________

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 24 – Phụ lục A: AI lập trình (không trình bày)

**Chữ trên slide:**
- GitHub Octoverse 2025: hơn 180 triệu lập trình viên; hơn 36 triệu người mới trong một năm; 630 triệu kho mã; gần 1 tỷ lần đẩy mã; 4,3 triệu dự án AI
- Stack Overflow 2025: 84% lập trình viên dùng hoặc dự định dùng AI; 51% lập trình viên chuyên nghiệp dùng hằng ngày
- SWE-bench Verified (năng lực sửa lỗi phần mềm thật) tăng mạnh trong một năm – *kiểm tra số liệu trong bản gốc AI Index 2026 trước khi dùng*
- Các AI Agent lập trình: Claude Code, OpenAI Codex, GitHub Copilot, Cursor

**Nguồn:** N1, N11, N13

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 25 – Phụ lục B: Ví dụ Google và các nhà khoa học dùng AI (không trình bày – dự phòng khi được hỏi)

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

## Slide 26 – Phụ lục C: Nguồn tham khảo (không trình bày)

**Chữ trên slide:** danh mục nguồn theo Mục 11 của kế hoạch – 5 công bố ví dụ ở Phụ lục B (kèm DOI), số liệu bối cảnh, pháp lý Việt Nam, tiêu chuẩn ISO 9223 / 9224, khoa học mở.

**Đã xác minh (v2.4):** arXiv 2609.00065 = Kassis T., Agarwal V., He Y., Patel D., Brueckner A.M. (2026). *Scientific Agent Skills: A Library of Procedural Knowledge for Research Agents* (N18).

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Slide 27 – Phụ lục D: Dự án và bộ Skill khoa học mở (không trình bày)

**Chữ trên slide:** K-Dense Scientific Agent Skills – https://github.com/K-Dense-AI/claude-scientific-skills (177 Skill, MIT; sinh học, hóa học, vật liệu, thống kê, viết khoa học…) · AI4S Open Science · AIPOCH Open Science · CES Global – kèm URL và lĩnh vực của từng bộ.

**Việc phải làm:** bổ sung URL của AI4S, AIPOCH, CES Global (N17).

**Duyệt:** [ ] Duyệt · [ ] Sửa · [ ] Bỏ
**Ghi chú:**

---

## Ý KIẾN CHUNG CỦA NGƯỜI DUYỆT

- Bố cục và thời lượng:
- Nội dung cần thêm:
- Nội dung cần bớt:
- Người duyệt: ______________________ · Ngày: ____ / ____ / 2026
