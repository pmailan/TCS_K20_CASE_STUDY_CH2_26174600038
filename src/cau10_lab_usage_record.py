from datetime import datetime
ma_phien = input("Nhap ma phien: ")
ma_may = input("Nhap ma may: ")
cong_suat_w = float(input("Nhap cong suat thiet bi (W): "))
so_phut = int(input("Nhap thoi gian su dung (phut): "))
don_gia_kwh = float(input("Nhap don gia dien (VND/kWh): "))
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
su_dung_lau = so_phut > 60
thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")
print("\n--- PHIEU GHI NHAN SU DUNG THIET BI ---")
print(f"Ma phien: {ma_phien}")
print(f"May: {ma_may}")
print(f"Cong suat: {cong_suat_w:.2f} W")
print(f"Thoi luong: {so_phut} phut")
print(f"Dien nang: {dien_nang_kwh:.3f} kWh")
print(f"Chi phi: {chi_phi:.2f} VND")
print(f"Tren 60 phut: {su_dung_lau}")
print(f"Ghi nhan luc: {thoi_diem_text}")