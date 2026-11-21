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
| Số ca làm lại tăng gấp đôi | CPS tăng **+51,8%**, từ `4.472 đ` lên **`6.787 đ/việc`** (`simulated`) | Tỉ lệ ca phát sinh `refund.rework.created` theo tuần vượt `> 7%` (đợt chạy thử trong phạm vi là `4,9%`, tức `48/982` ca) | Thu hẹp tạm thời phạm vi về chỉ `noi_dia`, giới hạn tối đa 2 lần chạy và rà soát 20 `trace_id` làm lại gần nhất | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài (nhân viên chưa tin gợi ý) | CPS trong phạm vi `noi_dia + hang_nang` tăng lên **`11.743 đ/việc = 0,98×`** (9 phút làm lại) đến **`12.415 đ/việc = 1,03×`** (`15,3` phút làm lại thực tế, `simulated`), mất toàn bộ lợi thế so với `12.000 đ`; ngưỡng hoà vốn xem lại chỉ `≤ 4,8–5,1` phút/ca | Tỉ lệ yêu cầu có `review.completed` vẫn `> 50%` ở cuối bước `0.25` hoặc thời gian xem lại thực tế (`duration_seconds`) trung bình `> 5` phút/ca | Giảm tỉ lệ xem lại theo bậc đối với các phân nhóm có tỉ lệ `sua + bo < 15%` và tối ưu giao diện tóm tắt để xem lại dưới 5 phút | Trưởng nhóm CSKH |
| Khối lượng yêu cầu thực tế thấp hơn dự kiến hoặc giá token tăng gấp đôi | Khối lượng giảm một nửa (`22.500 yc/tháng`) làm chi phí cố định tăng gấp đôi từ `1.185 đ` lên **`2.370 đ/việc`**, đẩy CPS + cố định từ `4.599 đ (0,38×)` lên **`5.784 đ/việc (0,48×)`** (`simulated`); giá token gấp đôi làm CPS tăng **`+5,6%`** lên **`4.723 đ/việc`** (`simulated`) | Số việc thành công/tuần đạt `< 50%` kế hoạch (`< 3.900` việc/tuần) hoặc đơn giá token/request vượt dự toán `> 20%` | Không mở rộng bước rollout tiếp theo, đàm phán lại hợp đồng chi phí cố định `40 triệu đ/tháng` và giới hạn tối đa 2 lần chạy (`6.901.220 đ` toàn hệ thống, `simulated`) | Giám đốc vận hành LogiX-VN |
