# Team

## Thông tin nhóm

- Tên nhóm: Hahaha
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-Hahaha-LaunchEconomics`
- URL repo, nhánh nộp, commit chốt: https://github.com/quangtrung0812/K5-L3A-DAY13-Hahaha-LaunchEconomics · nhánh `main` · commit chốt: *(cập nhật trước khi push cuối buổi)*

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Quang Trung | 2A202603389 | 26ai.trungnq@vinuni.edu.vn | `quangtrung0812` | Người viết code (Role 1) |
|   2 | Lê Văn Hoàng | 2A202603357 | 26ai.hoanglv5@vinuni.edu.vn | `hoanglv2k9` | Người kiểm số (Role 2) |
|   3 | Nguyễn Đức Trọng | 2A202603367 | 26ai.trongnd3@vinuni.edu.vn | `trong1004` | Người gắn nhãn 1 (Role 3) |
|   4 | Trần Thanh Tùng | 2A202603418 | 26ai.tungtt@vinuni.edu.vn | `tungtran306` | Người gắn nhãn 2, kiêm giữ hồ sơ (Role 4) |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## NguyenQuangTrung-2A202603389

### Phần việc phụ trách

- Role 1 — Người viết code: xây dựng và chạy mô hình chi phí (CP1: A1–A4) và phân tích độ nhạy (CP2: B1–B4) trong `src/lab13.py`; chủ trì duyệt chéo Gate 2a (`report/team/phieu_cham.md`) và kiểm thử chạy chéo toàn repo cuối buổi.

### Đóng góp cụ thể

- Hoàn thiện 3 hàm A1 đạt 3/3 phép thử đáp án biết trước (`1,20 · 1,25 · 1,25`), hàm `mo_hinh` (A2), tách theo `loai` và tỉ lệ `ok` theo `attempt` (A3), chi phí cố định 40 triệu đ/tháng ở 2 mức khối lượng (A4).
- Hoàn thiện phân tích độ nhạy 9 kịch bản đơn (B1), kịch bản cặp và xếp hạng top 3 yếu tố (B2), chi phí cả hệ thống theo giới hạn 1/2/3 lần chạy (B3), và kịch bản xem lại 100% kèm độ nhạy phút làm lại thực tế & ngưỡng hoà vốn (B4).
- Báo cáo cá nhân: `report/team/2A202603389_NguyenQuangTrung.md`.

### Bằng chứng

- `src/lab13.py` (chạy đạt `Ba phép thử đáp án biết trước: ĐẠT` và xuất đủ bảng A1–A4, B1–B4)
- `report/team/2A202603389_NguyenQuangTrung.md`
- `report/team/phieu_cham.md` *(cập nhật sau phiên duyệt chéo 17:00)*

## LeVanHoang-2A202603357

### Phần việc phụ trách

- Role 2 — Người kiểm số & Thiết kế Pilot: kiểm chứng số liệu A–B (`report/team/bang_chi_phi.md`), thiết kế kế hoạch pilot (`report/team/pilot_plan.yaml`) và đổi vai viết code bổ sung `# TODO CP4` (D1) vào `src/lab13.py`.

### Đóng góp cụ thể

- *(Cập nhật khi hoàn thành PR Role 2)*

### Bằng chứng

- `report/team/bang_chi_phi.md`, `report/team/pilot_plan.yaml`, `src/lab13.py` (`# TODO CP4`), `report/team/2A202603357_LeVanHoang.md`

## NguyenDucTrong-2A202603367

### Phần việc phụ trách

- Role 3 — Người gắn nhãn 1 & Đặc tả Chỉ số/Event: tính thử chỉ số E1, thiết kế danh sách event có `trace_id` và rủi ro kinh tế E2 (`report/team/chi_so.md`); gắn nhãn độc lập 20 ca lỗi CP3 và tổng hợp `report/team/bang_loi.md`; theo dõi điều kiện "Xong khi".

### Đóng góp cụ thể

- *(Cập nhật khi hoàn thành PR Role 3)*

### Bằng chứng

- `report/team/chi_so.md`, `report/team/bang_loi.md`, `report/team/2A202603367_NguyenDucTrong.md`

## TranThanhTung-2A202603418

### Phần việc phụ trách

- Role 4 — Người gắn nhãn 2, kiêm giữ hồ sơ Launch v0 & Đóng gói: gắn nhãn độc lập 20 ca lỗi CP3; duy trì và chốt `report/team/ho_so_launch_v0.md` trước 17:00; tổng hợp `report/team/group_report.md`, `TEAM.md` và kiểm tra checklist `SUBMISSION.md`.

### Đóng góp cụ thể

- *(Cập nhật khi hoàn thành PR Role 4)*

### Bằng chứng

- `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `TEAM.md`, `report/team/2A202603418_TranThanhTung.md`
