# Bảng chi phí · Nhiệm vụ A và B

Số được tính kiểm chứng độc lập từ `src/logix_runs.csv` và `src/logix_requests.csv` (`keep_default_na=False`) theo công thức trong `docs/du_lieu_va_cong_thuc.md` (sẵn sàng đối chiếu chéo với output `src/lab13.py` của Role 1). Mọi con số tính từ cột `_simulated` đều có nhãn `simulated`. Mỗi câu trả lời tối đa ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả kiểm chứng |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | **1,20** (`(1 - 0,2^2) / 0,8`) |
| Số lần chạy trung bình, chạy đến khi đúng | **1,25** (`1 / 0,8`) |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | **1,25** (`1,24 / 0,992 = 1 / 0,8`) |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` (`1.624` lần chạy) | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` (`5.600` lượt gọi) | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | `attempt > 1` (`28,5%` hóa đơn) | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` (`890` phút × `2.000` đ) | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` (`1.132` phút × `2.000` đ) | simulated |
| Tổng chi phí | 4.373.585 | Tổng hợp 4 khoản trên | có phần simulated |
| Số việc thành công | 978 | `ket_qua == 'thanh_cong'` (trên `1.200` yc) | đo từ trace |
| Chi phí mỗi việc thành công | 4.472 | `4.373.585 / 978` | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | `(245.585 + 84.000) / 1.200` | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? Chi phí mỗi việc thành công là **4.472 đ** (`simulated`), gấp **16,3 lần** (`16,28×`) hóa đơn token + tool chia đều (`274,7 đ/yêu cầu`), vì giờ nhân viên chiếm `92,5%` tổng chi phí (`4.044.000 đ`). Lưu ý nếu cộng cả `222` ca không thành công nhân viên phải làm thay (`12.000 đ/ca`), chi phí cả hệ thống là **5.865 đ/yêu cầu = 0,49×** của `12.000 đ` (`simulated`), chứ không phải `0,37×`.
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? Khoản lớn nhất là **làm lại (`2.264.000 đ`, chiếm `51,8%`, `simulated`)**, tiếp theo là xem lại (`1.780.000 đ`, chiếm `40,7%`, `simulated`); tổng giờ nhân viên chiếm `92,5%`, còn token + tool chỉ `7,5%`.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% (`783/824`) | 1,11 | 2.696 đ (`simulated`) | 0,22× |
| hang_nang | 158 | 74,1% (`117/158`) | 1,47 | 8.221 đ (`simulated`) | 0,69× |
| quoc_te | 150 | 27,3% (`41/150`) | 2,32 | 22.515 đ (`simulated`) | 1,88× |
| doi_tac | 68 | 54,4% (`37/68`) | 1,88 | 10.215 đ (`simulated`) | 0,85× |

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? **`quoc_te`** không đáng chạy (`22.515 đ/việc = 1,88×` nhân viên tự làm `12.000 đ`, `simulated`, tỉ lệ thành công chỉ `27,3%`). Chạy lại tới 3 lần không giúp vì xác suất `ok` tụt rất nhanh: lần 1 đạt `30,0%`, lần 2 chỉ `11,4%`, lần 3 còn `2,2%` (lỗi lặp lại theo dữ liệu/ngoại lệ); **`doi_tac`** cũng sát ngưỡng (`0,85×`) và có điều khoản riêng nên loại khỏi pilot.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

*(Trong phạm vi `noi_dia + hang_nang` có `982` yêu cầu trong mẫu `1.200`, `900` việc thành công, chi phí biến đổi `3.072.513 đ` = **`3.414 đ/việc`** `simulated`.)*

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ (`simulated`) | 0,38× |
| Một nửa khối lượng (22.500 yc/tháng) | 16.875 | 2.370 đ | 5.784 đ (`simulated`) | 0,48× |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? Chi phí cố định `40 triệu đ/tháng` **không đổi kết luận kinh tế** ở quy mô `45.000` (`4.599 đ = 0,38×`, `simulated`) hay `22.500` yêu cầu/tháng (`5.784 đ = 0,48×`, `simulated`), nhưng tăng nhanh khi khối lượng quá nhỏ (ngưỡng hòa vốn phần cố định là khi quy mô giảm dưới ~`4.659` việc thành công/tháng tức ~`6.212` yêu cầu/tháng toàn hệ thống).

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ (`simulated`) | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ (`simulated`) | -2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ (`simulated`) | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ (`simulated`) | -20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ (`simulated`) | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ (`simulated`) | -25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ (`simulated`) | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ (`simulated`) | -5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ (`simulated`) | -8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: Chi phí mỗi việc thành công tăng lên **6.543 đ (`+46,3%`, `simulated`)**, đúng bằng tổng tác động riêng lẻ (`+5,6% + 40,7% = +46,3%`) do mô hình chi phí là tổng tuyến tính không có tương tác nhân.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. **Số ca làm lại (`+51,8% / -25,9%`, `simulated`)** · 2. **Tỉ lệ xem lại (`+40,7% / -20,3%`, `simulated`)** · 3. **Lương nhân viên (`+23,1%` khi tăng 25%, `simulated`)**.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ (`simulated`) | 319 (`881` thành công) | 7.449.781 đ (`6.208 đ/yc`, `simulated`) | 4.111 đ (`simulated`) |
| 2 lần | 4.093.220 đ (`simulated`) | 234 (`966` thành công) | **6.901.220 đ (`5.751 đ/yc`, rẻ nhất, `simulated`)** | 4.237 đ (`simulated`) |
| 3 lần | 4.373.585 đ (`simulated`) | 222 (`978` thành công) | 7.037.585 đ (`5.865 đ/yc`, `simulated`) | 4.472 đ (`simulated`) |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? **Giới hạn 2 lần chạy** rẻ nhất cho toàn công ty (**`6.901.220 đ`**, tức `5.751 đ/yêu cầu`, `simulated`), **không trùng** với giới hạn có chi phí mỗi việc thành công thấp nhất (`1 lần` = `4.111 đ`, `simulated`) vì chặn 1 lần sẽ đẩy thêm `85` ca (`319 - 234`) về cho nhân viên tự xử lý với giá `12.000 đ/ca`.

## B4 · Nếu phải xem lại tất cả

*(Phạm vi `noi_dia + hang_nang`: `982` yêu cầu, `948` ca có ít nhất 1 lần `status='ok'`, `48` ca `lam_lai`, `900` việc thành công, tổng tiền token + tool = `224.513 đ`.)*

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: Với giả định làm lại **9 phút/ca**, chi phí là **11.743 đ/việc = 0,98×** (`10.568.513 / 900`, `simulated`); nếu thay bằng trung bình dữ liệu thực tế **`15,3 phút/ca`** thì lên tới **12.414 đ/việc** (nhân với `15,3` làm tròn) / **12.415 đ/việc** (nhân chính xác `15,2973` phút) **= 1,03×** (`simulated`), tức đắt hơn nhân viên tự làm `12.000 đ`.
- Kết quả này nói gì về thứ pilot cần học được? Để hòa vốn `12.000 đ`, thời gian xem lại mỗi ca chỉ được tối đa **`<= 5,1 phút`** (`5,12` phút khi làm lại 9 phút) hoặc **`<= 4,8 phút`** (khi làm lại `15,3` phút); vì tiền xem lại chiếm ~`90%` chi phí, pilot bắt buộc phải học được **mức giảm tỉ lệ xem lại an toàn theo bậc** và rút ngắn thao tác xem lại xuống dưới 5 phút.
