# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 994 / 1.200 = 82,83%. Chỉ số trong đợt chạy thử là 82,83%. |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 48 / 177 = 27,12%. Chỉ số trong đợt chạy thử là 27,12%. |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 51 / 1.200 = 4,25%. Chỉ số trong đợt chạy thử là 4,25% |
| Dùng | Nhóm tự đề xuất: Tỉ lệ chấp nhận nguyên trạng gợi ý | Số yêu cầu được xem lại có quyet_dinh_xem_lai == giu / số yêu cầu duoc_xem_lai == 1 | Không cần tính |
| An toàn | Nhóm tự đề xuất: Tỉ lệ sai lệch số tiền hoàn qua kiểm toán | Số giao dịch kiểm toán có actual_amount != expected_amount / tổng giao dịch được kiểm toán | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `request.created` | Backend tiếp nhận yêu cầu | `event_id`, `request_id`, `trace_id`, `depot`, `staff_id`, `loai`, `occurred_at` | Khi yêu cầu được tạo |
| `agent.run.started` | Agent runtime | `event_id`, `request_id`, `trace_id`, `run_id`, `attempt`, `model`, `occurred_at` | Trước mỗi lần agent chạy |
| `agent.run.completed` | Agent runtime | `event_id`, `request_id`, `trace_id`, `run_id`, `attempt`, `status`, `tokens_in`, `tokens_out`, `tool_calls`, `occurred_at` | Khi mỗi lần chạy kết thúc, kể cả lỗi |
| `review.completed` | Giao diện/nhân viên CS | `event_id`, `request_id`, `trace_id`, `staff_id`, `decision` (`giu`/`sua`/`bo`), `duration_seconds`, `occurred_at` | Khi nhân viên hoàn tất xem lại; đo thời gian thực |
| `refund.rework.created` | Hệ thống nghiệp vụ | `event_id`, `request_id`, `trace_id`, `reason`, `rework_minutes`, `occurred_at` | Khi phát sinh làm lại |
| `refund.ledger.written` | Dịch vụ sổ cái | `event_id`, `request_id`, `trace_id`, `idempotency_key`, `approved_amount`, `actual_amount`, `currency`, `occurred_at` | Sau khi ghi nhận giao dịch hoàn tiền |
| `request.handoff` | Agent/orchestrator | `event_id`, `request_id`, `trace_id`, `handoff_reason`, `assigned_staff_id`, `occurred_at` | Khi chuyển yêu cầu cho nhân viên |
| `request.closed` | Backend quản lý yêu cầu | `event_id`, `request_id`, `trace_id`, `closed_at`, `close_reason`, `occurred_at` | Khi yêu cầu được đóng |
| `request.reopened` | Backend quản lý yêu cầu | `event_id`, `request_id`, `trace_id`, `reopen_reason`, `reopened_at`, `occurred_at` | Khi yêu cầu được mở lại |
| `refund.audit.completed` | Nhân sự kiểm toán | `event_id`, `request_id`, `trace_id`, `expected_amount`, `actual_amount`, `mismatch`, `auditor_role`, `occurred_at` | Khi hoàn tất kiểm toán mẫu |
**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chỉ số chính (% đóng trong 24 giờ và không mở lại trong 7 ngày): dùng request.created, request.closed, request.reopened; tính thời gian từ occurred_at/`closed_at`, theo dõi cửa sổ 7 ngày sau khi đóng. Mẫu số là số request.created trong cohort đã đủ thời gian quan sát.
- Dùng – tỉ lệ bỏ qua gợi ý: dùng review.completed; đếm decision bằng sua hoặc bo, chia số yêu cầu có event xem lại.
- An toàn – tỉ lệ mở lại trong 7 ngày: dùng request.created, request.closed, request.reopened; nối bằng request_id và trace_id, chỉ tính cohort đã đủ 7 ngày theo dõi.
- Dùng – tỉ lệ chấp nhận nguyên trạng: dùng review.completed; đếm decision == giu, chia số yêu cầu có event xem lại.
- An toàn – tỉ lệ sai lệch số tiền hoàn: dùng refund.ledger.written và refund.audit.completed; so sánh actual_amount với expected_amount trên các giao dịch được kiểm toán. Chỉ tính được khi có dữ liệu sổ cái và kiểm toán.
- Chi phí xem lại/làm lại: dùng review.completed (duration_seconds) và refund.rework.created (rework_minutes). Đây là thời gian đo thực tế; không trộn với các cột _simulated trong trace giả lập.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Chi phí token tăng làm tăng chi phí mỗi việc thành công | Chờ kết quả B1 – kịch bản giá token gấp đôi (**simulated**) | Chi phí token/request và CPS theo tuần; cảnh báo khi vượt ngưỡng ngân sách pilot đã duyệt | Giới hạn token đầu ra, rà soát prompt/model và phân luồng yêu cầu dài | Kỹ sư AI |
| Xem lại hoặc làm lại tăng khiến lợi ích kinh tế giảm | Chờ kết quả B1/B4 (**simulated**) | Tỉ lệ `sua`/`bo`, phút xem lại thực tế, số ca làm lại và CPS theo loại yêu cầu | Tạm dừng loại yêu cầu vượt ngưỡng CPS; sửa luồng và tăng kiểm tra trước khi gửi | Trưởng vận hành CS |
| Chạy lại nhiều lần làm tăng chi phí nhưng không tăng tỷ lệ thành công tương ứng | Chờ kết quả A4/B1 giới hạn số lần chạy (**simulated**) | Số attempt/request, tỷ lệ `status == loi` theo attempt, chi phí chạy lại/request | Đặt giới hạn attempt; chuyển nhân viên khi lỗi lặp lại hoặc vượt giới hạn | Kỹ sư AI |
