# TÀI LIỆU PHÁT TAY

**AI Agent và sự chuyển đổi phương thức nghiên cứu khoa học** · Trung tâm Nhiệt đới Việt – Nga · 2026

Tài liệu gồm các nội dung chi tiết không chiếu trên slide. Câu lệnh mẫu đầy đủ kèm kết quả mong đợi: `cau-lenh-demo.md`.

---

## 1. Chọn công cụ theo 5 bậc công việc (Slide 5)

| Bậc | Loại việc | Công việc thường gặp của nhà khoa học | Công cụ phù hợp |
|---|---|---|---|
| 1 | Hỏi – đáp, tra cứu nhanh | Giải thích khái niệm, tiêu chuẩn (ISO 9223 cấp C4 là gì?) · Dịch thuật ngữ Việt – Nga – Anh · Gợi ý từ khóa tìm tài liệu · Kiểm tra công thức, đơn vị | Chatbot |
| 2 | Làm việc với một tài liệu | Tóm tắt bài báo · Dịch bài báo tiếng Nga/Anh · Trích bảng số liệu từ PDF · Sửa văn phong, rút gọn tóm tắt · Soạn công văn, thư mời hội thảo | Chatbot |
| 3 | Tổng hợp nhiều nguồn | Tổng quan tài liệu, ma trận bằng chứng · Tìm khoảng trống nghiên cứu · So sánh tiêu chuẩn Việt Nam – Nga (ГОСТ) – quốc tế · Bản tin công bố mới theo chủ đề | Chatbot có dự án / Research |
| 4 | Xử lý nhiều tệp, dữ liệu | Làm sạch, gộp số liệu từ nhiều trạm · Thống kê, hồi quy, vẽ biểu đồ · Điền biểu mẫu thuyết minh từ bộ hồ sơ · Lập dự toán, sơ đồ tiến độ | AI Agent |
| 5 | Chuỗi nhiệm vụ, tự động hóa | Dữ liệu → mô hình → biểu đồ → bản thảo bài báo · Bộ hồ sơ nghiệm thu (Mẫu 21, 22) · Theo dõi tiến độ hằng tháng · Bản tin tự động hằng tuần | AI Agent + Skill + lịch tự động |

## 2. Chatbot và AI Agent khác nhau thế nào (Slide 3, 5)

| | Chatbot AI | AI Agent |
|---|---|---|
| Đầu vào | Một câu hỏi | Một nhiệm vụ có mục tiêu |
| Lập kế hoạch | Hạn chế | Tự lập và điều chỉnh |
| Công cụ | Ít | Tìm kiếm, chạy mã, làm việc với tệp |
| Kiểm tra kết quả | Người dùng tự làm | Tự kiểm tra từng bước – vẫn cần người xác nhận |
| Chi phí – thời gian | Thấp | Cao hơn |

## 3. Tính năng mới của AI Agent 2024–2026 (Slide 3)

| Tính năng | Làm được gì cho nhà khoa học | Mốc |
|---|---|---|
| **Làm việc tự chủ nhiều giờ** | Giao cả chuỗi việc (đọc dữ liệu → phân tích → vẽ biểu đồ → viết báo cáo); AI tự làm, tự sửa lỗi | Độ dài việc AI làm được: ~1 giờ (02/2025) → ≥ 16 giờ (05/2026) |
| **Nghiên cứu chuyên sâu (Deep Research)** | Tự tìm, đọc hàng chục – hàng trăm nguồn, viết báo cáo có trích dẫn | Google 12/2024 · OpenAI 02/2025 · Claude 04/2025 |
| **Sử dụng máy tính** | Tự nhìn màn hình, bấm chuột, gõ phím – thao tác trên trang web, phần mềm như người dùng | Anthropic thử nghiệm công khai 10/2024 |
| **Kết nối chuẩn mở MCP** | Một "ổ cắm chung" để AI kết nối cơ sở dữ liệu, kho tài liệu, phần mềm | Ra mắt 11/2024; > 10.000 máy chủ kết nối công khai; chuyển cho Linux Foundation 12/2025 |
| **Skill – chuẩn mở** | Quy trình mẫu đóng gói một lần, dùng được trên nhiều công cụ AI khác nhau | Chuẩn mở 12/2025 (agentskills.io) |
| **Chạy nền, theo lịch** | Tự chạy định kỳ (ví dụ: bản tin công bố mới mỗi sáng thứ Hai) – không cần ngồi canh | Tác vụ theo lịch trong Cowork (Claude cho Windows, 04/2026) |

## 4. Claude trên Windows – đầy đủ tính năng (Slide 7)

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

## 5. Bắt đầu với Claude – 6 bước (Slide 8)

| Bước | Làm gì | Ở đâu |
|---|---|---|
| 1. Tạo tài khoản | Đăng nhập bằng email trên trình duyệt; nếu muốn, cài ứng dụng Claude cho Windows | claude.ai · claude.com/download |
| 2. Cài đặt quyền riêng tư **trước tiên** | Chọn có cho dùng hội thoại để cải thiện mô hình hay không; xem và sửa "bộ nhớ" Claude lưu về bạn | Settings → Privacy · Settings → Capabilities |
| 3. Hỏi đáp và tải tệp | Gõ câu hỏi; kéo thả PDF, Word, Excel, ảnh vào khung chat; chọn mô hình | Màn hình chính |
| 4. Bật công cụ | Tìm kiếm web; viết và chạy mã, tạo tệp; Research (gói Pro trở lên) | Settings → Capabilities, hoặc nút công cụ trong khung chat |
| 5. Tạo Dự án (Project) | Viết hướng dẫn chung một lần + tải bộ tài liệu dùng chung cho mọi cuộc trò chuyện trong dự án | Mục Projects |
| 6. Nhận sản phẩm | Văn bản, bảng, biểu đồ hiện ngay bên cạnh; tải về Word, Excel, PowerPoint, PDF | Khung kết quả bên phải |

**3 thói quen tốt:** nói rõ việc cần làm và dạng kết quả · yêu cầu dẫn nguồn · luôn kiểm tra lại trước khi dùng.

## 6. Giao việc cho AI Agent – mẫu 5 bước (Slide 9)

1. **Xác định nhiệm vụ** – làm gì, để làm gì
2. **Cung cấp dữ liệu** – theo quy tắc xanh / vàng / đỏ
3. **Quy định đầu ra** – dạng bảng, văn bản, biểu đồ, độ dài
4. **Yêu cầu dẫn nguồn, lưu mã** – để kiểm tra và tái lập
5. **Kiểm tra và xác nhận** – nhà khoa học duyệt

Ví dụ đủ 5 bước:
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

## 7. Bộ tài liệu thật dùng trong ví dụ ăn mòn khí quyển (Slide 12)

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

Danh mục đầy đủ 13 tài liệu đã xác minh: `du-an-nghien-cuu/01-tong-quan-tai-lieu/DANH-MUC-TAI-LIEU.csv`.

## 8. Thí nghiệm: không dùng và có dùng Skill (Slide 24)

| Câu hỏi kiểm tra | Không dùng Skill (phân tích ban đầu) | Có dùng Skill |
|---|---|---|
| Phân bố số liệu có lệch không? | Không kiểm tra – dùng thang log theo kinh nghiệm | **Có:** độ lệch 4,66 → sau log còn −0,02 → căn cứ định lượng cho thang log |
| Ngoại lệ ảnh hưởng thế nào? | Không báo cáo | **31/387** giá trị ngoài ngưỡng IQR; trung bình 37,7 → 29,2 µm/năm nếu bỏ chúng – **chỉ đánh dấu, không xóa** |
| Tập huấn luyện và kiểm định có trùng trạm không (rò rỉ dữ liệu)? | Không kiểm tra | **Không trùng** – xác nhận kiểm định độc lập là hợp lệ |
| Dữ liệu thiếu theo nhóm, theo tập? | Kiểm tra thủ công | Bảng tự động theo từng nhóm, từng tập |
| Quy tắc an toàn | Tùy người làm | Không tự xóa, không tự điền, không tự biến đổi dữ liệu; không kết luận nhân quả |

## 9. Dữ liệu mật: AI viết công cụ, máy không kết nối Internet xử lý (Slide 20–23)

**Căn cứ:** Luật Bảo vệ bí mật nhà nước số 117/2025/QH15 (hiệu lực 01/3/2026), Điều 5 nghiêm cấm: soạn thảo, lưu giữ tài liệu có nội dung bí mật nhà nước trên thiết bị đang kết nối Internet, mạng máy tính, mạng viễn thông (trừ mạng LAN độc lập theo quy định); sử dụng hệ thống trí tuệ nhân tạo, công nghệ mới để xâm phạm bí mật nhà nước. *Đối chiếu khoản cụ thể trong văn bản chính thức.*

| Được đưa cho AI trực tuyến | Không bao giờ đưa |
|---|---|
| Cấu trúc dữ liệu với tên cột trung tính | Giá trị số liệu thật, tọa độ, bản đồ, ảnh |
| Bài toán mô tả ở dạng tổng quát | Tên đơn vị, phiên hiệu, khu vực, mục đích nhiệm vụ |
| Dữ liệu giả do AI sinh ra | Thông số kỹ thuật thật của vũ khí, trang bị |
| Thông báo lỗi đã tái tạo trên dữ liệu giả | Ảnh chụp màn hình, nhật ký lỗi, tệp kết quả từ máy mật |

**Quy trình 6 bước – ba vùng (luồng một chiều: chỉ mã đi vào, không gì đi ra):**

| Vùng | Bước | Điểm kiểm soát |
|---|---|---|
| A. Máy có Internet | 1. Mô tả cấu trúc dữ liệu, bài toán tổng quát | Rà soát mô tả theo bảng trên |
| | 2. AI viết công cụ, sinh dữ liệu giả, chạy thử | Chỉ thư viện được phép |
| | 3. Đọc mã; quét mã | Không thư viện mạng, lệnh hệ thống, địa chỉ web |
| | 4. Đóng gói + mã băm SHA-256 | Ghi sổ danh sách tệp, mã băm |
| B. Chuyển giao | 5. Chép sang máy mật | Thiết bị được cấp phép, quét mã độc, đối chiếu mã băm |
| C. Máy không kết nối Internet / LAN độc lập | 6. Chạy với dữ liệu thật | Báo cáo ghi mã băm dữ liệu; kết quả lưu tại chỗ |

**Năm sai lầm dễ làm lộ dữ liệu:** (1) chụp màn hình, dán trích đoạn tài liệu mật để hỏi AI; (2) dùng Cowork, tiện ích AI trên trình duyệt, tính năng sử dụng máy tính trên máy có tài liệu mật; (3) bật đồng bộ đám mây hoặc Kết nối (Connectors) trên máy đó; (4) mang nhật ký lỗi, kết quả từ máy mật ra máy có Internet; (5) dùng tài khoản AI cá nhân cho công việc nội bộ.

Mã mẫu: `ma-nguon-demo/may-cach-ly/` (hướng dẫn trong `README.md`).

## 11. Tìm và lọc tài liệu bước đầu (Slide 12)

**Quy trình 4 bước:** (1) đặt câu hỏi, tìm bài ứng viên → (2) lọc theo tiêu đề, tóm tắt → (3) lấy toàn văn → (4) đưa vào dự án Claude, lập ma trận bằng chứng.

**Dùng Sci-Bot để tìm bài ứng viên (bước 1):**
1. Mở Sci-Bot (địa chỉ báo chí đưa tin: sci-bot.ru – kiểm tra địa chỉ chính thức trước khi dùng).
2. Đặt **một** câu hỏi bằng tiếng Anh, nêu rõ đối tượng – điều kiện – yếu tố cần xét. Ví dụ: *"Which environmental factors control the first-year atmospheric corrosion rate of carbon steel in tropical climates, and how accurate is the ISO 9223 dose-response function there?"*
3. Đọc câu trả lời; chép danh sách bài báo được trích kèm DOI vào bảng (tác giả, năm, tên bài, DOI).
4. Hỏi tiếp bằng câu hỏi mới (Sci-Bot không nhớ câu trước) – mỗi khía cạnh một câu: yếu tố môi trường, mô hình dự báo, dữ liệu Việt Nam, dữ liệu Nga…
5. Bổ sung bài mới (sau ~2021–2022) bằng Google Scholar Labs hoặc Semantic Scholar.

**Dùng Sci-Hub để lấy toàn văn (bước 3):** dán DOI (hoặc tiêu đề) vào ô tìm kiếm → mở hoặc tải PDF; nếu không có, thử Unpaywall, CORE, thư viện của đơn vị hoặc gửi thư xin tác giả.

**Lọc bài bằng Claude (bước 2):** tải danh sách bài (tiêu đề, tóm tắt, DOI) vào dự án → dùng câu lệnh `cau-lenh-demo.md` mục 14.

**Lưu ý:** Sci-Hub, Sci-Bot đang có tranh chấp bản quyền ở nhiều nước (đã bị chặn ở Nga, Ấn Độ…); nhiều trang giả mạo – chỉ dùng địa chỉ chính thức, không tải tệp chạy (.exe); không dùng trên máy có tài liệu mật; tuân thủ quy định truy cập Internet của đơn vị. Luôn kiểm tra DOI của mọi bài AI trích dẫn.

**Các công cụ khác:**

| Công cụ | Là gì | Cách dùng | Lưu ý |
|---|---|---|---|
| **Unpaywall** | Tiện ích trình duyệt, cơ sở dữ liệu bản mở hợp pháp | Cài vào Chrome/Edge/Firefox → nút xanh hiện khi bài báo có bản mở | Tìm được bản mở cho khoảng một nửa số yêu cầu |
| **CORE** | Kho tổng hợp bài báo truy cập mở từ các kho lưu trữ của trường, viện | core.ac.uk – tìm theo từ khóa, DOI | Hơn 100 triệu bài (con số thay đổi – xem trang) |
| **arXiv · PubMed Central · DOAJ** | Bản thảo trước công bố (vật lý, toán, tin học…) · bài y sinh toàn văn · danh mục tạp chí truy cập mở | Tìm trực tiếp trên trang | Bản arXiv có thể chưa qua phản biện |
| **Google Scholar Labs** | Chế độ tìm kiếm có AI của Google Scholar (11/2025): phân tích câu hỏi chi tiết, giải thích vì sao mỗi bài liên quan, cho hỏi tiếp | scholar.google.com → Scholar Labs; cần đăng nhập | Thử nghiệm; câu hỏi tiếng Anh |
| **Semantic Scholar** | Công cụ tìm kiếm bài báo miễn phí, có tóm tắt một dòng (TLDR), bản đồ trích dẫn | semanticscholar.org | Miễn phí |
| **Elicit · Consensus** | Tìm và trích xuất bảng từ bài báo; trả lời có dẫn chứng | Đặt câu hỏi nghiên cứu → bảng bài báo, trích dẫn | Bản miễn phí có giới hạn |
| **SciSpace** | Tìm bài, đọc và giải thích bài báo bằng AI | Tải PDF hoặc tìm theo câu hỏi | Kiểm tra giải thích với bản gốc |
| **Undermind** | Tác tử tìm kiếm chuyên sâu: tìm tuần tự, tổng hợp kỹ | Mô tả nhu cầu chi tiết → chờ vài phút | Chậm hơn nhưng đầy đủ hơn |
| **Scopus AI · Web of Science Research Assistant** | AI trên cơ sở dữ liệu Scopus, Web of Science | Qua tài khoản thư viện, tổ chức | Chỉ tìm trong tạp chí được hai cơ sở dữ liệu này chỉ mục |
| **VJOL** | Cơ sở dữ liệu tạp chí khoa học Việt Nam, do Cục Thông tin, Thống kê KH&CN quốc gia quản lý | Tìm bài tiếng Việt, xem miễn phí | Kiểm tra tên miền hiện hành |
| **CyberLeninka** | Thư viện khoa học truy cập mở của Nga | Tìm bài tiếng Nga, đọc toàn văn | Phù hợp tài liệu Nga về ăn mòn, nhiệt đới hóa |
| **eLIBRARY.ru** | Thư viện điện tử khoa học Nga, nền của chỉ số trích dẫn РИНЦ | Đăng ký miễn phí; một phần toàn văn mở | Kiểm tra tạp chí trong danh mục ВАК |

**Khi không có bản mở:** gửi thư cho tác giả liên hệ (đa số tác giả sẵn lòng gửi PDF) · nhờ thư viện của đơn vị · tìm bản tác giả trên trang cá nhân, kho của trường.

## 12. Xử lý dữ liệu với AI – quy trình 5 bước (Slide 15)

| Bước | AI làm | Nhà khoa học kiểm soát |
|---|---|---|
| 1. Chuẩn bị dữ liệu | Đọc tệp, mô tả cấu trúc: số dòng, tên cột, đơn vị, nguồn | Giữ bản gốc chỉ đọc; lập từ điển dữ liệu; chỉ đưa dữ liệu được phép |
| 2. Kiểm tra chất lượng | Tìm dòng trùng, ô trống, sai định dạng, sai đơn vị, giá trị bất thường → báo cáo | Chỉ đánh dấu, không tự xóa; quyết định giữ / loại |
| 3. Phân tích, lập mô hình | Viết và chạy mã Python: thống kê, hồi quy, mô hình theo tiêu chuẩn | Chọn phương pháp phù hợp thiết kế thí nghiệm; nêu rõ giả định |
| 4. Kiểm định kết quả | Tách tập kiểm định độc lập, tính sai số, so với tiêu chuẩn, số liệu đã công bố | Đánh giá kết quả có hợp lý về chuyên môn |
| 5. Lưu trữ, tái lập | Lưu mã, dữ liệu đã xử lý, nhật ký từng bước | Chạy lại ra cùng kết quả; lưu theo cấu trúc dự án |

Mẫu câu lệnh:
```
Tôi tải lên [tệp dữ liệu]. Làm lần lượt, dừng sau mỗi bước để tôi xác nhận:
1. Mô tả cấu trúc dữ liệu (số dòng, cột, đơn vị); 2. Kiểm tra chất lượng – chỉ đánh dấu,
không xóa; 3. Đề xuất phương pháp phân tích và giải thích vì sao; 4. Phân tích, kiểm định
trên tập độc lập; 5. Lưu toàn bộ mã Python và nhật ký để chạy lại.
```

## 10. Giải nghĩa thuật ngữ

| Thuật ngữ | Nghĩa |
|---|---|
| AI tạo sinh | AI tạo ra văn bản, hình ảnh, mã… từ yêu cầu bằng lời |
| Chatbot | Trợ lý AI hỏi – đáp: một câu hỏi, một câu trả lời |
| AI Agent (tác tử AI) | AI nhận một nhiệm vụ, tự lập kế hoạch, dùng công cụ (tìm kiếm, chạy mã, đọc – ghi tệp), kiểm tra từng bước |
| Mô hình (Haiku, Sonnet, Opus, Fable) | "Bộ não" của Claude; mô hình lớn hơn suy luận tốt hơn nhưng chậm, tốn hơn |
| Dự án (Project) | Không gian làm việc gom tài liệu + hướng dẫn chung cho một nhiệm vụ |
| Research / Deep Research | Chế độ nghiên cứu chuyên sâu: AI tự tìm, đọc nhiều nguồn, viết báo cáo có trích dẫn |
| Kết nối (Connectors) | Cho AI đọc dữ liệu ở dịch vụ khác (Google Drive, Gmail…) với quyền của người dùng |
| MCP | Chuẩn mở để AI kết nối với cơ sở dữ liệu, phần mềm – "ổ cắm chung" |
| Bộ nhớ (Memory) | AI nhớ bối cảnh làm việc giữa các cuộc trò chuyện; người dùng xem, sửa được |
| Skill (kỹ năng) | Quy trình mẫu đóng gói (hướng dẫn + biểu mẫu + mã) để AI dùng lại, cho kết quả nhất quán |
| Subagent (tác tử con) | Trợ lý con được giao một việc chuyên biệt trong nhiệm vụ lớn |
| Hệ nhiều Agent | Nhiều trợ lý phối hợp như một nhóm: đề xuất, phản biện, tổng hợp |
| Cowork | Chế độ của ứng dụng Claude cho Windows làm việc trực tiếp với thư mục trên máy |
| Tác vụ theo lịch | Việc AI tự chạy định kỳ, không cần người ngồi canh |
| Plugin | Gói nhiều Skill + kết nối + tác tử con, cài một lần dùng cho cả nhóm |
| Hàm liều – đáp ứng | Công thức tính tốc độ ăn mòn từ các yếu tố môi trường (ISO 9223) |
| Mã băm SHA-256 | "Dấu vân tay" của tệp – chỉ cần sửa một ký tự là mã băm thay đổi |
| FAIR | Nguyên tắc dữ liệu khoa học: dễ tìm, dễ truy cập, tương thích, tái sử dụng được |

---

*Ghi chú phiếu khảo sát:* trước buổi – đã dùng AI chưa, dùng làm gì, lo ngại gì; sau buổi – 3 câu kiểm tra (chatbot hay Agent? dữ liệu nào được đưa lên AI? ai chịu trách nhiệm kết quả?) và "Tuần tới tôi sẽ thử…".
