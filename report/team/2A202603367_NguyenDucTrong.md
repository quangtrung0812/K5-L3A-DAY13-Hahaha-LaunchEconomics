# Báo cáo cá nhân — NguyenDucTrong-2A202603367

## 1. Thông tin thành viên

- Họ tên: Nguyễn Đức Trọng
- MSSV: `2A202603367`
- Email: `26ai.trongnd3@vinuni.edu.vn`
- GitHub: `trong1004`
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): **Người gắn nhãn 1 (Role 3)**, đồng thời phụ trách đặc tả chỉ số, danh sách event và rủi ro kinh tế cho CP5 E1–E2.

## 2. Phần việc phụ trách

- CP3 – Bảng lỗi: chuẩn hóa cách phân biệt 5 nhóm nguyên nhân gốc theo Google PAIR: Do người dùng, Hệ thống, Ngữ cảnh, Giới hạn hệ thống và Ngầm. Chuẩn bị bảng cho 20 ca, quy tắc xử lý bất đồng và phương án khắc phục cho từng nhóm.
- CP5 E1 – Chỉ số và event: xác định công thức, tính thử các chỉ số từ 1.200 yêu cầu trong logix_requests.csv; thiết kế event có trace_id để truy vết và kiểm tra chéo chỉ số.
- CP5 E2 – Rủi ro kinh tế: xác định các rủi ro chi phí cần theo dõi, tín hiệu cảnh báo, hành động kiểm soát và vai trò chịu trách nhiệm. Tác động kinh tế phải lấy từ kết quả B1/B4/A4 đã được nhóm xác nhận và ghi rõ là simulated.
## 3. Đóng góp cụ thể

CP3 – Phân loại lỗi
- Chuẩn hóa mô tả và câu hỏi phân biệt cho 5 nhóm lỗi, theo nguyên tắc gắn nhãn theo nguyên nhân gốc, không gắn theo nơi cần sửa.
- Chuẩn bị bảng 20 ca với hai cột nhãn độc lập dành cho người gắn nhãn 1 và Role 4; giữ riêng phần nhãn AI tham khảo để hỗ trợ đối chiếu, không dùng thay nhãn độc lập.
- Bổ sung khung tính đồng thuận: số ca hai người gắn cùng nhãn / 20; ngưỡng mục tiêu tối thiểu 80% (16/20). Các ca bất đồng cần có nhãn thống nhất và một câu quy tắc phân biệt.
- Đề xuất cách phát hiện đo được (event, ngưỡng, tần suất) và cách khắc phục kèm 1 vai trò phụ trách cho đủ 5 nhóm lỗi đại diện (Ca 9, Ca 7, Ca 18, Ca 4, Ca 17).
- Kết quả thực hiện: Hoàn thành gắn nhãn độc lập 20 ca với Người gắn nhãn 2 (Trần Thanh Tùng), đạt tỉ lệ đồng thuận **18/20 = 90%** ($\ge 80\%$), thống nhất quy tắc phân biệt cho 2 ca không trùng (Ca 9 và Ca 13) và hoàn thiện bảng khắc phục 5 ca trong `report/team/bang_loi.md`.
CP5 E1 – Chỉ số thử nghiệm
Tính từ toàn bộ 1.200 dòng trong logix_requests.csv, đọc với keep_default_na=False:
Nhóm	Chỉ số	Kết quả tính thử
Chính	Yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày	994/1.200 = 82,83%
Dùng	Tỷ lệ bỏ qua gợi ý trong các yêu cầu được xem lại (sua hoặc bo)	48/177 = 27,12%
An toàn	Tỷ lệ yêu cầu mở lại trong 7 ngày	51/1.200 = 4,25%
Dùng bổ sung	Tỷ lệ chấp nhận nguyên trạng gợi ý (giu) trong các yêu cầu được xem lại	129/177 = 72,88%


Các số trên được diễn đạt là “chỉ số trong đợt chạy thử”. Vì dữ liệu không có nhóm đối chứng, không kết luận trợ lý đã gây ra mức tăng hoặc cải thiện. Chỉ số sai lệch số tiền hoàn qua kiểm toán được đề xuất nhưng chưa tính được từ CSV hiện có vì thiếu expected_amount và actual_amount.

Thiết kế danh sách 10 event gồm request.created, agent.run.started, agent.run.completed, review.completed, refund.rework.created, refund.ledger.written, request.handoff, request.closed, request.reopened và refund.audit.completed. Mỗi event đều có trace_id để nối với trace; chỉ số được đối chiếu chéo đầy đủ với event tương ứng.
CP5 E2 – Rủi ro kinh tế
- Tổng hợp 3 dòng rủi ro kinh tế vào `report/team/chi_so.md` bằng số liệu đã kiểm chứng từ bảng độ nhạy (`bang_chi_phi.md`): (1) Số ca làm lại tăng gấp đôi làm CPS tăng `+51,8%` lên `6.787 đ/việc` (`simulated`); (2) Kịch bản phải xem lại 100% kéo dài đẩy CPS phạm vi lên `11.743 đ (0,98×)` với 9 phút làm lại và `12.415 đ (1,03×)` với `15,3` phút làm lại thực tế (`simulated`), ngưỡng hoà vốn xem lại `≤ 4,8–5,1` phút/ca; (3) Khối lượng giảm một nửa làm chi phí cố định tăng lên `2.370 đ/việc` (`5.784 đ = 0,48×`, `simulated`) và giá token gấp đôi làm CPS tăng `+5,6%` lên `4.723 đ` (`simulated`).
- Gắn từng rủi ro với dấu hiệu theo dõi đo được, hành động kiểm soát cụ thể và 1 vai trò phụ trách (PM trợ lý hoàn phí, Trưởng nhóm CSKH, Giám đốc vận hành LogiX-VN).

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

- Đã hoàn thành đầy đủ nhiệm vụ của Người gắn nhãn 1 (Role 3): gắn nhãn độc lập 20 ca lỗi CP3 đạt đồng thuận `18/20 = 90%`, hoàn thiện bảng khắc phục 5 ca đại diện trong `report/team/bang_loi.md`; tính chính xác 3 chỉ số E1, thiết kế 10 event có `trace_id` kèm kiểm tra chéo và hoàn thiện bảng rủi ro kinh tế E2 có đầy đủ con số từ bảng độ nhạy (nhãn `simulated`) trong `report/team/chi_so.md`.