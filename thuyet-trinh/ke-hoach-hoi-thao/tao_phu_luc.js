// Sinh "Phụ lục – Định hướng nội dung trình bày tại hội thảo" (.docx) theo thể thức văn bản hành chính.
// Chạy: node tao_phu_luc.js  → PHU-LUC-DINH-HUONG-TRINH-BAY.docx (cùng thư mục)
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, AlignmentType,
  WidthType, BorderStyle, ShadingType, LevelFormat, VerticalAlign, Footer, PageNumber,
} = require("docx");

const FONT = "Times New Roman";
const SZ = 26; // 13 pt
const W = 9071; // A4 210 mm − lề trái 30 mm − lề phải 15 mm = 165 mm ≈ 9354 DXA; để 9071 cho an toàn khi in

const run = (t, o = {}) => new TextRun({ text: t, font: FONT, size: o.size || SZ, bold: o.b, italics: o.i });
const runs = (parts) => parts.map((p) => (typeof p === "string" ? run(p) : run(p.t, p)));
const P = (parts, o = {}) => new Paragraph({
  children: runs(Array.isArray(parts) ? parts : [parts]),
  alignment: o.align || AlignmentType.JUSTIFIED,
  spacing: { before: o.before ?? 60, after: o.after ?? 60, line: 300 },
  indent: o.noIndent ? undefined : { firstLine: o.firstLine ?? 567 },
  keepNext: o.keep,
});
const C = (t, o = {}) => P(Array.isArray(t) ? t : [{ t, b: o.b, i: o.i, size: o.size }], { align: AlignmentType.CENTER, noIndent: true, before: o.before ?? 0, after: o.after ?? 0 });
const H1 = (t) => P([{ t, b: true }], { noIndent: false, before: 180, after: 60, keep: true });
const H2 = (t) => P([{ t, b: true, i: true }], { before: 120, keep: true });
const B = (parts) => new Paragraph({
  children: runs(Array.isArray(parts) ? parts : [parts]), numbering: { reference: "gach", level: 0 },
  alignment: AlignmentType.JUSTIFIED, spacing: { before: 30, after: 30, line: 300 },
});

const border = { style: BorderStyle.SINGLE, size: 4, color: "000000" };
const borders = { top: border, bottom: border, left: border, right: border };
function table(widths, rows, headerRows = 1) {
  const sum = widths.reduce((a, b) => a + b, 0);
  return new Table({
    width: { size: sum, type: WidthType.DXA }, columnWidths: widths,
    rows: rows.map((r, ri) => new TableRow({
      tableHeader: ri < headerRows,
      children: r.map((cell, ci) => {
        const head = ri < headerRows;
        const bold = head || (typeof cell === "object" && cell.b);
        const txt = typeof cell === "object" ? cell.t : cell;
        const lines = String(txt).split("\n");
        return new TableCell({
          borders, width: { size: widths[ci], type: WidthType.DXA }, verticalAlign: VerticalAlign.CENTER,
          shading: head ? { fill: "E7E6E6", type: ShadingType.CLEAR, color: "auto" } : (typeof cell === "object" && cell.fill ? { fill: cell.fill, type: ShadingType.CLEAR, color: "auto" } : undefined),
          margins: { top: 40, bottom: 40, left: 80, right: 80 },
          children: lines.map((l) => new Paragraph({
            alignment: head || (typeof cell === "object" && cell.c) ? AlignmentType.CENTER : AlignmentType.LEFT,
            spacing: { before: 0, after: 0, line: 264 },
            children: [run(l, { b: bold, size: 24 })],
          })),
        });
      }),
    })),
  });
}
const gap = () => new Paragraph({ children: [], spacing: { before: 0, after: 0 } });

// ------------------------------------------------------------------ NỘI DUNG
const body = [];
body.push(C("PHỤ LỤC", { b: true }));
body.push(C("ĐỊNH HƯỚNG NỘI DUNG TRÌNH BÀY TẠI HỘI THẢO", { b: true }));
body.push(C("“AI Agent và sự chuyển đổi phương thức nghiên cứu khoa học”", { b: true }));
body.push(C("(Kèm theo Kế hoạch số …/KH-… ngày … tháng … năm 2026 của …)", { i: true, before: 40, after: 200 }));

// I
body.push(H1("I. MỤC ĐÍCH, YÊU CẦU"));
body.push(H2("1. Mục đích"));
body.push(B("Cập nhật cho cán bộ, nhà khoa học của Trung tâm tốc độ phát triển, năng lực và xu thế ứng dụng trí tuệ nhân tạo (AI), đặc biệt là AI Agent, trong nghiên cứu khoa học."));
body.push(B("Hướng dẫn lựa chọn và sử dụng công cụ AI phù hợp với từng loại công việc nghiên cứu; giới thiệu cách sử dụng cơ bản Claude trên máy tính Windows."));
body.push(B("Minh họa ứng dụng AI Agent trong toàn bộ chu trình thực hiện nhiệm vụ khoa học và công nghệ trên một ví dụ thực tế, gắn với lĩnh vực của Trung tâm (ăn mòn khí quyển của kim loại trong khí hậu nhiệt đới)."));
body.push(B("Định hướng cách khai thác AI đối với nhiệm vụ có dữ liệu mật: AI chỉ tham gia xây dựng công cụ, dữ liệu được xử lý trên máy tính không kết nối Internet."));
body.push(B("Thu thập ý kiến, đề xuất của các phòng, ban về các quy trình có thể thí điểm tự động hóa."));
body.push(H2("2. Yêu cầu"));
body.push(B("Nội dung chính xác, có căn cứ; số liệu, ví dụ quốc tế có nguồn được kiểm tra; ví dụ minh họa dùng dữ liệu thật đã công bố."));
body.push(B("Ngôn ngữ dễ hiểu, phù hợp với người nghe không chuyên về công nghệ thông tin; mỗi slide một ý chính, phần chi tiết đưa vào tài liệu phát tay."));
body.push(B("Chấp hành nghiêm quy định về bảo vệ bí mật nhà nước, an toàn thông tin và bản quyền; không đưa dữ liệu nội bộ, dữ liệu mật lên dịch vụ AI trực tuyến."));
body.push(B("Các phần minh họa được thực hiện trước, tại hội thảo chỉ trình chiếu kết quả (video, ảnh chụp); bảo đảm đúng thời lượng 120 phút."));

// II
body.push(H1("II. BỐ CỤC VÀ THỜI LƯỢNG"));
body.push(P("Bài trình bày gồm 27 slide, chia thành 6 phần, kèm 5 phụ lục dự phòng (không trình bày, dùng khi có câu hỏi). Tổng thời lượng 120 phút, trong đó trình bày 108 phút, trao đổi – thảo luận 12 phút."));
body.push(table([700, 5171, 1600, 1600], [
  ["Phần", "Nội dung", "Slide", "Thời lượng"],
  [{ t: "I", c: true }, "Tổng quan: AI và sự thay đổi phương thức nghiên cứu khoa học", { t: "1 – 4", c: true }, { t: "18 phút", c: true }],
  [{ t: "II", c: true }, "Lựa chọn và sử dụng công cụ AI phù hợp; công cụ tìm tài liệu; giới thiệu Claude", { t: "5 – 12", c: true }, { t: "32 phút", c: true }],
  [{ t: "III", c: true }, "AI Agent trong chu trình thực hiện nhiệm vụ khoa học (minh họa 1, 2; mô hình 3D)", { t: "13 – 19", c: true }, { t: "30 phút", c: true }],
  [{ t: "IV", c: true }, "Đề tài mật: ứng dụng AI khi dữ liệu không được đưa lên Internet (ranh giới pháp lý, quy trình, minh họa 3)", { t: "20 – 23", c: true }, { t: "15 phút", c: true }],
  [{ t: "V", c: true }, "Skill, khoa học mở và tự động hóa", { t: "24 – 26", c: true }, { t: "13 phút", c: true }],
  [{ t: "VI", c: true }, "Trao đổi, thảo luận", { t: "27", c: true }, { t: "12 phút", c: true }],
  [{ t: "", c: true }, { t: "Tổng cộng", b: true }, { t: "27 slide", c: true, b: true }, { t: "120 phút", c: true, b: true }],
]));

// III
body.push(H1("III. ĐỊNH HƯỚNG NỘI DUNG TỪNG PHẦN"));
const part = (title, mt, nd, kq) => {
  body.push(H2(title));
  body.push(P([{ t: "Mục tiêu: ", b: true }, mt]));
  body.push(P([{ t: "Nội dung chính:", b: true }]));
  nd.forEach((x) => body.push(B(x)));
  body.push(P([{ t: "Kết quả cần đạt: ", b: true }, kq]));
};
part("1. Phần I – Tổng quan (18 phút, slide 1 – 4)",
  "giúp người nghe nắm được AI đang phát triển nhanh như thế nào và đã thay đổi cách nghiên cứu khoa học ra sao.",
  [
    "Số liệu phát triển: khoảng một nửa dân số dùng AI tạo sinh chỉ sau 3 năm; AI đạt mức huy chương vàng Olympic Toán quốc tế 2025; độ dài công việc AI tự thực hiện được tăng từ vài giây (2019) lên hơn 16 giờ (2026).",
    "Ví dụ ứng dụng AI trong viễn thám, khí tượng, sinh học, vật liệu – liên hệ với các hướng nghiên cứu của Trung tâm.",
    "Sáu năng lực cốt lõi và các tính năng mới của AI Agent (làm việc tự chủ nhiều giờ, nghiên cứu chuyên sâu, sử dụng máy tính, kết nối chuẩn mở MCP); giới hạn: AI vẫn có thể sai, nhà khoa học phải kiểm tra.",
    "Xu thế chuyển từ thao tác thủ công, riêng lẻ sang quy trình liên tục; nhà khoa học giữ vai trò dẫn dắt.",
  ],
  "người nghe phân biệt được AI trả lời câu hỏi với AI Agent thực hiện nhiệm vụ, và nhận thức được cả năng lực lẫn giới hạn của AI.");
part("2. Phần II – Lựa chọn và sử dụng công cụ AI phù hợp (32 phút, slide 5 – 12)",
  "giúp người nghe chọn đúng công cụ cho đúng việc và bắt đầu sử dụng được Claude trên máy tính Windows.",
  [
    "Phân loại công việc nghiên cứu theo 5 bậc (hỏi – đáp; làm việc với một tài liệu; tổng hợp nhiều nguồn; xử lý nhiều tệp, dữ liệu; chuỗi nhiệm vụ tự động) và công cụ phù hợp với từng bậc.",
    "Các công cụ AI phổ biến (Perplexity, NotebookLM, ChatGPT, Gemini, Claude) và chính sách sử dụng dữ liệu của từng công cụ.",
    "Công cụ tìm và đọc tài liệu khoa học: ưu tiên kênh hợp pháp (Unpaywall, CORE, Google Scholar Labs, Semantic Scholar, Elicit, Consensus, SciSpace, Scopus AI, Web of Science); nguồn tiếng Việt – tiếng Nga (VJOL, CyberLeninka, eLIBRARY.ru); cảnh báo về Sci-Hub, Sci-Bot (vi phạm bản quyền, rủi ro an toàn thông tin).",
    "Giới thiệu Claude trên Windows (trình duyệt và ứng dụng): các mô hình, năm tính năng dùng ngay (dự án, tạo tệp – chạy mã, nghiên cứu chuyên sâu, Cowork, tác vụ theo lịch).",
    "Sáu bước bắt đầu sử dụng; minh họa tổng hợp dữ liệu ăn mòn từ 3 nguồn công bố thành bảng và báo cáo.",
    "Phương pháp giao việc cho AI Agent theo 5 bước (nhiệm vụ – dữ liệu – đầu ra – dẫn nguồn, lưu mã – kiểm tra), ví dụ với 387 số đo thực địa.",
    "Tổ chức không gian làm việc theo từng nhiệm vụ; giới thiệu Skill, Subagent và hệ thống nhiều Agent.",
  ],
  "người nghe tự tạo được tài khoản, dự án và viết được một yêu cầu đủ 5 bước cho công việc của mình.");
part("3. Phần III – AI Agent trong chu trình thực hiện nhiệm vụ khoa học (30 phút, slide 13 – 19)",
  "minh họa AI Agent hỗ trợ từng công đoạn của một nhiệm vụ khoa học và công nghệ, trên một dự án nghiên cứu thật.",
  [
    "Ví dụ xuyên suốt: “Khả năng áp dụng mô hình ăn mòn khí quyển quốc tế cho khí hậu nhiệt đới Việt Nam”, dùng 387 số đo thực địa đã công bố (quốc tế, Việt Nam, Nga).",
    "Tổng quan tài liệu: lập ma trận bằng chứng, xác định 3 khoảng trống nghiên cứu.",
    "Minh họa 1: xây dựng phiếu đề xuất, thuyết minh theo biểu mẫu của Trung tâm; lập tiến độ, dự toán theo Thông tư 03/2023/TT-BTC và quy định của Bộ Quốc phòng; AI không tự đặt số liệu tài chính.",
    "Minh họa 2: AI viết và chạy mã Python xử lý dữ liệu – phát hiện lỗi đơn vị trong dữ liệu công bố; mô hình quốc tế dự đoán thấp hơn thực đo ở Việt Nam khoảng 31%; sau hiệu chỉnh theo vùng, xếp đúng cấp ăn mòn 9/12 trạm (trước là 2/12).",
    "Mô hình 3D mô phỏng quá trình ăn mòn thép tại Nha Trang trong 30 năm và so sánh thép – kẽm – đồng – nhôm; phân biệt rõ phần định lượng (số đo, tiêu chuẩn ISO) và phần minh họa.",
    "Công bố kết quả theo nhiều định dạng: tạp chí Scopus/Web of Science, danh mục ВАК (Nga), tạp chí trong nước, báo cáo của Trung tâm.",
    "Tổng kết chu trình: nhà khoa học xác nhận ở mỗi bước.",
  ],
  "người nghe thấy được AI hỗ trợ cụ thể ở công đoạn nào, kết quả ra sao, và trách nhiệm kiểm tra của nhà khoa học ở từng công đoạn.");
part("4. Phần IV – Đề tài mật: ứng dụng AI khi dữ liệu không được đưa lên Internet (15 phút, slide 20 – 23)",
  "định hướng cách khai thác AI cho nhiệm vụ có nội dung bí mật nhà nước, bí mật quân sự mà vẫn tuân thủ pháp luật về bảo vệ bí mật nhà nước.",
  [
    "Ranh giới pháp lý (slide 20): Luật Bảo vệ bí mật nhà nước số 117/2025/QH15 (hiệu lực từ 01/3/2026) nghiêm cấm soạn thảo, lưu giữ tài liệu có nội dung bí mật nhà nước trên thiết bị đang kết nối Internet, mạng máy tính, mạng viễn thông (trừ mạng LAN độc lập theo quy định) và nghiêm cấm sử dụng hệ thống trí tuệ nhân tạo, công nghệ mới để xâm phạm bí mật nhà nước; phân định rõ thông tin được và không được đưa cho AI trực tuyến; cảnh báo nguy cơ suy luận ra thông tin mật từ việc ghép nhiều thông tin.",
    "Mô hình ba vùng và quy trình 6 bước (slide 21): vùng A – máy có Internet (AI viết công cụ, chạy thử với dữ liệu giả, quét mã, đóng gói kèm mã băm); vùng B – chuyển giao bằng thiết bị lưu trữ được cấp phép, quét mã độc, đối chiếu mã băm, ghi sổ; vùng C – máy không kết nối Internet hoặc mạng LAN độc lập (chạy với dữ liệu thật, kết quả lưu tại chỗ). Luồng một chiều, mỗi bước có điểm kiểm soát và người chịu trách nhiệm.",
    "Minh họa 3 (slide 22, dữ liệu giả lập): công cụ ước lượng lộ trình thiết bị bay không người lái theo địa hình và khí hậu nhiệt đới; kết quả kiểm tra an toàn (quét mã chặn thư viện kết nối mạng, đối chiếu mã băm khớp); trọng tâm là quy trình, mô hình đã được đơn giản hóa.",
    "Sai lầm thường gặp và phương án khác (slide 23): chụp màn hình, dán trích đoạn tài liệu mật; dùng Cowork, tiện ích AI trên trình duyệt, tính năng sử dụng máy tính hoặc đồng bộ đám mây trên máy có tài liệu mật; mang nhật ký lỗi từ máy mật ra ngoài; dùng tài khoản cá nhân. Phương án mô hình AI chạy cục bộ, mạng LAN độc lập – chỉ khi được cấp có thẩm quyền cho phép.",
  ],
  "người nghe nắm vững quy định pháp luật, quy trình và các điểm kiểm soát; nhận biết được các sai lầm dễ làm lộ dữ liệu.");
part("5. Phần V – Skill, khoa học mở và tự động hóa (13 phút, slide 24 – 26)",
  "giới thiệu hướng chuẩn hóa và tự động hóa dần các quy trình nghiên cứu tại Trung tâm.",
  [
    "Skill (quy trình mẫu đóng gói) và thư viện Skill khoa học mở; kết quả thí nghiệm trên cùng bộ dữ liệu khi không dùng và có dùng Skill.",
    "Khoa học mở: dữ liệu công bố mở được tái sử dụng, phát hiện lỗi, tạo tri thức mới; ba mức tự động hóa (hỗ trợ từng bước – bán tự động – tự động toàn trình).",
    "Bản đồ quy trình tự động dự kiến của Trung tâm (QT-00 đến QT-06) và năm quyết định thuộc về nhà khoa học.",
  ],
  "các phòng xác định được quy trình có thể thí điểm tự động hóa.");
part("6. Phần VI – Trao đổi, thảo luận (12 phút, slide 27)",
  "giải đáp thắc mắc và thu thập đề xuất.",
  [
    "Kết quả phiếu khảo sát trước hội thảo.",
    "Các quy trình các phòng, ban muốn thí điểm tự động hóa; đầu mối liên hệ.",
    "Câu hỏi thường gặp được chuẩn bị sẵn (phụ lục E của bài trình bày): quy định sử dụng dịch vụ AI, dữ liệu được phép đưa lên AI, chi phí, trách nhiệm đối với kết quả, yêu cầu về lập trình, công bố bài báo có sử dụng AI.",
  ],
  "có danh sách đề xuất thí điểm và các vấn đề cần hướng dẫn tiếp.");

// IV
body.push(H1("IV. HÌNH THỨC TRÌNH BÀY"));
body.push(B("Trình chiếu slide; mỗi slide một ý chính, tối đa một bảng hoặc một hình."));
body.push(B("Các phần minh họa (tổng hợp dữ liệu nhiều nguồn; phiếu đề xuất, thuyết minh; tiến độ, kinh phí; xử lý dữ liệu; mô hình 3D; công cụ cho máy không kết nối Internet) được thực hiện trước hội thảo, ghi hình màn hình 1 – 2 phút mỗi phần; tại hội thảo trình chiếu video và ảnh kết quả, không phụ thuộc kết nối Internet."));
body.push(B("Mô hình 3D tương tác được chạy trực tiếp từ tệp trên máy trình chiếu, không cần Internet."));
body.push(B("Phát tài liệu phát tay (bảng chọn công cụ, mẫu giao việc 5 bước, 6 bước bắt đầu với Claude, danh mục công cụ tìm tài liệu, giải nghĩa thuật ngữ) và phiếu khảo sát trước – sau hội thảo."));

// V
body.push(H1("V. YÊU CẦU VỀ BẢO MẬT, AN TOÀN THÔNG TIN VÀ BẢN QUYỀN"));
body.push(B("Dữ liệu dùng trong bài trình bày và các phần minh họa chỉ gồm dữ liệu đã công bố (bộ dữ liệu ăn mòn khí quyển C-OLR, giấy phép MIT) và dữ liệu giả lập."));
body.push(B("Biểu mẫu đã điền nội dung nhiệm vụ thật chỉ xử lý bằng tài khoản dịch vụ AI dạng tổ chức (không dùng dữ liệu để huấn luyện mô hình) hoặc thay bằng nội dung giả định khi ghi hình; không lưu vào kho mã công khai."));
body.push(B("Tuyệt đối không đưa thông tin, tài liệu thuộc phạm vi bí mật nhà nước, bí mật quân sự lên dịch vụ AI trực tuyến, theo Luật Bảo vệ bí mật nhà nước số 117/2025/QH15; việc chuyển tệp sang máy tính không kết nối Internet thực hiện theo quy định của Bộ Quốc phòng và quy chế của Trung tâm."));
body.push(B("Không trình diễn, không chụp ảnh màn hình bất kỳ dữ liệu thật nào của nhiệm vụ có nội dung bí mật; minh họa 3 chỉ dùng dữ liệu giả lập."));
body.push(B("Không khuyến nghị sử dụng Sci-Hub, Sci-Bot; nội dung này chỉ nêu để cảnh báo về bản quyền và an toàn thông tin."));
body.push(B("Việc sử dụng dịch vụ AI nước ngoài tại đơn vị thực hiện theo quy định hiện hành; nội dung trả lời được thống nhất với cơ quan chức năng trước hội thảo."));

// VI
body.push(H1("VI. CÔNG TÁC CHUẨN BỊ"));
body.push(table([520, 4100, 1550, 1500, 1401], [
  ["TT", "Nội dung công việc", "Cơ quan, cá nhân thực hiện", "Thời hạn", "Sản phẩm"],
  [{ t: "1", c: true }, "Hoàn thiện bài trình bày, xác nhận các số liệu, nguồn còn mở", "Người trình bày", "Trước … ngày", "Bộ slide"],
  [{ t: "2", c: true }, "Cung cấp biểu mẫu phiếu đề xuất, thuyết minh, tiến độ, dự toán, báo cáo tổng hợp, Mẫu 21, 22", "Phòng/ban quản lý khoa học", "Trước … ngày", "Biểu mẫu trống"],
  [{ t: "3", c: true }, "Xác nhận văn bản định mức kinh phí áp dụng", "Phòng/ban tài chính", "Trước … ngày", "Văn bản định mức"],
  [{ t: "4", c: true }, "Thống nhất nội dung trả lời về quy định sử dụng dịch vụ AI, bảo mật", "Bộ phận bảo mật, CNTT", "Trước … ngày", "Nội dung phụ lục E"],
  [{ t: "5", c: true }, "Thực hiện trước và ghi hình 6 phần minh họa; chụp ảnh kết quả", "Người trình bày", "Trước … ngày", "Video, ảnh"],
  [{ t: "6", c: true }, "Kiểm tra máy chiếu, máy trình chiếu, phát video và mô hình 3D không cần Internet", "Bộ phận CNTT, hậu cần", "Trước 1 ngày", "Biên bản kiểm tra"],
  [{ t: "7", c: true }, "In tài liệu phát tay, phiếu khảo sát", "Bộ phận văn thư", "Trước 2 ngày", "Tài liệu in"],
  [{ t: "8", c: true }, "Tổng hợp phiếu khảo sát, đề xuất thí điểm sau hội thảo", "Người trình bày, phòng/ban quản lý khoa học", "Sau … ngày", "Báo cáo tổng hợp"],
]));
body.push(gap());

// VII
body.push(H1("VII. TÀI LIỆU KÈM THEO"));
body.push(B("Danh sách slide và nội dung từng slide (27 slide, 5 phụ lục dự phòng)."));
body.push(B("Tài liệu phát tay."));
body.push(B("Bộ câu lệnh minh họa kèm kết quả mong đợi."));
body.push(B("Dự án nghiên cứu minh họa: dữ liệu, mã nguồn, kết quả, mô hình 3D, bản thảo bài báo."));
body.push(B("Công cụ mẫu cho máy tính không kết nối Internet (dữ liệu giả lập)."));

const doc = new Document({
  styles: { default: { document: { run: { font: FONT, size: SZ } } } },
  numbering: { config: [{ reference: "gach", levels: [{ level: 0, format: LevelFormat.BULLET, text: "-", alignment: AlignmentType.LEFT,
    style: { paragraph: { indent: { left: 851, hanging: 284 } } } }] }] },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1134, bottom: 1134, left: 1701, right: 850 } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 24 })] })] }) },
    children: body,
  }],
});
Packer.toBuffer(doc).then((buf) => {
  const out = path.join(__dirname, "PHU-LUC-DINH-HUONG-TRINH-BAY.docx");
  fs.writeFileSync(out, buf);
  console.log("Đã ghi", out);
});
