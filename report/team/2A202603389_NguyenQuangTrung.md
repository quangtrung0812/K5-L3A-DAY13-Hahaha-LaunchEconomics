# Báo cáo cá nhân — NguyenQuangTrung-2A202603389

## 1. Thông tin thành viên

- Họ tên: Nguyễn Quang Trung
- MSSV: 2A202603389
- Email: 26ai.trungnq@vinuni.edu.vn
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): **Người viết code (Role 1)**

## 2. Phần việc phụ trách

- Thiết lập môi trường Python (`src/.venv`) và hoàn thiện phần tính toán **CP1 (Nhiệm vụ A: A1–A4)** và **CP2 (Nhiệm vụ B: B1–B4)** trong `src/lab13.py` (giữ nguyên khung `# TODO CP4` cho Role 2 tiếp quản sau giải lao theo quy tắc đổi người viết code).
- Cung cấp bảng kết quả sạch, có gắn nhãn `simulated` đầy đủ cho Role 2 (`bang_chi_phi.md`, `pilot_plan.yaml`), Role 3 (`chi_so.md` mục E2) và Role 4 (`ho_so_launch_v0.md`).
- Cập nhật thông tin 4 thành viên ban đầu vào `TEAM.md`.
- Chủ trì duyệt chéo **Gate 2a** (`report/team/phieu_cham.md`) lúc 17:00 cho nhóm `n + 1` và kiểm thử chạy chéo toàn repo trước khi nộp.

## 3. Đóng góp cụ thể

- **A1:** Viết ba hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong` trong `src/lab13.py`; vượt qua 3/3 phép thử đáp án biết trước (`1,20 · 1,25 · 1,25`).
- **A2:** Viết hàm `mo_hinh(runs, reqs, ...)` đọc `logix_requests.csv` với `keep_default_na=False`, tính tử số trên mọi lần chạy kể cả lần lỗi và mẫu số chỉ đếm `ket_qua == 'thanh_cong'`. Kết quả: tổng chi phí `4.373.585 đ`, `978` việc thành công, **CPS = `4.472 đ` [simulated]** (gấp `16,3×` hoá đơn token + tool/yêu cầu `274,7 đ`); chi phí cả hệ thống/yêu cầu là `5.865 đ` (`0,49×` mức `12.000 đ`) [simulated].
- **A3 & A4:** Tách chi phí theo 4 loại (`noi_dia` `2.696 đ`, `hang_nang` `8.221 đ`, `quoc_te` `22.515 đ`, `doi_tac` `10.215 đ` [simulated]), lập bảng tỉ lệ `ok` theo `attempt` (chứng minh `quoc_te` giảm từ `30,0%` → `11,4%` → `2,2%`) và cộng chi phí cố định `40 triệu đ/tháng` cho phạm vi `noi_dia + hang_nang` (`4.599 đ` ở 45.000 yc/tháng; `5.784 đ` ở 22.500 yc/tháng [simulated]).
- **B1–B4:** Chạy đủ 9 kịch bản độ nhạy (đạt kiểm tra tính tuyến tính), kịch bản cặp (`6.543 đ`, `+46,3%` [simulated]), xếp hạng top 3 yếu tố (`1. Số ca làm lại +51,8% · 2. Tỉ lệ xem lại +40,7% · 3. Lương nhân viên +23,1%`), so sánh chi phí cả hệ thống theo giới hạn 1/2/3 lần (giới hạn **2 lần** rẻ nhất cho công ty: `6.901.220 đ` [simulated]), và kịch bản xem lại 100% (`11.743 đ = 0,98×` với 9 phút làm lại; `12.415 đ = 1,03×` với trung bình thực tế `15,3 phút` [simulated]; ngưỡng hoà vốn xem lại `≤ 5,12` và `≤ 4,80 phút/lần`).
- **Duyệt chéo Gate 2a (`report/team/phieu_cham.md`):** *(Bổ sung sau phiên 17:00 với bài thật của nhóm `n + 1`)*.

## 4. Bằng chứng

- File code: `src/lab13.py` (chạy `cd src && .\.venv\Scripts\python.exe lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT` và đầy đủ bảng A1–A4, B1–B4).
- File nhóm đã cập nhật thông tin thành viên: `TEAM.md`.
- File phiếu chấm chéo Gate 2a: `report/team/phieu_cham.md` *(sẽ cập nhật lúc 17:00)*.

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity (trợ lý AI tích hợp trong IDE).
- **Dùng vào việc gì:** Phân tích cấu trúc lab để chia 4 Role chạy song song không xung đột file; gợi ý triển khai hàm `mo_hinh` và các bảng A1–A4, B1–B4 trong `src/lab13.py`; rà soát các ràng buộc của đề (`keep_default_na=False`, nhãn `simulated`, không dùng từ cấm).
- **Cách tự kiểm tra:**
  - Chạy trực tiếp `src/lab13.py` trên dữ liệu thật `src/logix_runs.csv` và `src/logix_requests.csv` (không bịa số).
  - Kiểm chứng 3/3 phép thử A1 (`1,20 · 1,25 · 1,25`), kiểm chứng tự động tính tuyến tính B1 (mức giảm khi giảm một nửa đúng bằng nửa mức tăng khi gấp đôi), và đối chiếu toàn bộ bảng A2, A3, A4, B1–B4 khớp 100% trong sai số `≤ 2%`.
  - Hiểu và tự giải thích được bản chất công thức CPS (vì sao tử số gồm mọi lần chạy lỗi còn mẫu số chỉ đếm `thanh_cong`) và sự khác biệt giữa tối ưu CPS (1 lần) với tối ưu chi phí cả hệ thống (2 lần).

## 6. Tự đánh giá

- Hoàn thành sớm toàn bộ khối tính toán CP1 + CP2 trong `src/lab13.py` với sai số 0%, bàn giao đầy đủ bảng số sạch cho Role 2, Role 3, Role 4 làm song song mà không phát sinh xung đột file, sẵn sàng cho Role 2 tiếp quản `# TODO CP4` sau khi merge và sẵn sàng cho phiên duyệt chéo Gate 2a lúc 17:00.
