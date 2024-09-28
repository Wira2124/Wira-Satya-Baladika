# Fungsi untuk menghitung jarak fokus lensa
def hitung_fokus_lensa(n, R1, R2):
    # Menggunakan persamaan lensa pembuat
    f = 1 / ((n - 1) * (1/R1 + 1/R2))
    return f

# Fungsi untuk memperhitungkan alpha dan V0 (misalkan ada konteks lain yang memerlukan ini)
def pengaruh_alpha_v0(alpha, V0):
    # Ini adalah contoh, formula atau pengaruh alpha dan V0 bisa disesuaikan sesuai kebutuhan
    return alpha * V0

# Input dari pengguna
n = float(input("Masukkan nilai indeks bias n (misal: 1.50): "))
R1 = float(input("Masukkan nilai jari-jari kelengkungan R1 (dalam cm, misal: 22): "))
R2 = float(input("Masukkan nilai jari-jari kelengkungan R2 (dalam cm, misal: 17.5): "))
alpha = float(input("Masukkan nilai alpha (misal: 0.1): "))
V0 = float(input("Masukkan nilai V0 (misal: 2.0): "))

# Menghitung jarak fokus lensa
fokus = hitung_fokus_lensa(n, R1, R2)
pengaruh_alpha_v0 = pengaruh_alpha_v0(alpha, V0)

# Menampilkan hasil
print(f"Jarak fokus lensa (f) adalah: {fokus:.2f} cm")
print(f"Pengaruh alpha dan V0 adalah: {pengaruh_alpha_v0:.2f}")