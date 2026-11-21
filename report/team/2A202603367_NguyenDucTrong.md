# Báo cáo cá nhân — HoVaTen-MSSV

Copy file này và đổi tên theo quy tắc `MSSV_HoTen.md`. Giữ nguyên file mẫu.

Ví dụ: `20241234_NguyenVanAn.md`.

## 1. Thông tin thành viên

- Họ tên:
- MSSV:
- Email:
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người gắn nhãn 1, đồng thời phụ trách đặc tả chỉ số và event cho CP5 E1–E2.

## 2. Phần việc phụ trách

- CP3 – Bảng lỗi: chuẩn hóa cách phân biệt 5 nhóm nguyên nhân gốc theo Google PAIR: Do người dùng, Hệ thống, Ngữ cảnh, Giới hạn hệ thống và Ngầm. Chuẩn bị bảng cho 20 ca, quy tắc xử lý bất đồng và phương án khắc phục cho từng nhóm.
- CP5 E1 – Chỉ số và event: xác định công thức, tính thử các chỉ số từ 1.200 yêu cầu trong logix_requests.csv; thiết kế event có trace_id để truy vết và kiểm tra chéo chỉ số.
- CP5 E2 – Rủi ro kinh tế: xác định các rủi ro chi phí cần theo dõi, tín hiệu cảnh báo, hành động kiểm soát và vai trò chịu trách nhiệm. Tác động kinh tế phải lấy từ kết quả B1/B4/A4 đã được nhóm xác nhận và ghi rõ là simulated.
## 3. Đóng góp cụ thể

CP3 – Phân loại lỗi
- Chuẩn hóa mô tả và câu hỏi phân biệt cho 5 nhóm lỗi, theo nguyên tắc gắn nhãn theo nguyên nhân gốc, không gắn theo nơi cần sửa.
- Chuẩn bị bảng 20 ca với hai cột nhãn độc lập dành cho người gắn nhãn 1 và Role 4; giữ riêng phần nhãn AI tham khảo để hỗ trợ đối chiếu, không dùng thay nhãn độc lập.
- Bổ sung khung tính đồng thuận: số ca hai người gắn cùng nhãn / 20; ngưỡng mục tiêu tối thiểu 80% (16/20). Các ca bất đồng cần có nhãn thống nhất và một câu quy tắc phân biệt.
- Đề xuất cách phát hiện và khắc phục cho đủ 5 nhóm. Ví dụ: cảnh báo sai lệch số tiền giữa agent.run.completed và refund.ledger.written; kiểm tra yêu cầu ngoài phạm vi chưa được request.handoff; kiểm toán sai lệch hoàn tiền qua refund.audit.completed.
- Trạng thái: đã chuẩn bị khung và nhãn AI tham khảo; chưa thể kết luận tỷ lệ đồng thuận hoặc chốt 5 ca đại diện trước khi có đủ hai bộ nhãn độc lập và kết quả thảo luận.
CP5 E1 – Chỉ số thử nghiệm
Tính từ toàn bộ 1.200 dòng trong logix_requests.csv, đọc với keep_default_na=False:
Nhóm	Chỉ số	Kết quả tính thử
Chính	Yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày	994/1.200 = 82,83%
Dùng	Tỷ lệ bỏ qua gợi ý trong các yêu cầu được xem lại (sua hoặc bo)	48/177 = 27,12%
An toàn	Tỷ lệ yêu cầu mở lại trong 7 ngày	51/1.200 = 4,25%
Dùng bổ sung	Tỷ lệ chấp nhận nguyên trạng gợi ý (giu) trong các yêu cầu được xem lại	129/177 = 72,88%


Các số trên được diễn đạt là “chỉ số trong đợt chạy thử”. Vì dữ liệu không có nhóm đối chứng, không kết luận trợ lý đã gây ra mức tăng hoặc cải thiện. Chỉ số sai lệch số tiền hoàn qua kiểm toán được đề xuất nhưng chưa tính được từ CSV hiện có vì thiếu expected_amount và actual_amount.

Thiết kế danh sách event gồm request.created, agent.run.started, agent.run.completed, review.completed, refund.rework.created, refund.ledger.written, request.handoff, request.closed, request.reopened và refund.audit.completed. Mỗi event đều có trace_id để nối với trace; chỉ số được đối chiếu với event tương ứng.
CP5 E2 – Rủi ro kinh tế
- Xác định ba nhóm rủi ro cần theo dõi: giá token tăng; thời gian xem lại/làm lại tăng; chạy lại nhiều lần nhưng không cải thiện tỷ lệ thành công tương ứng.
- Gắn từng rủi ro với tín hiệu đo được như chi phí token/request, CPS, tỷ lệ sua/`bo`, phút xem lại, số lần attempt và tỷ lệ lỗi theo attempt.
- Đề xuất hành động kiểm soát và vai trò phụ trách: Kỹ sư AI, Trưởng vận hành CS. Tác động định lượng từ B1/B4/A4 cần lấy từ kết quả đã xác nhận của thành viên phụ trách; không tự suy diễn số liệu.

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

- bang_loi.md: định nghĩa 5 nhóm lỗi, bảng 20 ca, khu vực lưu hai bộ nhãn độc lập, phần nhãn AI tham khảo, khung tính agreement và bảng khắc phục.
- chi_so.md: công thức và kết quả tính thử E1, danh sách event, cách kiểm tra chéo chỉ số và khung rủi ro E2.
- logix_requests.csv: nguồn dữ liệu 1.200 yêu cầu dùng để tính E1. Kiểm tra lại cho kết quả: 994 yêu cầu đạt điều kiện chỉ số chính; 177 yêu cầu được xem lại, gồm 129 giu, 41 sua, 7 bo; có 51 yêu cầu mở lại trong 7 ngày.

## 5. Công cụ AI đã dùng

Công cụ nào, dùng vào việc gì, bạn tự kiểm tra kết quả ra sao.

- ChatGPT: hỗ trợ rà soát cấu trúc báo cáo, diễn giải định nghĩa 5 nhóm lỗi, đề xuất nhãn tham khảo cho 20 ca, xây dựng công thức chỉ số, thiết kế event và rà soát cách trình bày rủi ro.
- Cách tự kiểm tra: đối chiếu định nghĩa và yêu cầu với tài liệu Lab 13; kiểm tra lại các phép đếm trên toàn bộ logix_requests.csv bằng keep_default_na=False; kiểm tra tổng số yêu cầu là 1.200 và đối chiếu các nhóm giu/`sua`/`bo` với mẫu số 177.
- Giới hạn sử dụng AI: nhãn AI chỉ là tài liệu tham khảo, không thay thế nhãn độc lập của người gắn nhãn 1 và Role 4. Không dùng AI để tạo kết quả agreement, nhãn thống nhất hoặc số liệu kiểm toán khi chưa có dữ liệu tương ứng.

## 6. Tự đánh giá

- Đã hoàn thành: chuẩn hóa khung phân loại lỗi; chuẩn bị bảng 20 ca và nhãn AI tham khảo; tính và kiểm tra lại các chỉ số E1; thiết kế event có trace_id; xác định các rủi ro kinh tế và tín hiệu giám sát cần có.
- Tự đánh giá chung: phần đặc tả chỉ số và khung hồ sơ lỗi đã có cơ sở kiểm tra được. CP3 chưa thể xem là hoàn tất cho đến khi có hai bộ nhãn độc lập và kết quả agreement; E2 cần cập nhật số liệu kinh tế đã được nhóm xác nhận.