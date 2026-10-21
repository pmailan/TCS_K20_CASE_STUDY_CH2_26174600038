from datetime import datetime
ma_phien = input("Nhap ma phien: ")
ma_may = input("Nhap ma may: ")
cong_suat = float(input("Nhap cong suat thiet bi (W): "))
thoi_gian = int(input("Nhap thoi gian su dung (phut): "))
don_gia = float(input("Nhap don gia dien (VND/kWh): "))
dien_nang = cong_suat * thoi_gian / 60 / 1000
chi_phi = dien_nang * don_gia
tren_60_phut = thoi_gian > 60
thoi_diem = datetime.now()
print("\n===== BAO CAO SU DUNG THIET BI =====")
print(f"Ma phien: {ma_phien}")
print(f"May: {ma_may}")
print(f"Cong suat: {cong_suat:.2f} W")
print(f"Thoi luong: {thoi_gian} phut")
print(f"Dien nang: {dien_nang:.3f} kWh")
print(f"Chi phi: {chi_phi:.2f} VND")
print(f"Tren 60 phut: {tren_60_phut}")
print(f"Ghi nhan luc: {thoi_diem.strftime('%Y-%m-%d %H:%M:%S')}")