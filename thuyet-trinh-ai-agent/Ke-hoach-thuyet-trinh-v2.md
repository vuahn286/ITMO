# KẾ HOẠCH CHI TIẾT BÀI THUYẾT TRÌNH (v2.0)

**Chủ đề:** AI Agent và sự chuyển đổi phương thức nghiên cứu khoa học
**Thời lượng:** 120 phút
**Đối tượng:** Cán bộ, nhà khoa học tại Trung tâm Nhiệt đới Việt – Nga
**Định hướng:** Nhận thức là chính, lý thuyết vừa đủ, có ví dụ thực tế và demo. Nhấn mạnh năng lực cốt lõi và ưu điểm của AI. Không đi sâu kỹ thuật xây dựng Agent.
**Tình huống xuyên suốt (đã chốt):** **Phương án A – Ăn mòn khí quyển của kim loại trong môi trường nhiệt đới.**
**Ngày thuyết trình:** ____ / ____ / ______
**Phiên bản:** 2.2 – 21/10/2026 (rà soát ngôn ngữ và độ chính xác; xem Mục 0 và `RA-SOAT-v2.md`)

> **Bản v2.2 (21/10/2026) – bố cục slide mới, xem `DANH-SACH-SLIDE.md` (tệp này là bố cục chính thức):**
> - **Bỏ Slide 2** (ví dụ Google) khỏi phần trình bày; nội dung chuyển xuống **Phụ lục B** để dùng khi được hỏi. Hai ví dụ AI co-scientist và ERA vẫn được nêu tại slide tài liệu (mới 11) và slide Demo 2 (mới 14).
> - **Tách Slide 17** (năm quyết định): 5 quyết định gộp vào slide tự động hóa (mới 17) như 5 điểm phê duyệt; căn cứ pháp lý gộp vào slide giao việc (mới 7); thông điệp Phần III chuyển sang slide bài báo (mới 15).
> - Còn **20 slide trình bày + 4 phụ lục**. Nội dung chi tiết ở Mục 3 dưới đây vẫn đánh số theo v2.1 – đối chiếu bằng bảng sau:
>
> | Số v2.1 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |
> |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
> | **Số v2.2** | 1 | PL-B (22) | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | gộp vào 7, 15, 17 | 16 | 17 | 18 | 19 | 20 | PL-A (21) | PL-C (23) | PL-D (24) |

**Tài liệu đi kèm trong cùng thư mục:**

| Tệp | Nội dung |
|---|---|
| `cau-lenh-demo.md` | Toàn bộ câu lệnh để sao chép – dán vào Claude, kèm kết quả mong đợi |
| `du-lieu-demo/an_mon_tho.csv` | 253 dòng số liệu cân mẫu (3 trạm × 4 kim loại × 7 mốc × 3 mẫu lặp + 1 dòng trùng), **cài sẵn 14 lỗi** để AI phát hiện |
| `du-lieu-demo/khi_tuong_tram.csv` | 108 dòng khí tượng – môi trường theo tháng (T, RH, mưa, TOW, Cl⁻, SO₂), có ô trống |
| `du-lieu-demo/ke_hoach_cong_viec.csv` | 7 nội dung công việc, tiến độ, kinh phí – **cài sẵn 3 điểm bất hợp lý** |
| `ma-nguon/phan_tich_an_mon.py`, `ma-nguon/ve_gantt.py` | Mã phân tích tái lập (loại mã AI tự viết trong demo) |
| `ket-qua-mau/` | Kết quả đã chạy thử: báo cáo chất lượng dữ liệu, mô hình, biểu đồ, Gantt |

> ⚠ **Toàn bộ dữ liệu demo là dữ liệu GIẢ LẬP** (nhóm xanh), được sinh có chủ đích để minh họa; không phải số liệu đo của bất kỳ trạm thật nào. Trên slide luôn ghi "dữ liệu giả lập".

---

## MỤC LỤC

0. [Những thay đổi so với v1.0](#0-những-thay-đổi-so-với-v10)
1. [Thông điệp và nguyên tắc chung](#1-thông-điệp-và-nguyên-tắc-chung)
2. [Phân bổ thời gian](#2-phân-bổ-thời-gian)
3. [Nội dung chi tiết từng slide](#3-nội-dung-chi-tiết-từng-slide)
4. [Tình huống xuyên suốt và kịch bản demo](#4-tình-huống-xuyên-suốt-và-kịch-bản-demo)
5. [Hệ thống quy trình tự động tại Trung tâm (đề xuất)](#5-hệ-thống-quy-trình-tự-động-tại-trung-tâm-đề-xuất)
6. [Quy tắc phân loại dữ liệu xanh / vàng / đỏ](#6-quy-tắc-phân-loại-dữ-liệu-xanh--vàng--đỏ)
7. [Bảng căn cứ – số liệu đã xác minh](#7-bảng-căn-cứ--số-liệu-đã-xác-minh)
8. [Kế hoạch thực hiện theo giai đoạn](#8-kế-hoạch-thực-hiện-theo-giai-đoạn)
9. [Tài liệu đi kèm](#9-tài-liệu-đi-kèm)
10. [Phương án dự phòng](#10-phương-án-dự-phòng)
11. [Nguồn tham khảo](#11-nguồn-tham-khảo)
12. [Giải nghĩa thuật ngữ](#12-giải-nghĩa-thuật-ngữ-cho-người-trình-bày)

---

## 0. NHỮNG THAY ĐỔI SO VỚI v1.0

| # | Thay đổi | Lý do |
|---|---|---|
| 1 | **Slide 2 mới: "Mới đây: các nhà khoa học Google dùng AI giải bài toán khoa học thật"** – 5 ví dụ có công bố khoa học | Bổ sung ví dụ thực tế theo yêu cầu |
| 2 | **AI lập trình không còn là slide chính.** Chỉ còn một ô nhỏ trong Slide 4; số liệu GitHub/Stack Overflow chuyển xuống phụ lục (Slide 23) | Theo yêu cầu: AI lập trình là phần phụ |
| 3 | Ý "nhà khoa học dùng AI viết và chạy mã để xử lý dữ liệu" được đặt ở **Slide 15**, mở đầu bằng ví dụ thật của Google (Nature, 05/2026) rồi vào Demo 2 | Giữ ý chính, đặt đúng chỗ |
| 4 | Slide 12–16 trình bày theo khung: **ví dụ thực tế → câu lệnh → dữ liệu → kết quả mong đợi → gợi ý lời nói → điểm xác nhận** | Theo yêu cầu: có câu lệnh, dữ liệu, gợi ý nói |
| 5 | Chốt tình huống A; **đã dựng dữ liệu, đã chạy thử, có kết quả mẫu** | Demo chạy được ngay trên Claude |
| 6 | Cập nhật số liệu METR đến 2026 (v2.1: đính chính – câu "~4 tháng từ 2023" của v1 **có căn cứ**: METR Time Horizon 1.1 cho 131 ngày ≈ 4,3 tháng kể từ 2023); SWE-bench ghi đúng theo AI Index | Căn cứ phải chính xác |
| 7 | Mục 7 chuyển từ "danh mục cần xác minh" thành **bảng căn cứ đã xác minh**, có nguồn gốc cho từng số liệu | Căn cứ đầy đủ |
| 8 | **v2.1:** Viết lại Slide 1 bằng lời thường (câu "53% dân số" sửa theo nguyên văn nguồn); thêm phần "giải thích dễ hiểu" cho 5 ví dụ Slide 2; Slide 3 bỏ thuật ngữ (embedding, VLA…); sửa "hàm mũ" → "hàm lũy thừa"; nêu rõ ERA là đánh giá hồi cứu; sửa trích dẫn Penadés; thêm ô "Kết quả với dữ liệu thật" ở Slide 15; thêm Mục 12 – Giải nghĩa thuật ngữ | Rà soát ngày 21/10/2026 |
| 9 | **v2.2:** Bỏ slide ví dụ Google (chuyển Phụ lục B); tách slide "Năm quyết định" vào 3 slide phù hợp; chia lại thời lượng; bố cục chính thức chuyển sang `DANH-SACH-SLIDE.md` | Theo ý kiến duyệt ngày 21/10/2026 |

---

## 1. THÔNG ĐIỆP VÀ NGUYÊN TẮC CHUNG

### Thông điệp tổng thể
> AI đang chuyển từ công cụ trả lời sang năng lực hỗ trợ thực hiện công việc khoa học – và đã cùng nhà khoa học tạo ra những kết quả được công bố trên *Nature*, *Science*, *Cell*. Giá trị không nằm ở việc dùng thật nhiều AI, mà ở chọn đúng nhiệm vụ, tổ chức đúng quy trình và giữ trách nhiệm khoa học.

### Thông điệp từng phần
| Phần | Thông điệp |
|---|---|
| I | AI không thay thế nhà khoa học; AI đang thay đổi cách nhà khoa học đặt giả thuyết, xử lý dữ liệu và kiểm chứng kết quả. |
| II | Công cụ tốt nhất là công cụ phù hợp với nhiệm vụ, dữ liệu, chi phí và mức độ kiểm soát cần thiết. |
| III | AI Agent nối tài liệu, dữ liệu, biểu mẫu và sản phẩm thành một quá trình liên tục; các quyết định khoa học thuộc về nhà nghiên cứu. |
| IV | Đóng gói kinh nghiệm thành Skill, kế thừa khoa học mở, nối thành quy trình tự động; nhà khoa học đặt mục tiêu và phê duyệt. |

### Nguyên tắc trình bày
- **Giọng điệu tích cực:** tập trung vào năng lực và ưu điểm; vai trò nhà khoa học là *định hướng và xác nhận*.
- **Mỗi slide một ý chính, một con số hoặc một hình nổi bật.**
- **Mọi số liệu có nguồn ở chân slide** (mã nguồn theo Mục 7, ví dụ "[N3]").
- **Nói đúng mức:** "kiểm chứng trong phòng thí nghiệm" ≠ "đã chữa được bệnh"; "trùng với kết quả chưa công bố" ≠ "phát hiện mới". Cách nói chuẩn ghi ở từng ví dụ.
- **Biểu mẫu (01A, 07, 08, 21, 22) là sản phẩm đầu ra**, không phải trục chính.
- **Trung lập về công cụ:** Claude là ví dụ minh họa, luôn kèm công cụ tương đương.
- Ghi thời điểm số liệu ("cập nhật 10/2026").

---

## 2. PHÂN BỔ THỜI GIAN

| Phần | Nội dung | Slide (v2.2) | Thời lượng |
|---|---|---|---|
| I | Tổng quan: AI và sự thay đổi nghiên cứu khoa học | 1–4 | 18 phút |
| II | Lựa chọn và sử dụng công cụ AI phù hợp | 5–9 | 31 phút |
| III | AI Agent trong vòng đời nhiệm vụ khoa học (2 demo) | 10–15 | 41 phút |
| IV | Skill, khoa học mở, tự động hóa và năm quyết định của nhà khoa học | 16–19 | 18 phút |
| – | Trao đổi, thảo luận | 20 | 12 phút |
| – | Phụ lục (không trình bày) | 21–24 | – |
| | **Tổng cộng** | **20 slide + 4 phụ lục** | **120 phút** |

*v2.2: 11 phút có được khi bỏ slide ví dụ Google (7′) và slide năm quyết định (4′) được chia lại: +2′ cho mỗi demo, +1′ slide tài liệu, +1′ slide giao việc (thêm căn cứ pháp lý), +3′ slide tự động hóa (thêm năm quyết định), +2′ thảo luận.*

Phần I chi tiết (v2.2): Slide 1 (4′) – Slide 2 (5′) – Slide 3 (5′) – Slide 4 (4′).

---

## 3. NỘI DUNG CHI TIẾT TỪNG SLIDE

### PHẦN I. TỔNG QUAN (25 phút – 5 slide)

---

#### Slide 1 – AI đang phát triển nhanh đến mức nào? (4 phút)

**Nội dung chính (viết trên slide đúng như dưới đây – ngắn, không thuật ngữ):**

| Ô số liệu | Chữ trên slide | Lời nói giải thích |
|---|---|---|
| **≈ 1/2** | "Chỉ 3 năm sau khi ra mắt đại chúng, **khoảng một nửa dân số** đã dùng AI tạo sinh – nhanh hơn tốc độ phổ cập của máy tính cá nhân và Internet." [N1] | "AI tạo sinh là loại AI viết được văn bản, vẽ hình… như ChatGPT, Gemini, Claude. ChatGPT ra mắt cuối 2022; đến năm 2025, theo ước tính của Đại học Stanford, khoảng 53% dân số đã dùng. Máy tính cá nhân và Internet mất nhiều năm hơn để phổ biến đến mức đó. Tỷ lệ này chênh lệch lớn giữa các nước." |
| **5/6 bài** | "AI giải được **5/6 bài thi Olympic Toán quốc tế 2025** – đạt mức huy chương vàng." [N2] | "Đây là kỳ thi dành cho học sinh giỏi toán nhất thế giới; AI viết lời giải bằng ngôn ngữ tự nhiên, được chấm như thí sinh (35/42 điểm). Cả Google và OpenAI đều công bố kết quả này." |
| **Vài giây → hơn 16 giờ** | "AI tự làm được những việc mà chuyên gia cần: **vài giây** (2019) → **gần 1 giờ** (đầu 2025) → **khoảng 12 giờ** (đầu 2026) → **hơn 16 giờ** (giữa 2026). Từ 2024, cứ khoảng **3–4 tháng** độ dài này lại **tăng gấp đôi**." [N3] | "Độ dài công việc được đo bằng thời gian một chuyên gia cần để làm xong; AI được tính là 'làm được' nếu thành công ít nhất một nửa số lần. Giai đoạn 2019–2025, cứ 7 tháng tăng gấp đôi; từ 2024 tốc độ nhanh gấp đôi. Đến giữa 2026, mô hình mạnh nhất đã vượt quá khả năng đo của bộ bài kiểm tra (16 giờ)." |

> ⚠ Không viết "53% dân số thế giới" – nguồn gốc dùng cách nói "mức phổ cập trong dân số", và tỷ lệ khác nhau nhiều giữa các nước.
>
> ⚠ Về ô "16 giờ": METR ghi rõ các số đo trên 16 giờ **không còn tin cậy** với bộ bài kiểm tra hiện tại, nên nói "**hơn 16 giờ**", không nói một con số cụ thể lớn hơn. Số "12 giờ" có khoảng tin cậy rộng (5–61 giờ). Trước ngày thuyết trình, xem lại trang https://metr.org/time-horizons/ – nếu METR đã công bố bộ bài kiểm tra mới, cập nhật số mới nhất. METR cũng lưu ý: "làm được 50% số lần" không có nghĩa là giao hẳn việc dài 16 giờ cho AI.

**Hình ảnh:** Biểu đồ METR (trục tung logarit) + 3 ô số liệu lớn.

**Câu chốt:** "Chỉ trong vài năm, AI đi từ trả lời câu hỏi đến tự thực hiện những công việc kéo dài nhiều giờ."

> **Đính chính (v2.1):** bản v2.0 ghi câu "rút còn 4 tháng từ 2023" của v1 là sai nguồn – nhận định đó chưa đúng. Theo METR Time Horizon 1.1 (01/2026), thời gian tăng gấp đôi kể từ 2023 là 131 ngày (≈ 4,3 tháng); kể từ 2024 là 89–105 ngày (≈ 3–3,5 tháng). Trên slide dùng cách nói "từ 2024, cứ khoảng 3–4 tháng" [N3].

---

#### Slide 2 – MỚI: Google và các nhà khoa học dùng AI giải bài toán khoa học thật (7 phút)

> Tiêu đề không ghi "các nhà khoa học Google" vì ví dụ ② và ③ do nhà khoa học của Imperial College và Đại học Yale chủ trì, Google cung cấp hệ thống AI.
> **Phân bổ thời gian:** nói kỹ ② (giả thuyết khoa học) và ⑤ (viết – chạy mã xử lý dữ liệu), vì gần với công việc của Trung tâm nhất; ①, ③, ④ mỗi thẻ ≤ 40 giây.

**Mục tiêu:** Cho thấy AI đã tham gia tạo ra kết quả khoa học được công bố trên tạp chí hàng đầu, với nhà khoa học giữ vai trò đặt bài toán và kiểm chứng.

**Bố cục slide:** dòng thời gian ngang, 5 thẻ; thẻ đầu tiên (mới nhất) phóng to.

| # | Thời điểm | Kết quả | Con số nổi bật | Vai trò nhà khoa học | Nguồn |
|---|---|---|---|---|---|
| ① | **08/10/2026** – *Science* | **AlphaProof Nexus** giải các bài toán mở trong toán học | **9/353** bài toán Erdős, trong đó **2 bài tồn tại 56 năm**; **44/492** giả thuyết OEIS | Mọi chứng minh được **máy kiểm chứng hình thức bằng Lean**; chuyên gia xác nhận phát biểu đúng bài toán gốc | [G1] |
| ② | 02/2025 → *Cell* 2025, *Nature* 05/2026 | **AI co-scientist** cùng Imperial College London (GS. José Penadés) | Trong khoảng **2 ngày**, giả thuyết xếp hạng 1 của AI **trùng với cơ chế** mà nhóm mất **nhiều năm** thí nghiệm mới tìm ra – khi kết quả **chưa công bố** | Nhóm đặt câu hỏi, đã có sẵn bằng chứng thí nghiệm để đối chiếu | [G2] |
| ③ | 10/2025 – bioRxiv | **C2S-Scale 27B** (Google DeepMind + Đại học Yale) | Sàng lọc ảo **hơn 4.000** thuốc → dự đoán **silmitasertib** chỉ khuếch đại trình diện kháng nguyên khi có interferon | **Kiểm chứng bằng thí nghiệm** trên mô hình tế bào người; chưa thử lâm sàng | [G3] |
| ④ | 05/2025 | **AlphaEvolve** – agent viết và tiến hóa mã | Nhân ma trận phức 4×4 bằng **48** phép nhân (phương pháp Strassen 1969: 49); thuật toán phân bổ máy chủ giúp Google thu hồi trung bình **0,7%** năng lực tính toán trước đó bị bỏ phí | Kết quả được kiểm tra tự động; thuật toán phân bổ máy chủ chạy thực tế hơn 1 năm | [G4] |
| ⑤ | 09/2025 → *Nature* 05/2026 | **Hệ thống AI viết phần mềm khoa học** (ERA) | Trong **đánh giá hồi cứu**, **14** mô hình dự báo số ca nhập viện COVID-19 tốt hơn mô hình tổng hợp mà CDC Mỹ dùng làm chuẩn; **40** phương pháp phân tích dữ liệu tế bào đơn vượt phương pháp tốt nhất do người phát triển trên một bảng xếp hạng công khai | Nhà khoa học định nghĩa bài toán và thước đo chất lượng | [G5] |

**Giải thích dễ hiểu cho người nghe (thuật ngữ → lời thường):**
- ① *Bài toán Erdős:* hàng trăm bài toán mở do nhà toán học Paul Erdős để lại. *OEIS:* "bách khoa toàn thư" các dãy số, kèm nhiều giả thuyết chưa ai chứng minh. *Lean:* phần mềm kiểm tra chứng minh từng bước, như một "trọng tài máy" – lập luận sai không qua được.
- ② Nhóm Imperial nghiên cứu vì sao gen kháng kháng sinh lan được **giữa các loài vi khuẩn khác nhau**. Họ phát hiện một loại đoạn gen di động (cf-PICI) tự tạo "vỏ" nhưng **"mượn đuôi" của nhiều loại virus** để xâm nhập nhiều loài. Trước khi công bố, họ đặt cùng câu hỏi cho AI – giả thuyết số 1 của AI trùng với kết quả của họ.
- ③ Nhiều khối u là khối u "lạnh": hệ miễn dịch không nhận ra. AI dự đoán thuốc silmitasertib (đã có sẵn) dùng cùng interferon liều thấp giúp tế bào ung thư **"lộ diện"** rõ hơn trước hệ miễn dịch. Thí nghiệm trên tế bào xác nhận; **chưa thử trên người**.
- ④ Phép nhân ma trận là phép tính nền tảng của phần mềm khoa học và AI, được lặp lại hàng tỷ lần – bớt 1 phép nhân (49 → 48) là phá kỷ lục **56 năm**.
- ⑤ AI tự viết **nhiều phiên bản chương trình, chạy thử, chấm điểm, giữ bản tốt nhất** rồi cải tiến tiếp. *Đánh giá hồi cứu:* chạy lại trên dữ liệu các tuần đã qua để so sánh công bằng với các mô hình khác.

**Cách nói đúng mức (ghi vào lời thoại):**
- ①: "AI giải được, và **máy kiểm chứng từng bước logic**. Tỷ lệ thành công khoảng 2,5% số bài đã thử – còn khiêm tốn, nhưng là bài toán mở thật."
- ②: "AI **không phát hiện điều mới** ở đây – nó **đi đến cùng kết luận** với nhóm thí nghiệm, trong vài ngày thay vì nhiều năm. Nhóm nghiên cứu cho biết nếu có giả thuyết này từ đầu, họ đã tiết kiệm được nhiều năm thí nghiệm."
- ③: "Đây là **giả thuyết đã được kiểm chứng trên tế bào**, chưa phải thuốc điều trị."
- ⑤: "Đây là đánh giá hồi cứu, không phải dự báo trực tiếp trong mùa dịch. Ví dụ này mình sẽ quay lại ở Slide 15 – nhà khoa học **giao bài toán, AI viết và chạy mã**."

**Câu chốt:** "Điểm chung của cả 5 ví dụ: **nhà khoa học đặt bài toán, AI đề xuất và thực hiện, kết quả được kiểm chứng độc lập** – bằng máy, bằng thí nghiệm hoặc bằng dữ liệu thật."

---

#### Slide 3 – AI trong các lĩnh vực khoa học: quốc tế và Việt Nam (5 phút)

| Lĩnh vực | Ví dụ tiêu biểu (đã xác minh) | Liên hệ với Trung tâm |
|---|---|---|
| Viễn thám | **Prithvi-EO-2.0** (NASA và IBM, **mã nguồn mở – ai cũng tải về dùng được**): mô hình AI học từ 4,2 triệu chuỗi ảnh vệ tinh Landsat – Sentinel-2, dùng để nhận dạng lũ, cháy rừng, cây trồng [N5]. **AlphaEarth Foundations** (Google DeepMind): mỗi ô 10 m × 10 m trên toàn Trái Đất được AI tóm tắt thành một "dấu vân tay số", có cho từng năm 2017–2024, giúp lập bản đồ với rất ít mẫu thực địa [N6] | Giám sát rừng, sử dụng đất, sinh thái nhiệt đới |
| Khí tượng | **AIFS** – mô hình dự báo thời tiết bằng AI của Trung tâm Dự báo Thời tiết Hạn vừa châu Âu (ECMWF), **chạy nghiệp vụ từ 25/02/2025**; ECMWF công bố dự báo đường đi bão nhiệt đới **chính xác hơn tới khoảng 20%** so với mô hình vật lý truyền thống [N7] | Môi trường nhiệt đới, khí hậu |
| Robotics | **Gemini Robotics** – robot học một thao tác mới sau khoảng **100 lần người làm mẫu** [N8] | Tự động hóa thí nghiệm |
| Sinh học | **AlphaFold** – dự đoán cấu trúc 3D của protein; tác giả nhận **Giải Nobel Hóa học 2024** [N4] | Y sinh nhiệt đới |
| Vật liệu | **GNoME** – AI đề xuất 2,2 triệu cấu trúc tinh thể mới, trong đó khoảng **380.000** được dự đoán là bền; **A-Lab** – phòng thí nghiệm robot tự tổng hợp được **41/58** hợp chất mới trong **17 ngày** [N9] | Vật liệu, ăn mòn, độ bền nhiệt đới |

**Việt Nam:** **Luật Trí tuệ nhân tạo số 134/2025/QH15**, ban hành 10/12/2025, **hiệu lực 01/3/2026** [N10].

**Câu chốt:** "AI đang trở thành một thành phần của hạ tầng nghiên cứu."

---

#### Slide 4 – Năng lực cốt lõi của AI: từ trả lời đến thực hiện (5 phút)

**Sáu năng lực cốt lõi:**
1. Đọc và tổng hợp quy mô lớn.
2. Suy luận và lập kế hoạch.
3. **Sử dụng công cụ – tìm kiếm, đọc/tạo tệp, viết và chạy mã.**
4. Đa phương thức – văn bản, bảng, hình ảnh, biểu đồ.
5. Đa ngôn ngữ – Việt, Nga, Anh (lợi thế của Trung tâm Việt – Nga).
6. Tái sử dụng – đóng gói quy trình thành Skill, nhiều trợ lý phối hợp.

**Ô nhỏ bên cạnh năng lực 3 (phần phụ về AI lập trình – nói ≤ 1 phút):**
> *Lập trình là lĩnh vực AI Agent phát triển sớm nhất:* 84% lập trình viên đang dùng hoặc dự định dùng AI [N11]. Điều này có ý nghĩa với nhà khoa học: **không cần giỏi lập trình vẫn có thể yêu cầu AI viết và chạy mã R/Python để xử lý dữ liệu** → xem Slide 15.

**Bảng so sánh chatbot – AI Agent:** giữ như v1.

**Câu chốt:** "Không phải công việc nào cũng cần Agent."

---

#### Slide 5 – Phương thức nghiên cứu đang thay đổi (4 phút)

Bốn chuyển dịch (giữ như v1), minh họa bằng chính các ví dụ của Slide 2:

| Trước đây | Hiện nay | Ví dụ |
|---|---|---|
| Tìm kiếm thủ công | Tổng hợp bằng chứng có hệ thống | AI co-scientist đọc tài liệu, đề xuất giả thuyết [G2] |
| Thao tác riêng lẻ | Quy trình liên tục | ERA: viết mã → chạy → chấm điểm → cải tiến [G5] |
| Prompt dùng một lần | Skill dùng lại | Thư viện Skill khoa học mở (Phần IV) |
| Một chatbot | Nhiều trợ lý phối hợp | Co-scientist: các agent tạo, phản biện, xếp hạng giả thuyết [G2] |

**Thông điệp Phần I** (cuối slide).

---

### PHẦN II. LỰA CHỌN VÀ SỬ DỤNG CÔNG CỤ AI PHÙ HỢP (30 phút – 5 slide)

Giữ cấu trúc v1 (Slide 6–10). Bổ sung:

- **Slide 6 – Thang 5 bậc:** gắn ví dụ của tình huống A cho mỗi bậc:
  1. Hỏi – đáp: "Cấp ăn mòn C4 theo ISO 9223 nghĩa là gì?"
  2. Phân tích một tài liệu: tóm tắt một bài báo về ăn mòn thép ven biển.
  3. Tổng hợp nhiều nguồn: ma trận bằng chứng 15 bài (Slide 12).
  4. Xử lý nhiều tệp: 2 tệp CSV dữ liệu (Slide 15).
  5. Chuỗi nhiệm vụ: dữ liệu → mô hình → biểu đồ → bản thảo bài báo.
- **Slide 7 – Bảng công cụ:** cột "Chính sách dữ liệu" **phải điền từ điều khoản chính thức** của từng công cụ ngay trước buổi thuyết trình (chính sách thay đổi thường xuyên) – xem Mục 7, dòng N14.
- **Slide 8 – Giao việc 5 bước:** ví dụ minh họa dùng chính Câu lệnh 4.3 trong `cau-lenh-demo.md` (đã có đủ: nhiệm vụ – dữ liệu – đầu ra – yêu cầu tái lập – kiểm tra).
- **Slide 9 – Không gian dự án:** ảnh chụp Project "Demo – Ăn mòn khí quyển nhiệt đới" (đã dựng theo Mục 0 của `cau-lenh-demo.md`).
- **Slide 10 – Skill, Subagent, Multi-agent:** dẫn lại AI co-scientist [G2] như ví dụ thật về hệ nhiều agent. **Thông điệp Phần II.**

---

### PHẦN III. AI AGENT TRONG VÒNG ĐỜI NHIỆM VỤ KHOA HỌC (40 phút – 7 slide)

**Khung trình bày cho mỗi slide 12–16:**

| Khối | Nội dung trên slide |
|---|---|
| 🌍 Ví dụ thực tế | 1 ví dụ quốc tế đã công bố (≤ 2 dòng) |
| ⌨ Câu lệnh | Câu lệnh rút gọn (bản đầy đủ trong `cau-lenh-demo.md`) |
| 📂 Dữ liệu | Tệp đầu vào |
| 📊 Kết quả | Ảnh chụp kết quả thật đã chạy |
| 🗣 Gợi ý nói | Ghi trong phần ghi chú của slide |
| ✅ Xác nhận | Việc nhà khoa học phải làm |

---

#### Slide 11 – Một nhiệm vụ khoa học đi qua AI Agent như thế nào? (3 phút)

**Tình huống A (giới thiệu một lần, dùng xuyên suốt):**
> *"Đánh giá ăn mòn khí quyển của thép CT3, kẽm, đồng, nhôm tại 3 trạm thử nghiệm (ven biển, đô thị, nội địa); xây dựng mô hình dự báo C = A·tⁿ và phân cấp ăn mòn theo ISO 9223."*
> Quy mô: 3 trạm × 4 kim loại × 7 mốc thu mẫu (1–36 tháng) × 3 mẫu lặp = **252 mẫu**; số liệu khí tượng 36 tháng.
>
> *Giải nghĩa mô hình C = A·tⁿ (nói một lần ở đây):* C là lượng kim loại mất đi sau t năm; **A** là lượng mất trong **năm đầu tiên** (A càng lớn, môi trường càng ăn mòn mạnh); **n** cho biết tốc độ có chậm lại theo thời gian không – n < 1 nghĩa là lớp gỉ hình thành dần và che chắn một phần cho kim loại bên dưới.

**Hình chính:** Sơ đồ vòng đời: Tài liệu (S12) → Khoảng trống (S12) → Thuyết minh (S13) → Tiến độ – kinh phí (S14) → Dữ liệu – kết quả (S15) → Bài báo – báo cáo (S16), mỗi bước có biểu tượng ✅ điểm xác nhận.

**Gợi ý nói:** "Trong 30 phút tới, chúng ta đi hết vòng đời của một nhiệm vụ giả định, với dữ liệu giả lập nhưng câu lệnh và cách làm là thật – anh chị có thể về chạy lại ngay."

---

#### Slide 12 – Từ tài liệu đến khoảng trống và câu hỏi nghiên cứu (6 phút)

**🌍 Ví dụ thực tế:** *AI co-scientist* (Google): hệ nhiều agent tạo – phản biện – xếp hạng giả thuyết. Với câu hỏi của nhóm Imperial College, giả thuyết số 1 của AI trùng với cơ chế nhóm đã chứng minh bằng thí nghiệm nhưng chưa công bố [G2].

**⌨ Câu lệnh (rút gọn – bản đầy đủ: Câu lệnh 1.1, 1.2, 1.3):**
```
Từ các bài báo trong Project, lập ma trận bằng chứng: Tác giả–năm | Địa điểm & khí hậu |
Kim loại | Thời gian phơi mẫu | Biến môi trường | Mô hình | Giá trị n | Kết luận | Hạn chế.
Sau đó chỉ ra các điểm chưa thống nhất và 3 khoảng trống cho điều kiện Việt Nam,
mỗi khoảng trống dẫn chứng ít nhất 2 bài.
```

**📂 Dữ liệu:** 10–15 bài báo truy cập mở về ăn mòn khí quyển (tự tải; gợi ý từ khóa: *atmospheric corrosion, tropical, marine, chloride deposition, ISO 9223, dose–response*). Tài liệu nền: ISO 9223:2012, ISO 9224:2012.

**📊 Kết quả cần chụp:** bản đồ 5–7 hướng nghiên cứu; ma trận bằng chứng; 3 khoảng trống có điểm phản biện.

**🗣 Gợi ý nói:**
- "Câu lệnh 1.3 cho AI đóng vai 3 phản biện độc lập – đây là phiên bản thu nhỏ của cách AI co-scientist hoạt động."
- "**Mỗi DOI tôi đều bấm thử.** AI có thể nhầm nguồn; kiểm tra nguồn là việc của nhà khoa học."

**✅ Xác nhận:** nguồn có thật và đúng nội dung; khoảng trống có giá trị khoa học.

---

#### Slide 13 – Từ câu hỏi nghiên cứu đến thuyết minh (8 phút) – **DEMO 1**

**🌍 Ví dụ thực tế:** đầu ra của AI co-scientist không chỉ là giả thuyết mà là **đề xuất nghiên cứu** có lập luận và kế hoạch kiểm chứng [G2].

**⌨ Câu lệnh trình diễn trực tiếp (Câu lệnh 2.2):**
```
Lập bảng đối chiếu: Mục tiêu cụ thể → Nội dung → Phương pháp → Sản phẩm → Chỉ tiêu.
Đánh dấu ⚠ mọi chỗ: mục tiêu không có nội dung tương ứng; sản phẩm không có chỉ tiêu
đo được; phương pháp không đủ để đạt mục tiêu; số mẫu không khớp
(3 trạm × 4 kim loại × 7 mốc × 3 lặp = ? mẫu).
```

**📂 Dữ liệu:** bản nháp thuyết minh (tạo trước bằng Câu lệnh 2.1) + Mẫu 01A/07/08 trống.

**📊 Kết quả mong đợi:** bảng 5 cột; AI tính đúng **252 mẫu**; chỉ ra ít nhất 1–2 điểm ⚠ (ví dụ: mục tiêu "bản đồ phân vùng ăn mòn" nhưng chỉ có 3 trạm → không đủ để nội suy không gian).

**🗣 Gợi ý nói:** "Hội đồng thường bắt lỗi đúng ở những chỗ này. Để AI rà trước giúp ta sửa từ sớm – nhưng **chọn mục tiêu nào là quyết định của chủ nhiệm**."

**✅ Xác nhận:** tính mới, tính khả thi, chỉ tiêu.

---

#### Slide 14 – Tổ chức công việc, tiến độ và kinh phí (5 phút)

**⌨ Câu lệnh (Câu lệnh 3.1):**
```
Đọc ke_hoach_cong_viec.csv. Vẽ sơ đồ Gantt, tính tổng kinh phí và tỷ lệ theo đơn vị,
kiểm tra logic trình tự và độ phủ dữ liệu; liệt kê bất hợp lý và đề xuất điều chỉnh.
```

**📂 Dữ liệu:** `du-lieu-demo/ke_hoach_cong_viec.csv` (7 nội dung, 01/2027 – 04/2030).

**📊 Kết quả đã chạy thử:** `ket-qua-mau/so_do_gantt.png`; tổng kinh phí **1.350 triệu đồng**. AI cần phát hiện 3 điểm cài sẵn:

| # | Bất hợp lý | Đề xuất |
|---|---|---|
| 1 | ND4 (thu mẫu) bắt đầu 04/2027, khi ND2 (lắp giá phơi mẫu) đến 05/2027 mới xong | Dời ND4 hoặc rút ngắn ND2 |
| 2 | ND3 (quan trắc khí tượng) kết thúc 03/2030, sớm hơn ND4 (04/2030) → mốc thu mẫu cuối thiếu số liệu môi trường | Kéo dài ND3 thêm 1 tháng |
| 3 | ND7 (công bố) bắt đầu 06/2029 khi ND5 (mô hình) chưa xong | Chấp nhận nếu là bài báo giữa kỳ – **nhà khoa học quyết định** |

**🗣 Gợi ý nói:** "Ba lỗi này tôi cố ý cài vào – AI tìm ra trong vài giây. Trong hồ sơ thật, lỗi kiểu này thường chỉ bị phát hiện khi hội đồng đọc."

**✅ Xác nhận:** số liệu tài chính do cán bộ tài chính xác nhận.

---

#### Slide 15 – Từ dữ liệu thô đến kết quả phân tích: nhà khoa học dùng AI viết và chạy mã (8 phút) – **DEMO 2**

**🌍 Ví dụ thực tế (mở đầu slide, 1 phút):** hệ thống **ERA** của Google (*Nature*, 05/2026): nhà khoa học nêu bài toán và thước đo; AI **tự viết mã, chạy, chấm điểm, cải tiến** – tạo ra 14 mô hình dự báo COVID-19 tốt hơn mô hình tổng hợp của CDC [G5].
→ "Ở quy mô của chúng ta: **không cần biết lập trình**, nhà khoa học vẫn yêu cầu AI viết và chạy mã Python để xử lý dữ liệu thí nghiệm."

**📂 Dữ liệu:** `an_mon_tho.csv` (253 dòng), `khi_tuong_tram.csv` (108 dòng).

**⌨ Câu lệnh trình diễn trực tiếp (Câu lệnh 4.2 → 4.3 → 4.4):**
```
4.2  Rà soát an_mon_tho.csv: dòng trùng, tên trạm không thống nhất, ô trống, số sai
     định dạng, ngày sai định dạng, giá trị phi vật lý, ngoại lệ giữa các mẫu lặp,
     ghi chú thực nghiệm. Lưu ý: mỗi nhóm chỉ có 3 mẫu lặp – chọn phương pháp phát hiện
     ngoại lệ phù hợp và giải thích. KHÔNG xóa dữ liệu gốc.
4.3  Tính tổn thất (g/m², µm); hồi quy C = A·t^n cho từng trạm × kim loại;
     xếp cấp ISO 9223; dự báo 10 năm; lưu mã để tái lập.
4.4  Vẽ đồ thị log–log 4 kim loại × 3 trạm và biểu đồ cột thép theo trạm.
```

**📊 Kết quả đã chạy thử:**

*a) Báo cáo chất lượng dữ liệu – phát hiện đủ 14/14 lỗi cài sẵn:* 1 dòng trùng · 2 tên trạm không thống nhất · 3 ô trống · 2 số sai định dạng (`107,1491`, `114.2493 g`) · 2 ngày sai định dạng · 1 giá trị phi vật lý (khối lượng sau > trước) · 1 ngoại lệ (lệch +69% so với 2 mẫu lặp) · 2 ghi chú thực nghiệm. → 247/253 dòng dùng cho mô hình.

*b) Mô hình C = A·tⁿ cho thép CT3 (R² > 0,99):*

| Trạm | A (g/m², năm đầu) | n | Cấp ISO 9223 | Dự báo 10 năm |
|---|---|---|---|---|
| Ven biển | 567 | 0,74 | C4 | ≈ 397 µm |
| Đô thị | 305 | 0,71 | C3 | ≈ 201 µm |
| Nội địa | 160 | 0,72 | C2 | ≈ 108 µm |

*c) Biểu đồ:* `ket-qua-mau/bieu_do_dong_hoc_an_mon.png`, `ket-qua-mau/bieu_do_thep_theo_tram.png`.

**🗣 Gợi ý nói – bài học thật từ lúc chạy thử (điểm nhấn của slide):**
> "Lần chạy đầu, mã dùng phương pháp z-score/MAD – một cách thống kê đo xem một giá trị lệch bao xa so với số đông, vốn cần nhiều số liệu mới đáng tin – để tìm ngoại lệ. Kết quả: **đánh dấu nhầm 20 giá trị hoàn toàn bình thường**, trong khi **bỏ sót đúng lỗi gõ nhầm** cần tìm. Lý do: mỗi nhóm chỉ có **3 mẫu lặp** – quá ít cho phương pháp đó. Tôi yêu cầu đổi sang quy tắc 'lệch > 30% so với hai mẫu lặp còn lại' thì kết quả mới đúng.
> **AI viết mã rất nhanh – nhưng chọn phương pháp phù hợp với thiết kế thí nghiệm là việc của người làm chuyên môn.**"

**Phân biệt kết quả – diễn giải (Câu lệnh 4.5):** AI ghép số liệu môi trường và chỉ ra trạm ven biển có Cl⁻ ≈ 181 mg/m²·ngày và TOW ≈ 5.730 h/năm cao nhất. AI phải tự nêu được: *"chỉ có 3 trạm – không đủ để kết luận thống kê về tương quan"*. Diễn giải "n < 1 phù hợp với cơ chế lớp gỉ bảo vệ" là **đề xuất để nhà khoa học xác nhận**.

**✅ Xác nhận:** phương pháp xử lý ngoại lệ; diễn giải cơ chế; độ tin cậy của dự báo 10 năm khi chỉ có số liệu 3 năm.

**📌 Ô "Kết quả với dữ liệu thật" (30–60 giây, cuối slide)** – dùng kết quả của thư mục `nghien-cuu-an-mon/` (Báo cáo nghiên cứu, 10/2026):
> Cùng cách làm này, áp dụng cho **387 số đo thực địa đã công bố** về ăn mòn thép cacbon (ISOCORRAG, MICAT, **12 trạm Việt Nam**, 18 trạm Nga):
> - AI phát hiện **lỗi đơn vị trong bộ dữ liệu công bố**: cột ghi "g/m²" nhưng thực chất là µm/năm.
> - Mô hình học từ dữ liệu quốc tế **dự đoán thấp hơn thực đo ở Việt Nam khoảng 31%** → cần hệ số hiệu chỉnh riêng cho khí hậu nhiệt đới. Đây là lý do số liệu trạm của Trung tâm có giá trị lớn.
>
> Dữ liệu thật dùng cho ô này là dữ liệu đã công bố – thuộc nhóm xanh.

---

#### Slide 16 – Từ kết quả đến bài báo và báo cáo tổng hợp (6 phút)

**🌍 Ví dụ thực tế:** cả 5 công trình ở Slide 2 đều do **nhà khoa học đứng tên và chịu trách nhiệm**. Chính sách của *Nature*: công cụ AI **không đủ điều kiện là tác giả**, việc sử dụng phải được nêu trong phần Phương pháp [N15].

**⌨ Câu lệnh (Câu lệnh 5.1, 5.2, 5.3):**
```
5.1  Lập dàn ý IMRaD cho tạp chí [...]: 3 phương án tiêu đề, ý chính từng phần,
     danh mục hình – bảng, 3 điểm mới; đối chiếu hướng dẫn tác giả của tạp chí.
5.2  Đóng vai phản biện khó tính: 5 nhược điểm lớn nhất và cách trả lời.
5.3  Bảng: Mục tiêu | Sản phẩm cam kết | Sản phẩm đã có | Bằng chứng | Mức hoàn thành.
```

**📂 Dữ liệu:** kết quả Slide 15 + thuyết minh đã duyệt (Slide 13).

**📊 Kết quả mong đợi:** dàn ý bài báo; danh sách 5 câu hỏi phản biện (AI cần nêu được: chỉ 3 trạm, dự báo 10 năm từ số liệu 3 năm, cách xử lý ngoại lệ); bảng đối chiếu Mẫu 21/22.

**🗣 Gợi ý nói:** "Để AI phản biện mình trước khi gửi bài – rẻ hơn rất nhiều so với một lần bị từ chối."

**✅ Xác nhận:** nội dung khoa học, trích dẫn, quyền tác giả, khai báo việc sử dụng AI.

---

#### Slide 17 – Năm quyết định thuộc về nhà khoa học (4 phút)

Giữ năm quyết định của v1, gắn mỗi quyết định với một khoảnh khắc trong demo:

| Quyết định | Khoảnh khắc trong demo |
|---|---|
| 1. Nguồn nào được chấp nhận | Bấm thử từng DOI (S12) |
| 2. Khoảng trống nào có giá trị | Chọn 1 trong 3 khoảng trống (S12–13) |
| 3. Phương pháp nào phù hợp | **Đổi phương pháp ngoại lệ khi chỉ có 3 mẫu lặp (S15)** |
| 4. Kết quả được diễn giải thế nào | Tách "kết quả tính toán" và "diễn giải đề xuất" (S15) |
| 5. Dữ liệu nào được đưa lên AI | Chỉ dữ liệu giả lập – nhóm xanh (Mục 6) |

Lồng ghép: Luật Trí tuệ nhân tạo 134/2025/QH15 [N10]; Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 [N12]. **Thông điệp Phần III.**

---

### PHẦN IV. SKILL, KHOA HỌC MỞ VÀ TỰ ĐỘNG HÓA (15 phút – 4 slide)

Giữ nguyên nội dung Slide 18–21 của v1. Bổ sung:
- **Slide 18:** Ví dụ Skill cụ thể từ tình huống A: "SK-08 Kiểm tra chất lượng dữ liệu cân mẫu ăn mòn" – đóng gói câu lệnh 4.2 *đã sửa bài học về 3 mẫu lặp* → lần sau ai chạy cũng đúng ngay.
- **Slide 20:** Ảnh chụp bản tin QT-01 chạy thật với từ khóa ăn mòn khí quyển (câu lệnh mục 6 trong `cau-lenh-demo.md`).
- **Slide 21:** giữ lộ trình và lời kêu gọi hành động.

---

### TRAO ĐỔI VÀ PHỤ LỤC

- **Slide 22 – Trao đổi (10 phút):** kết quả phiếu khảo sát; câu hỏi; đề xuất quy trình thí điểm.
- **Slide 23 – Phụ lục A: AI lập trình** *(chuyển từ Slide 2 cũ, không trình bày)*: GitHub Octoverse 2025 – hơn 180 triệu lập trình viên, hơn 36 triệu người mới, 630 triệu kho mã, gần 1 tỷ commit, 4,3 triệu dự án AI [N13]; Stack Overflow 2025 – 84% dùng/dự định dùng AI, 51% lập trình viên chuyên nghiệp dùng hằng ngày [N11]; SWE-bench Verified tăng từ 60% lên gần 100% trong một năm [N1].
- **Slide 24 – Phụ lục B:** nguồn tham khảo (Mục 11).
- **Slide 25 – Phụ lục C:** dự án và bộ Skill khoa học mở.

---

## 4. TÌNH HUỐNG XUYÊN SUỐT VÀ KỊCH BẢN DEMO

### 4.1. Tình huống đã chốt: Phương án A

| Thành phần | Nội dung |
|---|---|
| Câu hỏi nghiên cứu | Tốc độ và động học ăn mòn khí quyển của 4 kim loại ở 3 kiểu môi trường nhiệt đới; yếu tố môi trường chi phối |
| Thiết kế | 3 trạm × 4 kim loại × 7 mốc (1, 3, 6, 12, 18, 24, 36 tháng) × 3 mẫu lặp = 252 mẫu; mẫu 100×150 mm (300 cm² hai mặt) |
| Dữ liệu | Khối lượng trước/sau tẩy gỉ; khí tượng – môi trường theo tháng |
| Mô hình | C = A·tⁿ (dạng hàm lũy thừa, như ISO 9224); phân cấp theo ISO 9223:2012 |
| Sản phẩm | Ma trận bằng chứng, thuyết minh, Gantt, mô hình, biểu đồ, dàn ý bài báo |

**Cách dữ liệu giả lập được tạo (để trả lời nếu bị hỏi):** chọn trước giá trị A, n "đúng" cho từng trạm – kim loại (thép: 560 / 310 / 160 g/m²; n = 0,72), thêm nhiễu ngẫu nhiên ~6%, rồi cài 14 lỗi có chủ đích. Mô hình AI khôi phục lại A = 567 / 305 / 160 – **khớp với giá trị gốc**, chứng tỏ quy trình phân tích đúng.

### 4.2. Demo 1 – Từ khoảng trống đến thuyết minh (Slide 13)

| Bước | Thao tác | Câu lệnh | Đầu ra | Cách trình bày |
|---|---|---|---|---|
| 1 | Dựng Project, tải 10–15 bài báo + mẫu trống | Mục 0 | Không gian dự án | Ảnh chụp |
| 2 | Ma trận bằng chứng + 3 khoảng trống | 1.2 | Bảng | Ảnh chụp |
| 3 | Phản biện, xếp hạng khoảng trống | 1.3 | Bảng điểm | Ảnh chụp |
| 4 | Soạn các mục thuyết minh | 2.1 | Bản nháp | Ảnh chụp |
| 5 | **Kiểm tra logic** | 2.2 | Bảng đối chiếu | **Trực tiếp (~2 phút)** |
| 6 | Điền Mẫu 01A | 2.3 | Tệp .docx | Mở tệp đã tạo sẵn |

### 4.3. Demo 2 – Từ dữ liệu thô đến kết quả (Slide 15)

| Bước | Thao tác | Câu lệnh | Đầu ra (đối chiếu `ket-qua-mau/`) | Cách trình bày |
|---|---|---|---|---|
| 1 | Tải 2 tệp CSV | – | – | Trực tiếp |
| 2 | Từ điển dữ liệu | 4.1 | Bảng mô tả biến | Ảnh chụp |
| 3 | **Rà soát chất lượng** | 4.2 | 14 vấn đề | **Trực tiếp** |
| 4 | **Mô hình C = A·tⁿ** | 4.3 | `mo_hinh_A_n.csv` | **Trực tiếp** |
| 5 | **Biểu đồ** | 4.4 | 2 tệp PNG | **Trực tiếp** |
| 6 | Môi trường – diễn giải | 4.5 | `moi_truong_va_ton_that_nam_dau.csv` | Ảnh chụp |

Tổng thời gian trực tiếp: ~3 phút. Kết quả chạy lại trên Claude có thể lệch nhẹ (cách làm sạch khác chút); **sai khác lớn là tín hiệu cần xem lại**.

### 4.4. Hướng dẫn tự chạy trên Claude (cho người trình bày)
1. claude.ai → Settings → Capabilities → bật **Code execution and file creation** (tên mục có thể khác tùy phiên bản) (và **Web search** cho Slide 12).
2. Tạo Project, dán *Project instructions* trong `cau-lenh-demo.md` (Mục 0).
3. Tải tệp từ `du-lieu-demo/`.
4. Lần lượt dán câu lệnh theo thứ tự; so kết quả với `ket-qua-mau/`.
5. Chạy thử trọn bộ **ít nhất 2 lần**, chụp màn hình từng bước, quay video dự phòng.

### 4.5. Yêu cầu chung
- Chỉ dùng dữ liệu xanh; trên slide ghi "dữ liệu giả lập".
- Lưu sẵn mọi kết quả trung gian.
- Tệp câu lệnh mở sẵn để sao chép nhanh.

---

## 5. HỆ THỐNG QUY TRÌNH TỰ ĐỘNG TẠI TRUNG TÂM (ĐỀ XUẤT)

Giữ nguyên Mục 5 của v1 (cấu trúc chung, thư viện Skill SK-01 → SK-14, đặc tả QT-00 → QT-06, liên thông, hạ tầng, tiêu chí đánh giá). Bổ sung ví dụ cụ thể theo tình huống A:

| Quy trình | Ví dụ theo tình huống A |
|---|---|
| QT-01 | Bản tin tuần "atmospheric corrosion AND (tropical OR marine OR chloride)" |
| QT-02 | Ma trận bằng chứng ăn mòn khí quyển (Câu lệnh 1.2) |
| QT-04 | Mỗi lần có tệp cân mẫu mới → tự chạy SK-08 (14 kiểm tra) → SK-09 (mô hình, biểu đồ) → gửi nghiên cứu viên duyệt |
| QT-05 | Hằng tháng đối chiếu tiến độ thực tế với `ke_hoach_cong_viec.csv` |

---

## 6. QUY TẮC PHÂN LOẠI DỮ LIỆU XANH / VÀNG / ĐỎ

Giữ nguyên Mục 6 của v1. Cập nhật căn cứ pháp lý (đã xác minh):
- Luật Trí tuệ nhân tạo số **134/2025/QH15** – ban hành 10/12/2025, hiệu lực 01/3/2026 [N10].
- Luật Bảo vệ dữ liệu cá nhân số **91/2025/QH15** – ban hành 26/6/2025, hiệu lực 01/01/2026 [N12].
- Luật Bảo vệ bí mật nhà nước số 29/2018/QH14; quy định nội bộ của Trung tâm và Bộ Quốc phòng.

> Nội dung chính thức do bộ phận phụ trách bảo mật của Trung tâm xác nhận trước khi trình bày.

---

## 7. BẢNG CĂN CỨ – SỐ LIỆU ĐÃ XÁC MINH

Trạng thái: ✅ đã đối chiếu nguồn gốc · ◐ đã đối chiếu một phần / qua nguồn thứ cấp đáng tin · ☐ cần làm trước buổi thuyết trình.

### 7.1. Các ví dụ Google (Slide 2)

| Mã | Nội dung trên slide | Nguồn gốc | Trạng thái |
|---|---|---|---|
| G1 | AlphaProof Nexus: 9/353 bài toán Erdős (2 bài mở 56 năm); 44/492 giả thuyết OEIS; kiểm chứng bằng Lean | Tsoukalas et al., "Advancing mathematics research with AI-driven formal proof search", *Science* 394(6820):234–239, **08/10/2026**, DOI 10.1126/science.aej2213; bản tiền ấn phẩm arXiv:2605.22763 | ✅ |
| G2 | AI co-scientist: giả thuyết số 1 trùng cơ chế cf-PICI "mượn đuôi phage" của nhóm Imperial khi chưa công bố; khoảng 2 ngày | (a) Penadés et al., "AI mirrors experimental science to uncover a mechanism of gene transfer crucial to bacterial evolution", *Cell* 188(23):6654–6665 (2025), DOI 10.1016/j.cell.2025.08.018; (b) He et al., "Chimeric infective particles expand species boundaries in phage-inducible chromosomal island mobilization", *Cell* (2025), DOI 10.1016/j.cell.2025.08.019; (c) Gottweis et al., "Accelerating scientific discovery with Co-Scientist", *Nature* (19/05/2026), DOI 10.1038/s41586-026-10644-y; bản arXiv:2502.18864 (02/2025); (d) tin Imperial College 02/2025 | ✅ (con số "2 ngày" theo tin của *Nature*, không có trong bài *Cell*) |
| G3 | C2S-Scale 27B: sàng lọc >4.000 thuốc; silmitasertib khuếch đại trình diện kháng nguyên **chỉ khi có interferon**; kiểm chứng trên tế bào | Blog Google (10/2025); bioRxiv DOI 10.1101/2025.04.14.648850 (v2, v3) | ✅ — **không dùng** con số "% tăng" vì chưa đối chiếu được |
| G4 | AlphaEvolve: 48 phép nhân cho ma trận phức 4×4; 0,7% tài nguyên tính toán; (tùy chọn) số hôn 11 chiều 592 → 593 | Novikov et al., arXiv:2506.13131 (2025); blog Google DeepMind 05/2025 | ✅ |
| G5 | ERA: 14 mô hình COVID-19 tốt hơn CovidHub Ensemble của CDC; 40 phương pháp tế bào đơn vượt phương pháp tốt nhất của người | Aygün et al., "An AI system to help scientists write expert-level empirical software", *Nature* 654:909–916 (công bố trực tuyến 19/05/2026), DOI 10.1038/s41586-026-10658-6; bản arXiv:2509.06503 | ✅ |

### 7.2. Số liệu khác

| Mã | Số liệu | Slide | Nguồn | Trạng thái |
|---|---|---|---|---|
| N1 | Nguyên văn: "gần **53% mức phổ cập trong dân số** trong vòng **3 năm kể từ khi ra mắt đại chúng**, nhanh hơn máy tính cá nhân hay Internet"; tỷ lệ khác nhau nhiều giữa các nước. SWE-bench Verified 60% → gần 100% trong 1 năm | 1, 23 | Stanford HAI, *AI Index Report 2026*, Chương 4 – Kinh tế (13/04/2026) | ✅ (53%) / ◐ (SWE-bench) |
| N1b | 88% tổ chức dùng AI cho ít nhất một chức năng | (tùy chọn) | Báo chí tóm tắt AI Index 2026 | ◐ – kiểm tra bản gốc trước khi dùng |
| N2 | Gemini Deep Think đạt chuẩn vàng IMO 2025, 5/6 bài, 35/42 điểm; OpenAI công bố kết quả tương tự | 1 | Google DeepMind (07/2025); xác nhận của Ban tổ chức IMO | ◐ |
| N3 | Độ dài tác vụ (thành công 50%): GPT-2 (2019) ≈ 2 giây → Claude 3.7 Sonnet (02/2025) ≈ 50–59 phút → mô hình công khai mạnh nhất (02–03/2026) ≈ 12 giờ [5–61 giờ] → Claude Mythos Preview (05/2026) ≥ 16 giờ (giới hạn đo). Thời gian tăng gấp đôi: ~7 tháng (2019–2025, dài hạn); **105 ngày ≈ 3,5 tháng** cho mô hình ra mắt từ 01/2024 (R² = 0,98) | 1 | METR: "Measuring AI Ability to Complete Long Tasks" (19/03/2025, arXiv:2503.14499); "Time Horizon 1.1" (29/01/2026); "Frontier Risk Report (Feb–Mar 2026)" (19/05/2026); trang metr.org/time-horizons (cập nhật 08/05/2026) | ✅ – xem lại trang METR ngay trước buổi thuyết trình |
| N4 | AlphaFold – Giải Nobel Hóa học 2024 (Hassabis, Jumper; cùng David Baker) | 3 | nobelprize.org | ✅ (nguồn kinh điển) |
| N5 | Prithvi-EO-2.0: 300M/600M tham số, 4,2 triệu mẫu HLS, mã nguồn mở | 3 | arXiv:2412.02732 | ✅ |
| N6 | AlphaEarth Foundations: embedding 10 m, hằng năm 2017–2024 | 3 | arXiv:2507.22291; Google Earth Engine catalog | ✅ |
| N7 | ECMWF AIFS vận hành từ 25/02/2025; cải thiện tới ~20% với đường đi bão | 3 | ECMWF, "ECMWF's AI forecasts become operational" | ✅ |
| N8 | Gemini Robotics: tác vụ ngắn mới từ ~100 lần trình diễn | 3 | arXiv:2503.20020 (03/2025) | ✅ |
| N9 | GNoME 2,2 triệu cấu trúc, ~380.000 dự đoán bền; A-Lab 41/58 hợp chất trong 17 ngày | 3 | *Nature* (11/2023); Berkeley Lab News (29/11/2023) | ✅ |
| N10 | Luật Trí tuệ nhân tạo 134/2025/QH15 | 3, 17 | Công báo Chính phủ | ✅ |
| N11 | Stack Overflow 2025: 84% dùng/dự định dùng AI; 51% chuyên nghiệp dùng hằng ngày | 4, 23 | survey.stackoverflow.co/2025/ai | ✅ |
| N12 | Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15, hiệu lực 01/01/2026 | 17 | Cổng TTĐT Chính phủ | ✅ |
| N13 | GitHub Octoverse 2025 (09/2024 – 08/2025) | 23 | github.blog – Octoverse 2025 | ✅ |
| N14 | Chính sách dữ liệu của 5 công cụ AI | 7 | Điều khoản chính thức từng công cụ | ☐ kiểm tra trong tuần thuyết trình |
| N15 | *Nature*: AI không đủ điều kiện tác giả, phải khai báo việc sử dụng | 16 | Chính sách biên tập Nature Portfolio về AI | ◐ – trích nguyên văn trước khi dùng |
| N16 | Ngưỡng ISO 9223:2012 Bảng 2 (g/m²·năm) | 15 | ISO 9223:2012 | ✅ thép, kẽm (6 cấp); đồng, nhôm (C1–C3) · ☐ đồng, nhôm từ C4 |
| N17 | URL, số lượng Skill của AI4S, AIPOCH, K-Dense, CES Global | 18, 25 | Trang chính thức / GitHub | ☐ |
| N18 | Bài báo arXiv 2609.00065 | 24 | Kiểm tra lại mã số | ☐ |
| N19 | Nguyên tắc FAIR; Khuyến nghị Khoa học mở UNESCO | 18 | *Scientific Data* (2016); UNESCO (2021) | ✅ (nguồn kinh điển) |

> **Lưu ý về cách xác minh:** các số liệu ✅ được đối chiếu với trang của nguồn gốc (tạp chí, arXiv, trang tổ chức) qua công cụ tìm kiếm. Trước khi in slide, người trình bày nên mở trực tiếp các DOI ở Mục 7.1 một lần nữa – đặc biệt G1 (mới công bố 08/10/2026).

---

## 8. KẾ HOẠCH THỰC HIỆN THEO GIAI ĐOẠN

| Giai đoạn | Công việc | Sản phẩm | Trạng thái |
|---|---|---|---|
| 1. Nghiên cứu | Xác minh số liệu (Mục 7) | Bảng căn cứ | ✅ phần lớn; còn N14, N16 (đồng/nhôm), N17, N18 |
| 2. Tình huống & dữ liệu | Chốt tình huống A; dữ liệu demo | `du-lieu-demo/` | ✅ |
| 2a. Chạy thử phân tích | Chạy mã, lấy kết quả mẫu | `ket-qua-mau/` | ✅ |
| 2b. Skill & quy trình | Khảo sát Skill mở; dựng thử QT-01 | Bản tin mẫu | ☐ |
| 3. Xây dựng slide | 25 slide theo Mục 3 | Slide v1 | ☐ |
| 4. Chuẩn bị demo | Chạy trên Claude 2 lần (Mục 4.4); chụp màn hình; quay video | Ảnh, video | ☐ |
| 5. Rà soát | Lãnh đạo/chuyên môn; bộ phận bảo mật duyệt Mục 6 | Slide v2 | ☐ |
| 6. Lời thoại & tập dượt | Lời thoại theo "Gợi ý nói"; bấm giờ 2 lần | Bản cuối | ☐ |
| 7. Tài liệu đi kèm | Phiếu khảo sát; tài liệu phát tay | Bản in | ☐ |

### Danh sách kiểm tra trước ngày thuyết trình
- ☐ Mở lại các DOI Mục 7.1; điền N14 (chính sách dữ liệu)
- ☐ Quy tắc xanh / vàng / đỏ đã được xác nhận
- ☐ Demo chạy trên Claude thành công ≥ 2 lần; kết quả khớp `ket-qua-mau/`
- ☐ Video demo dự phòng
- ☐ Kiểm tra mạng, máy chiếu, tài khoản AI tại phòng thuyết trình
- ☐ Tập dượt bấm giờ: kế hoạch có 108′ trình bày + 12′ thảo luận; khi tập, nói trong 100′ để còn 10′ dự phòng cho demo
- ☐ Phiếu khảo sát đã gửi và tổng hợp; tài liệu phát tay đã in

---

## 9. TÀI LIỆU ĐI KÈM

### 9.1. Phiếu khảo sát trước buổi học
Giữ như v1 (6 câu hỏi).

### 9.2. Tài liệu phát tay (1 trang, 2 mặt)
- **Mặt 1:** Quy trình giao việc 5 bước; quy tắc xanh/vàng/đỏ; năm quyết định của nhà khoa học; bảng chọn công cụ.
- **Mặt 2:** **5 câu lệnh mẫu dùng ngay** (1.2 ma trận bằng chứng; 2.2 kiểm tra logic thuyết minh; 3.1 kiểm tra tiến độ; 4.2 rà soát dữ liệu; 5.2 phản biện bài báo) + mã QR tới thư mục tài liệu demo.

---

## 10. PHƯƠNG ÁN DỰ PHÒNG

| Rủi ro | Phương án |
|---|---|
| Mất mạng / công cụ AI không phản hồi | Video demo quay sẵn |
| Demo chậm, vượt giờ | Dừng, chuyển ảnh chụp từ `ket-qua-mau/` |
| Kết quả AI khi chạy trực tiếp khác kết quả mẫu | Biến thành điểm nói: "đây là lý do cần kiểm tra – so với kết quả tái lập bằng mã đã lưu" |
| AI lại chọn sai phương pháp ngoại lệ | Tận dụng làm minh họa sống cho bài học ở Slide 15 |
| Phần trước quá giờ | Rút gọn Slide 14, 16 (chỉ ảnh); Slide 2 chỉ nói kỹ thẻ ① và ②. Không cắt Slide 20–21 |
| Bị hỏi sâu về các ví dụ Google | Trả lời theo "cách nói đúng mức" ở Slide 2; dẫn DOI Mục 7.1 |
| Câu hỏi bảo mật, pháp lý vượt phạm vi | Ghi nhận, trả lời sau khi tham vấn bộ phận chuyên trách |

---

## 11. NGUỒN THAM KHẢO

### 11.1. Các ví dụ AI trong khoa học (Slide 2)
- Tsoukalas G. et al. (2026). Advancing mathematics research with AI-driven formal proof search. *Science* 394(6820), 234–239. https://doi.org/10.1126/science.aej2213 — preprint: https://arxiv.org/abs/2605.22763
- Penadés J.R., Gottweis J., … Costa T.R.D. (2025). AI mirrors experimental science to uncover a mechanism of gene transfer crucial to bacterial evolution. *Cell* 188(23), 6654–6665. https://doi.org/10.1016/j.cell.2025.08.018
- He L. et al. (2025). Chimeric infective particles expand species boundaries in phage-inducible chromosomal island mobilization. *Cell*. https://doi.org/10.1016/j.cell.2025.08.019
- Gottweis J. et al. (2026). Accelerating scientific discovery with Co-Scientist. *Nature*. https://doi.org/10.1038/s41586-026-10644-y — preprint "Towards an AI co-scientist": https://arxiv.org/abs/2502.18864
- Imperial College London (2025). Google's AI co-scientist could enhance research, say Imperial researchers. https://www.imperial.ac.uk/news/261293/googles-ai-co-scientist-could-enhance-research/
- Rizvi S.A. et al. (2025). Scaling Large Language Models for Next-Generation Single-Cell Analysis. bioRxiv. https://doi.org/10.1101/2025.04.14.648850
- Google (2025). How a Gemma model helped discover a new potential cancer therapy pathway. https://blog.google/technology/ai/google-gemma-ai-cancer-therapy-discovery/
- Novikov A. et al. (2025). AlphaEvolve: A coding agent for scientific and algorithmic discovery. https://arxiv.org/abs/2506.13131 — blog: https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/
- Aygün E. et al. (2026). An AI system to help scientists write expert-level empirical software. *Nature* 654, 909–916. https://doi.org/10.1038/s41586-026-10658-6 — preprint: https://arxiv.org/abs/2509.06503 — blog: https://research.google/blog/accelerating-scientific-discovery-with-ai-powered-empirical-software/

### 11.2. Bối cảnh và số liệu chung
- Stanford HAI – AI Index Report 2026: https://hai.stanford.edu/ai-index/2026-ai-index-report
- METR (2025). Measuring AI Ability to Complete Long Tasks: https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
- GitHub Octoverse 2025: https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/
- Stack Overflow Developer Survey 2025 – AI: https://survey.stackoverflow.co/2025/ai
- Prithvi-EO-2.0: https://arxiv.org/abs/2412.02732
- AlphaEarth Foundations: https://arxiv.org/abs/2507.22291
- ECMWF – AI forecasts become operational: https://www.ecmwf.int/node/29308
- Gemini Robotics: https://arxiv.org/abs/2503.20020
- GNoME & A-Lab – Berkeley Lab: https://newscenter.lbl.gov/2023/11/29/google-deepmind-new-compounds-materials-project/

### 11.3. Pháp lý Việt Nam
- Luật Trí tuệ nhân tạo số 134/2025/QH15: https://congbao.chinhphu.vn/van-ban/luat-so-134-2025-qh15-468694.htm
- Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15: https://vanban.chinhphu.vn/?pageid=27160&docid=214590&classid=1&typegroupid=3

### 11.4. Chuyên môn tình huống A
- ISO 9223:2012 – Corrosion of metals and alloys — Corrosivity of atmospheres — Classification, determination and estimation.
- ISO 9224:2012 – Guiding values for the corrosivity categories (mô hình dài hạn).

### 11.5. Khoa học mở và Skill (giữ từ v1, cần bổ sung URL – N17)
- AI4S Open Science; AIPOCH Open Science; K-Dense Scientific Agent Skills; CES Global.
- Wilkinson M.D. et al. (2016). The FAIR Guiding Principles. *Scientific Data*. https://www.nature.com/articles/sdata201618
- UNESCO (2021). Recommendation on Open Science. https://www.unesco.org/en/open-science

---

## 12. GIẢI NGHĨA THUẬT NGỮ (CHO NGƯỜI TRÌNH BÀY)

Nguyên tắc: **trên slide dùng lời thường**; thuật ngữ chỉ xuất hiện khi cần, và lần đầu nói phải kèm câu giải nghĩa dưới đây.

| Thuật ngữ | Nói bằng lời thường |
|---|---|
| AI tạo sinh | AI tạo ra nội dung mới – văn bản, hình ảnh, mã – như ChatGPT, Gemini, Claude |
| AI Agent | AI được giao một nhiệm vụ, tự lập kế hoạch, dùng công cụ (tìm kiếm, chạy mã, đọc – ghi tệp) và tự kiểm tra cho đến khi xong |
| Chatbot | AI hỏi – đáp trong một cuộc trò chuyện |
| Skill | Một "quy trình mẫu" đóng gói sẵn (hướng dẫn + biểu mẫu + mã), AI tự dùng lại khi gặp việc tương tự |
| Subagent / Multi-agent | Một trợ lý con được giao việc chuyên biệt / nhiều trợ lý phối hợp như một nhóm |
| Prompt / câu lệnh | Đoạn văn bản người dùng viết để giao việc cho AI |
| Mã nguồn mở | Phần mềm hoặc mô hình công bố công khai, ai cũng tải về, dùng và kiểm tra được |
| Đánh giá hồi cứu | Chạy lại mô hình trên dữ liệu quá khứ để so sánh công bằng với các mô hình khác |
| Kiểm chứng hình thức (Lean) | Máy kiểm tra từng bước của một chứng minh toán học; bước sai không thể qua |
| TOW (thời gian ẩm ướt) | Số giờ trong năm bề mặt kim loại bị ẩm (theo ISO 9223: RH > 80% và T > 0 °C) |
| Cấp ăn mòn C1–CX | Thang 6 mức độ ăn mòn của khí quyển theo ISO 9223 – C1 rất thấp, CX cực cao |
| C = A·tⁿ | A: lượng kim loại mất trong năm đầu; n: tốc độ có chậm lại theo thời gian không (n < 1 → lớp gỉ che chắn dần) |
| Ngoại lệ | Giá trị lệch bất thường so với các giá trị cùng điều kiện – có thể do lỗi đo, lỗi ghi, hoặc hiện tượng thật |
| Mẫu lặp | Các mẫu giống hệt nhau, phơi cùng điều kiện, để kiểm tra độ lặp lại của phép đo |
| Dữ liệu giả lập | Dữ liệu tạo ra có chủ đích để minh họa – không phải số đo thật |
