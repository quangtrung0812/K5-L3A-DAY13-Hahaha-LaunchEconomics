"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26                    # đồng cho 1.000 token đầu vào
GIA_RA = 130                    # đồng cho 1.000 token đầu ra
GIA_TOOL = 15                   # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000               # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000                # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CHI_PHI_CO_DINH_THANG = 40_000_000  # đồng / tháng chi phí cố định của trợ lý
KHOI_LUONG_THANG = 45_000       # yêu cầu / tháng quy mô đầy đủ


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1.0 / p if k is None else (1.0 - (1.0 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1.0 - (1.0 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc,
    khong_thanh_cong, ca_he_thong, ca_he_thong_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × luong_phut. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000.0 * gia_vao + runs['tokens_out'] / 1000.0 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    chay_lai = (tien_token + tien_tool)[runs['attempt'] > 1].sum()
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    khong_thanh_cong = int(len(reqs) - thanh_cong)
    cps = tong / thanh_cong
    hoa_don_moi_yc = (tien_token.sum() + tien_tool.sum()) / len(reqs)
    ca_he_thong = tong + khong_thanh_cong * BASELINE
    ca_he_thong_moi_yc = ca_he_thong / len(reqs)

    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=chay_lai,
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        khong_thanh_cong=khong_thanh_cong,
        cps=cps,
        hoa_don_moi_yc=hoa_don_moi_yc,
        ca_he_thong=ca_he_thong,
        ca_he_thong_moi_yc=ca_he_thong_moi_yc,
    )


def in_nhiem_vu_a(runs, reqs):
    """In đầy đủ kết quả CP1: A1, A2, A3, A4."""
    print('\n=== A1 · Ba phép thử đáp án biết trước (p = 0,8) ===')
    print(f'  Số lần chạy trung bình, tối đa 2 lần       : {so_lan_chay_ky_vong(0.8, 2):.2f}')
    print(f'  Số lần chạy trung bình, chạy đến khi đúng  : {so_lan_chay_ky_vong(0.8):.2f}')
    print(f'  Hệ số chi phí mỗi việc thành công, tối đa 3: {he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f}')

    kq = mo_hinh(runs, reqs)
    phut_xl = reqs['phut_xem_lai_simulated'].sum()
    phut_ll = reqs['phut_lam_lai_simulated'].sum()
    so_tool = int(runs['tool_calls'].sum())
    so_chuyen_nv = int((reqs['ket_qua'] == 'chuyen_nhan_vien').sum())
    print('\n=== A2 · Mô hình chi phí từ trace (1.200 yêu cầu, 1.624 lần chạy) ===')
    print(f'  Token (mọi lần chạy)                  : {kq["token"]:>12,.0f} đ  [đo từ trace]')
    print(f'  Tool ({so_tool:,} lần gọi)                 : {kq["tool"]:>12,.0f} đ  [đo từ trace]')
    print(f'  Trong đó, lần chạy thứ 2 và 3         : {kq["chay_lai"]:>12,.0f} đ  [đo từ trace]')
    print(f'  Xem lại ({phut_xl:,.0f} phút)                   : {kq["xem_lai"]:>12,.0f} đ  [simulated]')
    print(f'  Làm lại ({phut_ll:,.0f} phút)                 : {kq["lam_lai"]:>12,.0f} đ  [simulated]')
    print(f'  Tổng chi phí                          : {kq["tong"]:>12,.0f} đ  [có phần simulated]')
    print(f'  Số việc thành công                    : {kq["thanh_cong"]:>12,d}')
    print(f'  Chi phí mỗi việc thành công (CPS)     : {kq["cps"]:>12,.0f} đ  [simulated]')
    print(f'  Hoá đơn token + tool / số yêu cầu     : {kq["hoa_don_moi_yc"]:>12,.1f} đ  [đo từ trace]')
    print(f'  Gấp bao nhiêu lần hoá đơn/yêu cầu     : {kq["cps"] / kq["hoa_don_moi_yc"]:>12.1f}x  [simulated]')
    print(f'  Tỉ trọng lớn nhất (Làm lại)           : {kq["lam_lai"] / kq["tong"] * 100:>11.1f}%  [simulated]')
    print(f'  Tỉ trọng Xem lại                      : {kq["xem_lai"] / kq["tong"] * 100:>11.1f}%  [simulated]')
    print(f'  Tổng giờ nhân viên (Xem + Làm lại)    : {(kq["xem_lai"] + kq["lam_lai"]) / kq["tong"] * 100:>11.1f}%  [simulated]')
    print(f'  Chi phí cả hệ thống/yêu cầu (cộng {kq["khong_thanh_cong"]} ca không TC, gồm {so_chuyen_nv} chuyển NV): '
          f'{kq["ca_he_thong_moi_yc"]:,.0f} đ = {kq["ca_he_thong_moi_yc"] / BASELINE:.2f}x của 12.000 đ [simulated]')

    print('\n=== A3 · Tách theo loại yêu cầu ===')
    print(f'  {"Loại":<12s} {"Số YC":>6s} {"Tỉ lệ TC":>10s} {"Lần chạy/YC":>12s} {"CPS [sim]":>12s} {"So 12.000đ":>11s}')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub = reqs[reqs['loai'] == loai]
        r = mo_hinh(runs, sub)
        ti_le = r['thanh_cong'] / len(sub) * 100
        lan_tb = sub['so_lan_chay'].mean()
        print(f'  {loai:<12s} {len(sub):>6d} {ti_le:>9.1f}% {lan_tb:>12.2f} {r["cps"]:>11,.0f}đ {r["cps"] / BASELINE:>10.2f}x')

    print('\n  Tỉ lệ status == "ok" theo (loại, lần chạy attempt):')
    merged = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    merged['is_ok'] = (merged['status'] == 'ok').astype(float)
    piv = merged.pivot_table(index='loai', columns='attempt', values='is_ok', aggfunc='mean') * 100
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        vals = '  '.join(f'Lần {c}: {piv.loc[loai, c]:5.1f}%' for c in piv.columns)
        print(f'    {loai:<10s} -> {vals}')

    print('\n=== A4 · Chi phí cố định 40 triệu đ/tháng (phạm vi noi_dia + hang_nang) ===')
    pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pv = mo_hinh(runs, pv)
    ti_le_pv_tc = kq_pv['thanh_cong'] / len(reqs)
    print(f'  Trong phạm vi mẫu: {kq_pv["thanh_cong"]}/{len(reqs)} việc thành công; '
          f'tổng {kq_pv["tong"]:,.0f} đ; CPS chưa cố định = {kq_pv["cps"]:,.0f} đ [simulated]')
    print(f'  {"Khối lượng":<22s} {"Việc TC/tháng":>14s} {"Cố định/việc":>13s} {"CPS+CĐ [sim]":>13s} {"So 12.000đ":>11s}')
    for nhan, kl in [('45.000 yêu cầu/tháng', KHOI_LUONG_THANG), ('22.500 (một nửa)', KHOI_LUONG_THANG // 2)]:
        viec_thang = kl * ti_le_pv_tc
        cd_viec = CHI_PHI_CO_DINH_THANG / viec_thang
        tong_cps = kq_pv['cps'] + cd_viec
        print(f'  {nhan:<22s} {viec_thang:>14,.0f} {cd_viec:>12,.0f}đ {tong_cps:>12,.0f}đ {tong_cps / BASELINE:>10.2f}x')


def in_nhiem_vu_b(runs, reqs):
    """In đầy đủ kết quả CP2: B1, B2, B3, B4."""
    goc = mo_hinh(runs, reqs)['cps']
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi': dict(he_so_xem_lai=2.0),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi': dict(he_so_lam_lai=2.0),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%': dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần': dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần': dict(max_lan_chay=1),
    }

    print('\n=== B1 · Bảng độ nhạy (đổi từng yếu tố) ===')
    print(f'  {"Kịch bản":<28s} {"CPS [sim]":>12s} {"Thay đổi":>10s}')
    print(f'  {"Gốc (A2)":<28s} {goc:>11,.0f}đ {"0.0%":>10s}')
    delta_map = {}
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        pct = (cps / goc - 1.0) * 100
        delta_map[ten] = pct
        print(f'  {ten:<28s} {cps:>11,.0f}đ {pct:>+9.1f}%')

    # Tự kiểm tra tuyến tính: giảm nửa = -0.5 × tăng gấp đôi
    for k_up, k_dn in [
        ('Giá token gấp đôi', 'Giá token giảm một nửa'),
        ('Tỉ lệ xem lại gấp đôi', 'Tỉ lệ xem lại giảm một nửa'),
        ('Số ca làm lại gấp đôi', 'Số ca làm lại giảm một nửa'),
    ]:
        assert abs(delta_map[k_dn] + 0.5 * delta_map[k_up]) < 1e-6, f'Sai tuyến tính ở {k_up}'
    print('  Kiểm tra tính tuyến tính (giảm nửa = 1/2 mức tăng gấp đôi): ĐẠT')

    print('\n=== B2 · Đổi một cặp & Xếp hạng top 3 ===')
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)['cps']
    pct_cap = (cps_cap / goc - 1.0) * 100
    print(f'  Giá token ×2 + Xem lại ×2 : {cps_cap:,.0f} đ ({pct_cap:+.1f}%) [simulated]')
    top3 = [
        ('Số ca làm lại', delta_map['Số ca làm lại gấp đôi']),
        ('Tỉ lệ xem lại', delta_map['Tỉ lệ xem lại gấp đôi']),
        ('Lương nhân viên (+25%)', delta_map['Lương nhân viên tăng 25%']),
    ]
    top3.sort(key=lambda x: abs(x[1]), reverse=True)
    print('  Xếp hạng 3 yếu tố mạnh nhất: ' + ' · '.join(f'{i+1}. {n} ({v:+.1f}%)' for i, (n, v) in enumerate(top3)))

    print('\n=== B3 · Giới hạn chạy lại: Chi phí cả hệ thống vs CPS ===')
    print(f'  {"Giới hạn":<10s} {"Tổng trợ lý [sim]":>18s} {"Không TC":>10s} {"Cả hệ thống [sim]":>18s} {"CPS [sim]":>12s}')
    for cap in [1, 2, 3]:
        r = mo_hinh(runs, reqs, max_lan_chay=cap)
        print(f'  {f"{cap} lần":<10s} {r["tong"]:>17,.0f}đ {r["khong_thanh_cong"]:>10d} '
              f'{r["ca_he_thong"]:>17,.0f}đ {r["cps"]:>11,.0f}đ')

    print('\n=== B4 · Kịch bản xem lại 100% (phạm vi noi_dia + hang_nang) ===')
    pv_reqs = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    pv_runs = runs[runs['request_id'].isin(pv_reqs['request_id'])]
    co_ok = pv_runs.loc[pv_runs['status'] == 'ok', 'request_id'].nunique()
    so_lam_lai = int((pv_reqs['ket_qua'] == 'lam_lai').sum())
    so_tc = int((pv_reqs['ket_qua'] == 'thanh_cong').sum())
    token_tool = (pv_runs['tokens_in'] / 1000.0 * GIA_VAO
                  + pv_runs['tokens_out'] / 1000.0 * GIA_RA
                  + pv_runs['tool_calls'] * GIA_TOOL).sum()
    xem_lai_100 = co_ok * 5.0 * LUONG_PHUT
    phut_ll_tb_all = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    phut_ll_med_all = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].median()

    print(f'  Phạm vi noi_dia + hang_nang: {len(pv_reqs)} YC · {co_ok} YC có ≥1 lần ok · '
          f'{so_lam_lai} ca làm lại · {so_tc} việc thành công')
    print(f'  Token + Tool = {token_tool:,.0f} đ [đo từ trace] · Xem lại 100% (5 phút/YC) = {xem_lai_100:,.0f} đ [simulated]')
    print(f'  Phút làm lại thực tế trong dữ liệu (toàn bộ ca lam_lai): TB = {phut_ll_tb_all:.2f} phút, trung vị = {phut_ll_med_all:.1f} phút [simulated]')
    for nhan, phut_ll in [('Theo đề (9 phút/ca làm lại)', 9.0),
                          (f'Theo dữ liệu ({phut_ll_tb_all:.1f} phút/ca làm lại)', phut_ll_tb_all)]:
        lam_lai_cp = so_lam_lai * phut_ll * LUONG_PHUT
        tong_100 = token_tool + xem_lai_100 + lam_lai_cp
        cps_100 = tong_100 / so_tc
        hoa_von_phut = (BASELINE * so_tc - token_tool - lam_lai_cp) / (co_ok * LUONG_PHUT)
        print(f'  - {nhan}: Làm lại = {lam_lai_cp:,.0f} đ · Tổng = {tong_100:,.0f} đ · '
              f'CPS = {cps_100:,.0f} đ ({cps_100 / BASELINE:.2f}x) [simulated] · '
              f'Hoà vốn xem lại <= {hoa_von_phut:.2f} phút/lần')


# ---------- Nhiệm vụ D1 · Cỡ mẫu kế hoạch Pilot (CP4 — Role 2) ----------
def co_mau_hai_ti_le(p1, p2, alpha=0.05, power=0.80):
    """Cỡ mẫu mỗi nhóm khi so sánh hai tỉ lệ độc lập (công thức chuẩn NormalDist)."""
    from statistics import NormalDist
    nd = NormalDist()
    za = nd.inv_cdf(1.0 - alpha / 2.0)
    zb = nd.inv_cdf(power)
    pb = (p1 + p2) / 2.0
    tu_so = za * math.sqrt(2.0 * pb * (1.0 - pb)) + zb * math.sqrt(p1 * (1.0 - p1) + p2 * (1.0 - p2))
    return math.ceil((tu_so ** 2) / ((p2 - p1) ** 2))


def in_nhiem_vu_d(reqs):
    """In kết quả 5 câu cỡ mẫu D1 (a-e), power ở mức 5 điểm khi n=859, và tỉ lệ mở lại 7 ngày."""
    from statistics import NormalDist
    p1 = 0.70
    p2_5pt = 0.75
    p2_6pt = 0.76
    alpha = 0.05
    power = 0.80
    icc = 0.02

    # a) Chia theo yêu cầu (+5 điểm)
    n_a = co_mau_hai_ti_le(p1, p2_5pt, alpha=alpha, power=power)

    # b) Chia theo nhân viên, m = 75
    m_b = 75
    de_b = 1.0 + (m_b - 1) * icc
    n_b = math.ceil(n_a * de_b)
    nv_b = math.ceil(n_b / m_b)

    # c) 20 nhân viên mỗi nhóm -> giới hạn c / ICC
    c_staff = 20
    n_eff_max_c = int(round(c_staff / icc))

    # d) 6 depot mỗi nhóm -> giới hạn c / ICC
    c_depot = 6
    n_eff_max_d = int(round(c_depot / icc))

    # e) Mức chênh 6 điểm (0.70 -> 0.76, cần 859/nhóm), 20 nhân viên mỗi nhóm
    n_6pt = co_mau_hai_ti_le(p1, p2_6pt, alpha=alpha, power=power)
    m_e = math.ceil(((1.0 - icc) * n_6pt) / (c_staff - icc * n_6pt))
    de_e = 1.0 + (m_e - 1) * icc
    n_eff_e = (c_staff * m_e) / de_e

    # Power thực tế ở mức +5 điểm nếu dùng n_per_arm = 859
    nd = NormalDist()
    za = nd.inv_cdf(1.0 - alpha / 2.0)
    pb_5 = (p1 + p2_5pt) / 2.0
    z_beta_2p = (abs(p2_5pt - p1) * math.sqrt(n_6pt) - za * math.sqrt(2.0 * pb_5 * (1.0 - pb_5))) / math.sqrt(
        p1 * (1.0 - p1) + p2_5pt * (1.0 - p2_5pt)
    )
    power_5pt_2p = nd.cdf(z_beta_2p)
    try:
        from statsmodels.stats.proportion import proportion_effectsize
        from statsmodels.stats.power import NormalIndPower
        h_5pt = abs(proportion_effectsize(p2_5pt, p1))
        power_5pt_sm = NormalIndPower().power(effect_size=h_5pt, nobs1=n_6pt, alpha=alpha, ratio=1.0)
    except ImportError:
        h_5pt = 2.0 * (math.asin(math.sqrt(p2_5pt)) - math.asin(math.sqrt(p1)))
        power_5pt_sm = nd.cdf(abs(h_5pt) * math.sqrt(n_6pt / 2.0) - za)

    # Tỉ lệ mo_lai_trong_7_ngay hiện tại
    mo_lai_all_cnt = int((reqs['mo_lai_trong_7_ngay'] == 1).sum())
    mo_lai_all_pct = reqs['mo_lai_trong_7_ngay'].mean() * 100.0
    pv_reqs = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    mo_lai_pv_cnt = int((pv_reqs['mo_lai_trong_7_ngay'] == 1).sum())
    mo_lai_pv_pct = pv_reqs['mo_lai_trong_7_ngay'].mean() * 100.0

    print('\n=== D1 · Cỡ mẫu kế hoạch Pilot (baseline=0.70, alpha=0.05, power=0.80, ICC=0.02) ===')
    print(f'  a) Chia theo yêu cầu (+5 điểm, 0.70 -> 0.75) : {n_a:,} yêu cầu/nhóm (tổng {2 * n_a:,} yêu cầu)')
    print(f'  b) Theo nhân viên (m = 75, ICC = 0.02)       : DE = {de_b:.2f} · cần {n_b:,} YC/nhóm -> {nv_b} nhân viên/nhóm (tổng {2 * nv_b} > 40: không đủ người)')
    print(f'  c) 20 nhân viên mỗi nhóm (c / ICC)           : tối đa < {n_eff_max_c:,} YC hiệu dụng/nhóm (< {n_a:,}: không đạt mốc +5 điểm)')
    print(f'  d) 6 depot mỗi nhóm (c / ICC)                : tối đa < {n_eff_max_d:,} YC hiệu dụng/nhóm (< {n_a:,} và chỉ có 6 cụm < 20)')
    print(f'  e) Mức chênh +6 điểm (n = {n_6pt}/nhóm, 20 NV/nhóm): cần m >= {m_e} YC/nhân viên (DE = {de_e:.2f}, n_hiệu_dụng = {n_eff_e:.1f})')
    print(f'  - Đánh đổi khi n = {n_6pt} nhưng tác động thật là +5 điểm: power giảm còn ~{power_5pt_2p:.2f} (2 tỉ lệ = {power_5pt_2p:.4f} · Cohen-h = {power_5pt_sm:.4f})')
    print(f'  - Tỉ lệ mo_lai_trong_7_ngay hiện tại         : toàn mẫu = {mo_lai_all_pct:.2f}% ({mo_lai_all_cnt}/{len(reqs)}) · phạm vi (noi_dia+hang_nang) = {mo_lai_pv_pct:.2f}% ({mo_lai_pv_cnt}/{len(pv_reqs)})')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    in_nhiem_vu_a(runs, reqs)
    in_nhiem_vu_b(runs, reqs)
    in_nhiem_vu_d(reqs)
