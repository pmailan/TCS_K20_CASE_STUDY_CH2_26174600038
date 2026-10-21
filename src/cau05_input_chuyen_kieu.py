ma_may = input("Nhap ma may: ")
cong_suat_w = float(input("Nhap cong suat W: "))
so_phut = int(input("Nhap so phut: "))
don_gia_kwh = float(input("Nhap don gia dien/kWh: "))
print("Kieu ma may:", type(ma_may))
print("Kieu cong suat:", type(cong_suat_w))
print("Kieu so phut:", type(so_phut))
print("Kieu don gia:", type(don_gia_kwh))
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print("Dien nang:", dien_nang_kwh, "kWh")
print("Chi phi:", chi_phi, "VND")