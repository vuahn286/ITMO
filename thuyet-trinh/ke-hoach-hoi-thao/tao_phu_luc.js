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
body.push(B("Minh họa ứng dụng AI Agent trong toàn bộ chu trình thực hiện nhiệm vụ khoa học và công nghệ, từ tìm kiếm tài liệu đến công bố kết quả, trên hai dự án minh họa gắn với lĩnh vực của Trung tâm: dự án nghiên cứu về ăn mòn khí quyển của kim loại trong khí hậu nhiệt đới và bộ minh họa đi kèm bài trình bày (mục III)."));
body.push(B("Định hướng cách khai thác AI đối với nhiệm vụ có dữ liệu mật: AI chỉ tham gia xây dựng công cụ, dữ liệu được xử lý trên máy tính không kết nối Internet."));
body.push(B("Thu thập ý kiến, đề xuất của các phòng, ban về các quy trình có thể thí điểm tự động hóa."));
body.push(H2("2. Yêu cầu"));
body.push(B("Nội dung chính xác, có căn cứ; ví dụ minh họa dùng dữ liệu thật đã công bố; phần cần cài sẵn lỗi hoặc thay cho dữ liệu mật dùng dữ liệu giả lập, ghi rõ trên slide; ngôn ngữ dễ hiểu với người nghe không chuyên về công nghệ thông tin."));
body.push(B("Chấp hành nghiêm quy định về bảo vệ bí mật nhà nước và an toàn thông tin; không đưa dữ liệu nội bộ, dữ liệu mật lên dịch vụ AI trực tuyến."));
body.push(B("Các phần minh họa được thực hiện trước, tại hội thảo chỉ trình chiếu kết quả; bảo đảm đúng thời lượng 120 phút."));

// II
body.push(H1("II. BỐ CỤC VÀ THỜI LƯỢNG"));
body.push(P("Bài trình bày gồm 27 slide, chia thành 6 phần; tổng thời lượng 120 phút, trong đó trình bày 108 phút, trao đổi – thảo luận 12 phút."));
body.push(table([700, 5171, 1600, 1600], [
  ["Phần", "Nội dung", "Slide", "Thời lượng"],
  [{ t: "I", c: true }, "Tổng quan: AI và sự thay đổi phương thức nghiên cứu khoa học", { t: "1 – 4", c: true }, { t: "18 phút", c: true }],
  [{ t: "II", c: true }, "Lựa chọn và sử dụng công cụ AI phù hợp; giới thiệu Claude", { t: "5 – 11", c: true }, { t: "28 phút", c: true }],
  [{ t: "III", c: true }, "AI Agent trong chu trình thực hiện nhiệm vụ khoa học: tài liệu, tổng quan → thuyết minh → xử lý dữ liệu (minh họa 1, 2; mô hình 3D) → công bố", { t: "12 – 19", c: true }, { t: "34 phút", c: true }],
  [{ t: "IV", c: true }, "Đề tài mật: ứng dụng AI khi dữ liệu không được đưa lên Internet (ranh giới pháp lý, quy trình, minh họa 3)", { t: "20 – 23", c: true }, { t: "15 phút", c: true }],
  [{ t: "V", c: true }, "Skill, khoa học mở và tự động hóa", { t: "24 – 26", c: true }, { t: "13 phút", c: true }],
  [{ t: "VI", c: true }, "Trao đổi, thảo luận", { t: "27", c: true }, { t: "12 phút", c: true }],
  [{ t: "", c: true }, { t: "Tổng cộng", b: true }, { t: "27 slide", c: true, b: true }, { t: "120 phút", c: true, b: true }],
]));

// III
body.push(H1("III. DỰ ÁN MINH HỌA"));
body.push(P("Các phần minh họa của bài trình bày được thực hiện trên hai dự án đã xây dựng hoàn chỉnh với sự hỗ trợ của AI Agent; toàn bộ kết quả chạy lại được bằng một lệnh."));
body.push(table([520, 2000, 3851, 1500, 1200], [
  ["TT", "Dự án", "Nội dung chính", "Dữ liệu", "Sử dụng tại slide"],
  [{ t: "1", c: true }, "Dự án nghiên cứu “Khả năng áp dụng mô hình ăn mòn khí quyển quốc tế cho khí hậu nhiệt đới Việt Nam”", "Thực hiện đủ vòng đời một nhiệm vụ: tổng quan tài liệu (13 tài liệu đã xác minh, ma trận bằng chứng, 3 khoảng trống) → bản nháp đề xuất → hợp nhất, kiểm tra dữ liệu → mô hình, hiệu chỉnh theo vùng → mô hình 3D → bản thảo bài báo → báo cáo tổng hợp; có nhật ký thực hiện, ghi cả các lần sai và sửa", "Thật, đã công bố: 387 số đo thực địa (kho dữ liệu mở C-OLR, giấy phép MIT)", { t: "9, 10, 12 – 19, 24, 25", c: true }],
  [{ t: "2", c: true }, "Bộ minh họa của bài trình bày", "Tổng hợp dữ liệu từ 3 nguồn công bố, 4 định dạng; bộ dữ liệu ăn mòn, khí tượng và kế hoạch công việc có cài sẵn lỗi để AI phát hiện; công cụ ước lượng lộ trình thiết bị bay không người lái chạy trên máy không kết nối Internet", "Thật (trích từ C-OLR) và giả lập", { t: "8, 14, 16, 22", c: true }],
]));

// IV
body.push(H1("IV. ĐỊNH HƯỚNG NỘI DUNG TỪNG PHẦN"));
const part = (title, mt, nd) => {
  body.push(H2(title));
  body.push(P([{ t: "Mục tiêu: ", b: true }, mt]));
  nd.forEach((x) => body.push(B(x)));
};
part("1. Phần I – Tổng quan (18 phút)",
  "nắm được tốc độ phát triển, năng lực, giới hạn của AI và xu thế thay đổi phương thức nghiên cứu.",
  [
    "Số liệu phát triển: khoảng một nửa dân số dùng AI tạo sinh chỉ sau 3 năm; AI đạt mức huy chương vàng Olympic Toán quốc tế 2025; độ dài công việc AI tự thực hiện được tăng từ vài giây (2019) lên hơn 16 giờ (2026).",
    "Ví dụ ứng dụng AI trong viễn thám, khí tượng, sinh học, vật liệu – liên hệ với các hướng nghiên cứu của Trung tâm.",
    "Sáu năng lực cốt lõi và các tính năng mới của AI Agent; giới hạn: AI vẫn có thể sai, nhà khoa học phải kiểm tra.",
    "Xu thế chuyển từ thao tác thủ công, riêng lẻ sang quy trình liên tục; nhà khoa học giữ vai trò dẫn dắt.",
  ]);
part("2. Phần II – Lựa chọn và sử dụng công cụ AI phù hợp (28 phút)",
  "chọn đúng công cụ cho đúng việc và bắt đầu sử dụng được Claude trên máy tính Windows.",
  [
    "Phân loại công việc nghiên cứu theo 5 bậc và công cụ phù hợp với từng bậc.",
    "Các công cụ AI phổ biến (Perplexity, NotebookLM, ChatGPT, Gemini, Claude) và chính sách sử dụng dữ liệu của từng công cụ.",
    "Giới thiệu Claude trên Windows: các mô hình, năm tính năng dùng ngay (dự án, tạo tệp – chạy mã, nghiên cứu chuyên sâu, Cowork, tác vụ theo lịch); sáu bước bắt đầu sử dụng; minh họa tổng hợp dữ liệu từ 3 nguồn công bố (Dự án 2): 4 tệp khác định dạng → bảng tổng hợp, báo cáo Word; AI phát hiện nhãn đơn vị sai trong nguồn.",
    "Phương pháp giao việc cho AI Agent theo 5 bước (nhiệm vụ – dữ liệu – đầu ra – dẫn nguồn, lưu mã – kiểm tra); ví dụ câu lệnh đủ 5 bước trên dữ liệu thật của Dự án 1.",
    "Tổ chức không gian làm việc theo từng nhiệm vụ, lấy cấu trúc Dự án 1 làm mẫu (mỗi giai đoạn của nhiệm vụ một thư mục, từ quản lý dự án, tài liệu đến bài báo, báo cáo); giới thiệu Skill, Subagent và hệ thống nhiều Agent.",
  ]);
part("3. Phần III – AI Agent trong chu trình thực hiện nhiệm vụ khoa học (34 phút)",
  "minh họa AI hỗ trợ từng công đoạn của một nhiệm vụ khoa học và công nghệ, theo đúng trình tự các giai đoạn của Dự án 1; phần minh họa phát hiện lỗi dùng dữ liệu giả lập của Dự án 2.",
  [
    "Nghiên cứu tài liệu và tổng quan: tìm bài ứng viên bằng Sci-Bot – trợ lý AI trên kho Sci-Hub (câu trả lời tổng hợp kèm danh sách bài báo, DOI), bổ sung bài mới bằng Google Scholar Labs, Semantic Scholar; lọc theo tiêu đề, tóm tắt (Elicit, Consensus, Claude); lấy toàn văn theo DOI qua Sci-Hub, Unpaywall, CORE và nguồn tiếng Việt – tiếng Nga (VJOL, CyberLeninka, eLIBRARY.ru); lập ma trận bằng chứng từ 13 tài liệu đã xác minh, xác định 3 khoảng trống nghiên cứu (Dự án 1); kiểm tra DOI của mọi trích dẫn.",
    "Xây dựng thuyết minh đề tài từ khoảng trống thứ nhất của Dự án 1 (minh họa 1): phiếu đề xuất, thuyết minh theo biểu mẫu của Trung tâm; tiến độ, dự toán theo Thông tư 03/2023/TT-BTC và quy định của Bộ Quốc phòng; với kế hoạch công việc giả lập (Dự án 2), AI phát hiện đủ 3 bất hợp lý cài sẵn về trình tự công việc.",
    "Hướng dẫn xử lý dữ liệu với AI theo 5 bước: chuẩn bị dữ liệu (giữ bản gốc, từ điển dữ liệu) → kiểm tra chất lượng (chỉ đánh dấu, không tự xóa) → phân tích, lập mô hình (nhà khoa học chọn phương pháp) → kiểm định trên tập độc lập → lưu mã, nhật ký để tái lập.",
    "Minh họa 2 – áp dụng quy trình trên: AI viết và chạy mã Python xử lý dữ liệu. Với dữ liệu giả lập (Dự án 2): phát hiện đủ 14/14 lỗi cài sẵn. Với 387 số đo thật (Dự án 1): phát hiện lỗi đơn vị trong dữ liệu công bố; mô hình quốc tế dự đoán thấp hơn thực đo ở Việt Nam khoảng 31%; sau hiệu chỉnh theo vùng, xếp đúng cấp ăn mòn 9/12 trạm (trước là 2/12).",
    "Mô hình 3D tương tác (Dự án 1) mô phỏng quá trình ăn mòn thép tại Nha Trang trong 30 năm và so sánh thép – kẽm – đồng – nhôm.",
    "Công bố kết quả: bản thảo bài báo (tóm tắt Việt – Anh) và báo cáo tổng hợp của Dự án 1; chuyển đổi theo nhiều định dạng: tạp chí Scopus/Web of Science, danh mục ВАК (Nga), tạp chí trong nước, báo cáo của Trung tâm; nhà khoa học xác nhận ở mỗi bước.",
  ]);
part("4. Phần IV – Đề tài mật: ứng dụng AI khi dữ liệu không được đưa lên Internet (15 phút)",
  "khai thác AI cho nhiệm vụ có nội dung bí mật nhà nước, bí mật quân sự mà vẫn tuân thủ pháp luật về bảo vệ bí mật nhà nước.",
  [
    "Ranh giới pháp lý: Luật Bảo vệ bí mật nhà nước số 117/2025/QH15 (hiệu lực từ 01/3/2026) nghiêm cấm soạn thảo, lưu giữ tài liệu có nội dung bí mật nhà nước trên thiết bị đang kết nối Internet, mạng máy tính, mạng viễn thông (trừ mạng LAN độc lập theo quy định) và nghiêm cấm sử dụng hệ thống trí tuệ nhân tạo, công nghệ mới để xâm phạm bí mật nhà nước; phân định thông tin được và không được đưa cho AI trực tuyến.",
    "Mô hình ba vùng, quy trình 6 bước: máy có Internet (AI viết công cụ, chạy thử với dữ liệu giả, quét mã, đóng gói kèm mã băm) → chuyển giao bằng thiết bị lưu trữ được cấp phép, đối chiếu mã băm → máy không kết nối Internet hoặc mạng LAN độc lập (chạy với dữ liệu thật, kết quả lưu tại chỗ); luồng một chiều, mỗi bước có điểm kiểm soát và người chịu trách nhiệm.",
    "Minh họa 3 (Dự án 2, dữ liệu giả lập thay cho dữ liệu mật): công cụ ước lượng lộ trình thiết bị bay không người lái theo địa hình và khí hậu nhiệt đới – lộ trình vòng tránh 8 ô cấm bay; chiều về ngược gió mùa tốn năng lượng gấp 1,8 lần chiều đi nên phải đổi phương án; quét mã không phát hiện kết nối mạng, mã băm trên máy đích khớp.",
    "Sai lầm thường gặp: chụp màn hình, dán trích đoạn tài liệu mật; dùng Cowork, tiện ích AI trên trình duyệt hoặc đồng bộ đám mây trên máy có tài liệu mật; mang nhật ký lỗi từ máy mật ra ngoài; dùng tài khoản cá nhân.",
  ]);
part("5. Phần V – Skill, khoa học mở và tự động hóa (13 phút)",
  "định hướng chuẩn hóa và tự động hóa dần các quy trình nghiên cứu tại Trung tâm.",
  [
    "Skill và thư viện Skill khoa học mở; thí nghiệm trên 387 số đo của Dự án 1 khi không dùng và có dùng Skill: Skill bổ sung 3 bước kiểm tra mà phân tích ban đầu bỏ qua.",
    "Khoa học mở qua vòng đời bộ dữ liệu của Dự án 1: dữ liệu công bố mở → tái sử dụng → phát hiện lỗi đơn vị → tri thức mới → đóng góp lại cộng đồng; ba mức tự động hóa (hỗ trợ từng bước – bán tự động – tự động toàn trình).",
    "Bản đồ quy trình tự động dự kiến của Trung tâm và năm quyết định thuộc về nhà khoa học.",
  ]);
part("6. Phần VI – Trao đổi, thảo luận (12 phút)",
  "giải đáp thắc mắc, thu thập đề xuất các quy trình thí điểm tự động hóa.",
  []);

// V
body.push(H1("V. YÊU CẦU VỀ BẢO MẬT VÀ AN TOÀN THÔNG TIN"));
body.push(B("Dữ liệu dùng trong bài trình bày và các phần minh họa chỉ gồm dữ liệu đã công bố và dữ liệu giả lập; không trình chiếu dữ liệu thật của nhiệm vụ có nội dung bí mật."));
body.push(B("Tuyệt đối không đưa thông tin, tài liệu thuộc phạm vi bí mật nhà nước, bí mật quân sự lên dịch vụ AI trực tuyến; việc chuyển tệp sang máy tính không kết nối Internet thực hiện theo quy định của Bộ Quốc phòng và quy chế của Trung tâm."));
body.push(B("Truy cập Sci-Hub, Sci-Bot và các dịch vụ trực tuyến khác theo quy định truy cập Internet của đơn vị; chỉ dùng địa chỉ chính thức, không dùng trên máy tính có tài liệu mật."));

// VI
body.push(H1("VI. CÔNG TÁC CHUẨN BỊ"));
body.push(table([520, 4100, 1550, 1500, 1401], [
  ["TT", "Nội dung công việc", "Cơ quan, cá nhân thực hiện", "Thời hạn", "Sản phẩm"],
  [{ t: "1", c: true }, "Hoàn thiện bài trình bày; chạy lại 2 dự án minh họa, thực hiện trước và ghi hình các phần minh họa", "Người trình bày", "Trước … ngày", "Bộ slide, video, ảnh; kết quả 2 dự án"],
  [{ t: "2", c: true }, "Cung cấp biểu mẫu phiếu đề xuất, thuyết minh, tiến độ, dự toán, báo cáo tổng hợp", "Phòng/ban quản lý khoa học", "Trước … ngày", "Biểu mẫu trống"],
  [{ t: "3", c: true }, "Thống nhất nội dung về quy định sử dụng dịch vụ AI, bảo mật", "Bộ phận bảo mật, CNTT", "Trước … ngày", "Nội dung trả lời"],
  [{ t: "4", c: true }, "Kiểm tra máy chiếu, máy trình chiếu; in tài liệu phát tay", "Bộ phận CNTT, văn thư", "Trước 1 ngày", "Thiết bị, tài liệu"],
  [{ t: "5", c: true }, "Tổng hợp đề xuất thí điểm sau hội thảo", "Người trình bày, phòng/ban quản lý khoa học", "Sau … ngày", "Báo cáo tổng hợp"],
]));

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
