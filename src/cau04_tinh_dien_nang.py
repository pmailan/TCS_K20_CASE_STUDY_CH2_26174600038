cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print("Dien nang:", dien_nang_kwh, "kWh")
print("Chi phi:", chi_phi, "VND")
print("Kieu dien nang:", type(dien_nang_kwh))
print("Kieu chi phi:", type(chi_phi))
so_phut = 60
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print("Khi su dung 60 phut:")
print("Dien nang:", dien_nang_kwh, "kWh")
print("Chi phi:", chi_phi, "VND")