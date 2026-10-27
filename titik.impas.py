import math

nama = "Tri Kholipianto Rahmatsyah"
nim = "20250040019"

def fungsi(x):
    return 800 * math.exp(0.3 * x) - (2000 + 400 * x)

batas_bawah = 5
batas_atas = 6
error = 0.00001

print("PROGRAM PENCARIAN TITIK IMPAS")
print("Metode Numerik: Biseksi")
print("Nama :", "Tri Kholipianto Rahmatsyah")
print("NIM  :", "20250040019")
print("-" * 75)
print(f"{'No':<6}{'Tengah':<15}{'f(Tengah)':<18}{'Galat':<15}")
print("-" * 75)

tengah_lama = batas_bawah

for nomor in range(1, 101):
    tengah = (batas_bawah + batas_atas) / 2
    hasil = fungsi(tengah)
    galat = abs(tengah - tengah_lama)

    print(f"{nomor:<6}{tengah:<15.4f}{hasil:<18.4f}{galat:<15.4f}")

    if abs(hasil) < error:
        break

    if fungsi(batas_bawah) * hasil < 0:
        batas_atas = tengah
    else:
        batas_bawah = tengah

    tengah_lama = tengah

print("-" * 75)
print("Hasil perhitungan:")
print(f"Perkiraan titik impas = {tengah:.4f} bulan")
print(f"Nilai fungsi          = {fungsi(tengah):.4f}")