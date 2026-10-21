ma_may = input("Nhap ma may: ")
cong_suat_w = float(input("Nhap cong suat W: "))
so_phut = int(input("Nhap so phut: "))
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"May: {ma_may}")
print(f"Dien nang: {dien_nang_kwh:.3f} kWh")
# Loi 1: cong_suat_w la chuoi nen khong the tinh toan truc tiep
# Loi 2: can chuyen cong_suat_w sang float truoc khi tinh dien nang
