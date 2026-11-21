# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: **Hahaha**
- Lớp: **L3A**
- Repo nhóm: `K5-L3A-DAY13-Hahaha-LaunchEconomics`
- Thành viên: xem [`TEAM.md`](../../TEAM.md)

## 2. Mục tiêu và cách tiếp cận

Xây dựng bộ **hồ sơ launch v0** cho trợ lý hoàn phí LogiX-VN nhằm bảo vệ kế hoạch pilot trước hội đồng **Gate 2a** trên mẫu dữ liệu giả lập `1.200` yêu cầu (`1.624` lượt chạy agent). Nhóm chia 4 vai độc lập (Người viết code, Người kiểm số, Người gắn nhãn 1, Người gắn nhãn 2 kiêm Giữ hồ sơ), đổi người viết code sau giờ giải lao để bổ sung phần tính cỡ mẫu D1, và kiểm chứng chéo toàn bộ số liệu qua `src/lab13.py` (sai số `< 2%`).

## 3. Giải pháp

- **Nhiệm vụ A (Mô hình chi phí):** Viết 3 hàm xác suất A1 (đạt 3/3 phép thử `1,20 · 1,25 · 1,25`), hàm `mo_hinh` (A2), tách theo `loai` (A3) và cộng chi phí cố định `40 triệu đ/tháng` (A4) trong [`src/lab13.py`](../../src/lab13.py) và [`bang_chi_phi.md`](bang_chi_phi.md).
- **Nhiệm vụ B (Độ nhạy):** Chạy 9 kịch bản đơn (B1), kịch bản cặp (B2), chi phí cả hệ thống theo giới hạn 1/2/3 lần chạy (B3) và kịch bản xem lại 100% (B4) trong [`bang_chi_phi.md`](bang_chi_phi.md).
- **Nhiệm vụ C (Bảng lỗi):** Gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR và lập bảng khắc phục 5 ca đại diện trong [`bang_loi.md`](bang_loi.md).
- **Nhiệm vụ D (Kế hoạch pilot):** Tính 5 câu cỡ mẫu D1 trong `src/lab13.py`, kiểm tra 5 câu tách tác động D2 và thiết lập 3 luật dừng 4 vế (`NẾU – TRONG – THÌ – KHÔNG THÌ`) trong [`pilot_plan.yaml`](pilot_plan.yaml).
- **Nhiệm vụ E & Duyệt chéo:** Đặc tả chỉ số, `10` event có `trace_id`, rủi ro kinh tế trong [`chi_so.md`](chi_so.md); tổng hợp hồ sơ 1 trang trong [`ho_so_launch_v0.md`](ho_so_launch_v0.md); chấm chéo nhóm bạn trong [`phieu_cham.md`](phieu_cham.md).

## 4. Kết quả

- **Kinh tế (A–B):** Chi phí mỗi việc thành công toàn mẫu là **4.472 đ** (`simulated`), gấp **16,3×** hoá đơn token + tool (`274,7 đ/yc`); giờ nhân viên chiếm `92,5%` (làm lại `51,8%`, xem lại `40,7%`, `simulated`). Chi phí cả hệ thống (tính cả `222` ca nhân viên làm thay) là **5.865 đ/yc = 0,49×** so với `12.000 đ` (`simulated`). Thu hẹp phạm vi về `noi_dia` (`2.696 đ`, `0,22×`) và `hang_nang` (`8.221 đ`, `0,69×`), loại `quoc_te` (`22.515 đ`, `1,88×`) và `doi_tac` (`10.215 đ`, `0,85×`). Giới hạn **2 lần chạy** rẻ nhất toàn hệ thống (`6.901.220 đ`, `simulated`). Nếu xem lại 100%, chi phí lên **11.743 đ (`0,98×`)** với 9 phút làm lại hoặc **12.415 đ (`1,03×`)** với `15,3` phút làm lại thực tế (`simulated`).
- **Chỉ số & Pilot (D–E):** Trong đợt chạy thử: chỉ số chính **82,83%**, bỏ qua gợi ý **27,12%**, mở lại 7 ngày **4,25%**. Pilot chia theo **nhân viên** (`20` can thiệp / `20` đối chứng), chấp nhận MDE `+6` điểm (`n = 859`, `m ≥ 299` yc/người, `power ~0,64` ở mức `+5` điểm).
- **Đề xuất cuối (`ho_so_launch_v0.md`):** **Go có điều kiện** cho kế hoạch pilot `noi_dia + hang_nang` kèm 4 điều kiện cụ thể (khoá sổ cái & chốt bảng lỗi, ký chấp nhận MDE +6 điểm, đo thật thay `simulated`, lộ trình giảm xem lại theo bậc).
- **Kết quả duyệt chéo Gate 2a:**
  - *Vai trò Hội đồng (chấm nhóm `abc123` tại [`phieu_cham.md`](phieu_cham.md)):* Chấm **25/30 điểm** (`C6: 10/10 · C7: 10/10 · C8: 5/10`), quyết định **Go có điều kiện**; đã đặt câu hỏi phản biện và ghi nhận đầy đủ phần giải trình công thức hoà vốn B4 (`≤ 4,80–5,12 phút/ca`), chi phí cả hệ thống riêng phạm vi pilot (`4.131 đ/YC = 0,34×` `simulated`), cùng góp ý đồng bộ code `src/lab13.py` (A4, B4 `15,3 phút`, D1 `power 0,64`), chuẩn hoá 1 vai trò phụ trách và chốt mốc khoá mẫu 7 ngày trước `decision_date`.
  - *Vai trò Đội trình (bảo vệ hồ sơ nhóm `Hahaha`):* Hồ sơ [`ho_so_launch_v0.md`](ho_so_launch_v0.md) và [`pilot_plan.yaml`](pilot_plan.yaml) được Hội đồng đánh giá khớp bằng chứng từ `src/lab13.py`, gắn đủ nhãn `simulated`, công khai đầy đủ các số bất lợi (`xem lại 100%` lên `11.743–12.415 đ = 0,98×–1,03×` `simulated`, đánh đổi `MDE +6 điểm` với `n = 859`, `m ≥ 299`, `power ~0,64` ở mức `+5 điểm`, ngưỡng dừng an toàn dựa trên baseline mở lại `4,25%` toàn mẫu / `3,97%` phạm vi) và thống nhất thông qua đề xuất **Go có điều kiện**.

## 5. Khó khăn và cách xử lý

- **Ràng buộc 40 nhân viên không đủ mẫu cho MDE +5 điểm:** Khi chia cụm theo nhân viên (`20/nhóm`, `ICC = 0,02`), cỡ mẫu hiệu dụng tối đa `< 1.000 < 1.251`. Nhóm xử lý bằng cách nâng MDE lên `+6` điểm (`n = 859`, `m ≥ 299`), giữ đúng `20` cụm/nhóm để tách tác động và công khai đánh đổi `power ~0,64` trong hồ sơ.
- **Số phút xem lại và làm lại là dữ liệu giả lập (`_simulated`):** Nhóm gắn nhãn `simulated` nhất quán ở mọi bảng/hồ sơ và đưa yêu cầu đo thời gian thật qua `review.completed` và `refund.rework.created` thành điều kiện bắt buộc sau tuần 1.
- **Đồng bộ nhiều nhánh làm việc song song:** Nhóm phân quyền file rõ ràng theo 4 vai để tránh xung đột git khi merge về `main`.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp và bằng chứng của từng thành viên (Nguyễn Quang Trung, Lê Văn Hoàng, Nguyễn Đức Trọng, Trần Thanh Tùng) được ghi đầy đủ trong [`TEAM.md`](../../TEAM.md) và 4 file báo cáo cá nhân `report/team/<MSSV>_<HoTen>.md`.

## 7. Hạn chế và hướng cải thiện

- **Hạn chế:** Dữ liệu chi phí nhân viên hiện là giả lập (`_simulated`) và đợt chạy thử 2 tuần chưa có nhóm đối chứng nên chưa thể kết luận tác động nhân quả.
- **Hướng cải thiện:** Thay số `simulated` bằng telemetry thực ở tuần 1 pilot; theo dõi sát tỉ lệ xem lại để hạ dần dưới `50%` ở bước `0.25`; tự động hoá đối soát sổ cái hàng giờ nhằm triệt tiêu lỗi hoàn trùng.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, https://arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", https://pair.withgoogle.com
- Tài liệu `statsmodels`, lớp `NormalIndPower` (`statsmodels.stats.power`)
- Tài liệu bài lab: [`docs/du_lieu_va_cong_thuc.md`](../../docs/du_lieu_va_cong_thuc.md), [`docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md)
