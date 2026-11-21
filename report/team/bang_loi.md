# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: **Nguyễn Đức Trọng** · Người gắn nhãn 2: **Trần Thanh Tùng** (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Hệ thống | Không | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Hệ thống | Không | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 18 / 20 = **90%** *(đạt yêu cầu $\ge 80\%$)*

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu.

- **Ca 9 (Do người dùng):** Gốc lỗi là khách nhập sai mã (mã sàn TMĐT thay vì mã vận đơn); việc trợ lý chưa gợi ý cách nhập nằm ở hướng khắc phục, không đổi nguyên nhân gốc.
- **Ca 13 (Giới hạn hệ thống):** Yêu cầu nằm ngoài phạm vi sản phẩm của trợ lý (bảo hiểm của đối tác) thì luôn gắn là Giới hạn hệ thống, kể cả khi trợ lý phản hồi chưa rõ ràng.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` gắn `trace_id`; cảnh báo khi `> 2%` số yêu cầu/ngày | Tự nhận diện định dạng mã sàn TMĐT để tra sang mã vận đơn; nếu không tra được thì hiển thị hướng dẫn kèm ảnh mẫu | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát tự động mỗi giờ giữa tin nhắn "đã hoàn" và event `refund.ledger.written` có cùng `trace_id`; ngưỡng `0` ca lệch | Chỉ gửi thông báo "đã hoàn" khi dịch vụ sổ cái trả về `ok` với `idempotency_key`; gặp lỗi `503` sau tối đa 2 lần thử thì báo "đang xử lý" và chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ `request.reopened` với lý do "sai tiền" nhưng kiểm tra lại thấy số tiền hoàn đúng chính sách; theo dõi hằng tuần, ngưỡng `> 1%` | Bắt buộc mẫu tin nhắn hoàn tiền ghi rõ công thức tính (ví dụ: `30.000 đ × 50% = 15.000 đ`) kèm điều khoản áp dụng | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `request.handoff` có `handoff_reason = thieu_du_lieu` phân theo `loai`; thống kê hằng tuần | Giữ cơ chế chuyển nhân viên kèm tóm tắt ngữ cảnh; loại `quoc_te` khỏi phạm vi pilot và định tuyến thẳng sang nhân viên | PM trợ lý hoàn phí |
| 17 | Ngầm | Event `refund.audit.completed` kiểm toán mẫu `100` đơn/tuần so với bảng giá hiện hành; ngưỡng cảnh báo `> 1%` đơn sai lệch | Xoá bộ nhớ đệm ngay khi cập nhật bảng giá mới và ghi `pricing_version` vào mọi `trace_id` để đối chiếu | Kế toán trưởng |
