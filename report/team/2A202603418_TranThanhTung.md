# Báo cáo cá nhân — TranThanhTung-2A202603418

## 1. Thông tin thành viên

- Họ tên: Trần Thanh Tùng
- MSSV: `2A202603418`
- Email: `26ai.tungtt@vinuni.edu.vn`
- Vai trong nhóm: **Người gắn nhãn 2, kiêm giữ hồ sơ (Role 4)**

## 2. Phần việc phụ trách

- Thực hiện gắn nhãn độc lập 20 ca lỗi CP3 theo 5 loại Google PAIR và phối hợp đối chiếu đồng thuận với Người gắn nhãn 1 (Role 3).
- Duy trì cuốn chiếu và chốt hồ sơ 1 trang `report/team/ho_so_launch_v0.md` (CP5 E3) đúng hạn trước phiên duyệt chéo Gate 2a (17:00).
- Tổng hợp báo cáo nhóm `report/team/group_report.md`, cập nhật `TEAM.md` và chạy audit toàn bộ checklist nộp bài theo `SUBMISSION.md`.

## 3. Đóng góp cụ thể

- Trích xuất nguyên văn 20 ca lỗi từ `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` để gắn nhãn độc lập theo nguyên nhân gốc.
- Tổng hợp số liệu đã kiểm chứng từ Role 1, Role 2, Role 3 (`bang_chi_phi.md`, `pilot_plan.yaml`, `chi_so.md`, `bang_loi.md`) vào `report/team/ho_so_launch_v0.md` đủ 7 mục, đảm bảo 100% số từ cột `_simulated` có nhãn `simulated`, cột trạng thái chỉ dùng 3 giá trị quy định, người phụ trách là 1 vai trò cụ thể.
- Xây dựng đề xuất **Go có điều kiện** cho kế hoạch pilot `noi_dia + hang_nang`, nêu thẳng các điểm bất lợi (kịch bản xem lại 100% lên `0,98×–1,03×` `simulated`, `power ~0,64` ở mức `+5` điểm, tỉ lệ mở lại `4,25%`, lỗi sổ cái/hoàn trùng) kèm 4 điều kiện có vai trò phụ trách và ngày kiểm tra.
- Hoàn thiện `report/team/group_report.md` ($\le 2$ trang), cập nhật phần đóng góp trong `TEAM.md` và chạy bộ lệnh kiểm tra chất lượng toàn repo.

## 4. Bằng chứng

- Nhánh làm việc: `tranthanhtung`
- Các file trực tiếp hoàn thiện:
  - `report/team/ho_so_launch_v0.md`
  - `report/team/group_report.md`
  - `TEAM.md`
  - `report/team/2A202603418_TranThanhTung.md`

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity (trợ lý AI tích hợp trong IDE).
- **Mục đích sử dụng:** Tóm tắt yêu cầu đề bài và rubric; trích xuất nguyên văn 20 ca lỗi từ file `.docx` (không sinh nhãn thay); hỗ trợ soạn cấu trúc và rà soát tính nhất quán số liệu giữa `bang_chi_phi.md`, `pilot_plan.yaml`, `chi_so.md` với `ho_so_launch_v0.md` và `group_report.md`; chạy lệnh tự động kiểm tra checklist `SUBMISSION.md`.
- **Cách tự kiểm tra:** Đối chiếu trực tiếp từng con số trong `ho_so_launch_v0.md` với output của `src/lab13.py` và các file của Role 1–3; chạy lệnh kiểm tra từ cấm, kiểm tra `yaml.safe_load` trên `pilot_plan.yaml`, và rà soát thủ công từng điều kiện của đề xuất cuối.

## 6. Tự đánh giá

- Hoàn thành đúng phạm vi file của Role 4, không gây xung đột git với các thành viên khác.
- Hồ sơ `ho_so_launch_v0.md` súc tích đúng 1 trang, minh bạch mọi con số bất lợi và nhãn `simulated`, sẵn sàng bảo vệ trước hội đồng Gate 2a.
- Điểm cần theo sát tiếp: phối hợp Role 3 chốt nốt bộ nhãn Người 2 + 5 ca khắc phục trong `bang_loi.md` và cập nhật kết quả duyệt chéo vào `group_report.md` sau phiên 17:00.
