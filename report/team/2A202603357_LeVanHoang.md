# Báo cáo cá nhân — LeVanHoang-2A202603357

Copy file này và đổi tên theo quy tắc `MSSV_HoTen.md`. Giữ nguyên file mẫu.

## 1. Thông tin thành viên

- Họ tên: Lê Văn Hoàng
- MSSV: `2A202603357`
- Email: `26ai.hoanglv5@vinuni.edu.vn`
- GitHub: `hoanglv2k9`
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): **Người kiểm số** (kiêm phụ trách Nhiệm vụ D — `pilot_plan.yaml` và đổi người viết code phần CP4 sau giờ giải lao)

## 2. Phần việc phụ trách

- **CP1 & CP2 (Nhiệm vụ A, B — Kiểm chứng số liệu & Điền bảng chi phí):** Tính tay và kiểm chứng độc lập trên hai file `src/logix_runs.csv` (`1.624` lần chạy) và `src/logix_requests.csv` (`1.200` yêu cầu, đọc với `keep_default_na=False`), đối chiếu chéo với Role 1 và hoàn thiện `report/team/bang_chi_phi.md` (bảng A1, A2, A3, A4, B1, B2, B3, B4).
- **CP4 (Nhiệm vụ D — Thiết kế kế hoạch Pilot):** Tính 5 câu cỡ mẫu D1 (`a–e`), lực kiểm định (`power ~0,64`) khi chấp nhận mức chênh `+6 điểm`, trả lời 5 câu tách tác động D2, tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại và hoàn thiện toàn bộ `report/team/pilot_plan.yaml`.
- **Đổi người viết code sau giải lao:** Phụ trách bổ sung khối `# TODO CP4` vào `src/lab13.py` ở Phase 2 (sau khi PR #1 của Role 1 được gộp vào `main`).

## 3. Đóng góp cụ thể

- Kiểm chứng 3 phép thử A1 với \(p = 0{,}8\): tối đa 2 lần chạy đạt **`1,20`**; chạy đến khi đúng đạt **`1,25`**; hệ số chi phí mỗi việc thành công tối đa 3 lần đạt **`1,25`**.
- Tính và kiểm tra bảng A2–A4 trong `report/team/bang_chi_phi.md`:
  - Tổng chi phí `4.373.585 đ` cho `978` việc thành công \(\rightarrow\) **`4.472 đ/việc`** (`simulated`), gấp **`16,3 lần`** (`16,28×`) hóa đơn token + tool chia đều (`274,7 đ/yêu cầu`); giờ nhân viên chiếm **`92,5%`** (`làm lại 51,8%`, `xem lại 40,7%`, `simulated`). Nếu tính cả `222` ca không thành công nhân viên làm thay (`12.000 đ/ca`), chi phí cả hệ thống là **`5.865 đ/yêu cầu = 0,49×`** (`simulated`).
  - Phân tách A3 theo `loai`: xác định phạm vi pilot chỉ gồm `noi_dia` (`2.696 đ = 0,22×`, `simulated`) và `hang_nang` (`8.221 đ = 0,69×`, `simulated`); loại `quoc_te` (`22.515 đ = 1,88×`, `simulated`, tỉ lệ `ok` giảm từ `30,0%` ở lần 1 xuống `11,4%` lần 2 và `2,2%` lần 3) và `doi_tac` (`10.215 đ = 0,85×`, điều khoản riêng).
  - Cộng chi phí cố định `40 triệu đ/tháng` ở A4 cho phạm vi `noi_dia + hang_nang` (`3.414 đ/việc` biến đổi, `simulated`): ở `45.000` yêu cầu/tháng (`33.750` việc thành công) là **`4.599 đ/việc = 0,38×`** (`simulated`); ở một nửa khối lượng (`16.875` việc) là **`5.784 đ/việc = 0,48×`** (`simulated`).
- Kiểm chứng bảng độ nhạy B1–B4:
  - Xác nhận tính đối xứng tuyến tính ở B1 (mức giảm khi giảm một nửa đúng bằng nửa mức tăng khi gấp đôi: `5,6% vs -2,8%`; `40,7% vs -20,3%`; `51,8% vs -25,9%`) và tính cộng tuyến tính ở B2 (`+5,6% + 40,7% = +46,3%` \(\rightarrow\) `6.543 đ`, `simulated`).
  - Xếp hạng 3 yếu tố nhạy nhất: **1. Số ca làm lại (`+51,8%`) · 2. Tỉ lệ xem lại (`+40,7%`) · 3. Lương nhân viên (`+23,1%`)** (`simulated`).
  - Chỉ ra ở B3: giới hạn **2 lần chạy** rẻ nhất cho toàn công ty (**`6.901.220 đ`**, `simulated`), không trùng với giới hạn có chi phí mỗi việc thành công thấp nhất (`1 lần = 4.111 đ`, `simulated`).
  - Tính B4 khi xem lại 100% trong phạm vi (`948` ca có run `ok`, `48` ca `lam_lai`, `900` việc thành công): **`11.743 đ = 0,98×`** (với `9` phút/ca làm lại, `simulated`) và **`12.414 đ / 12.415 đ = 1,03×`** (với `15,3` phút/ca trung bình dữ liệu thực tế, `simulated`), ngưỡng hòa vốn xem lại `<= 5,1 phút` (`5,12` phút) hoặc `<= 4,8 phút`.
- Thiết kế hoàn chỉnh `report/team/pilot_plan.yaml`:
  - Tính D1: a) `1.251` yêu cầu/nhóm (`1.250` nếu làm tròn \(z\)); b) `DE = 2,48`, `3.103` yêu cầu/nhóm \(\rightarrow\) `42` nhân viên/nhóm (`84 > 40`, không đủ người); c) trần hiệu dụng `20 / 0,02 = 1.000 < 1.251`; d) trần hiệu dụng `6 / 0,02 = 300`; e) ở mức chênh `+6 điểm` (`n = 859`/nhóm) với `20` nhân viên/nhóm cần **`m >= 299`** yêu cầu/nhân viên (`DE = 6,96`), chấp nhận đánh đổi `power ~0,64` ở mức `+5 điểm`.
  - Tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại: **`4,25%`** (`51/1.200`) toàn mẫu và **`3,97%`** (`39/982`) trong phạm vi `noi_dia + hang_nang`; thiết lập 3 luật dừng (An toàn, Chi phí, Sử dụng) đủ 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ`.

## 4. Bằng chứng

- File hồ sơ & code đã hoàn thiện trên nhánh `LeVanHoang-2A202603357`:
  - `src/lab13.py` (bổ sung hàm `co_mau_hai_ti_le` và `in_nhiem_vu_d` cho `# TODO CP4` — chạy thông suốt từ đầu đến cuối).
  - `report/team/bang_chi_phi.md` (đầy đủ A1–A4, B1–B4, đối chiếu khớp 100% với output `src/lab13.py`, đủ nhãn `simulated`).
  - `report/team/pilot_plan.yaml` (đọc hợp lệ bằng `yaml.safe_load`, 0 dấu `?` ngoài comment, 3 luật dừng 4 vế).
  - `report/team/2A202603357_LeVanHoang.md` (báo cáo cá nhân).

## 5. Công cụ AI đã dùng

- **Công cụ:** Trợ lý AI (Gemini / Antigravity IDE).
- **Mục đích sử dụng:** Rà soát công thức cỡ mẫu so hai tỉ lệ, hệ số thiết kế cụm (\(\text{DE} = 1 + (m-1)\cdot \text{ICC}\)), kiểm tra điều kiện biên của 9 kịch bản độ nhạy B1 và kiểm tra cú pháp YAML của `pilot_plan.yaml`.
- **Cách tự kiểm tra kết quả:**
  1. Tự tính tay lại 3 phép thử A1 (\(p=0{,}8 \Rightarrow 1{,}20; 1{,}25; 1{,}25\)), bất đẳng thức câu D1e (\(20m / (0{,}98 + 0{,}02m) \ge 859 \Rightarrow 2{,}82m \ge 841{,}82 \Rightarrow m \ge 298{,}52 \Rightarrow 299\)) và công thức điểm hòa vốn B4.
  2. Kiểm tra tính chất đối xứng của bảng B1 (kịch bản giảm một nửa luôn giảm đúng bằng \(1/2\) mức tăng của kịch bản gấp đôi) và tính cộng tuyến tính ở B2 (`+5,61% + 40,70% = +46,31%`).
  3. Chạy lệnh kiểm tra tự động `yaml.safe_load`, quét regex xác nhận không còn dấu `?` ngoài dòng chú thích và không xuất hiện các từ bị cấm theo quy định của lab.

## 6. Tự đánh giá

- Hoàn thành đầy đủ, chính xác 100% nhiệm vụ của **Người kiểm số & Thiết kế Pilot (Role 2)** theo đúng tiến độ và phân quyền nhánh Git của nhóm (không gây xung đột file).
- Nắm vững bản chất kinh tế và thống kê đằng sau từng con số (tại sao tử số cộng mọi lần chạy còn mẫu số chỉ đếm `thanh_cong`, giới hạn \(c/\text{ICC}\) khi chia theo cụm, đánh đổi giữa `CPS` thấp nhất ở 1 lần chạy và tổng chi phí hệ thống rẻ nhất ở 2 lần chạy) để sẵn sàng bảo vệ trước hội đồng Gate 2a.
