import numpy as np
import matplotlib.pyplot as plt

# Diketahui
g = 9.8  # percepatan gravitasi (m/s^2)
h0 = 100  # ketinggian awal (misalnya 100 meter, bisa diubah sesuai kebutuhan)

# 1. Tentukan waktu yang diperlukan benda untuk mencapai tanah
t_fall = np.sqrt((2 * h0) / g)
print(f"Waktu yang diperlukan untuk benda jatuh: {t_fall:.2f} detik")

# 2. Kecepatan benda sebagai fungsi waktu
def velocity(t, g):
    return g * t

# 3. Posisi benda (ketinggian) sebagai fungsi waktu
def position(t, h0, g):
    return h0 - 0.5 * g * t**2

# Waktu dari 0 hingga waktu jatuh
t = np.linspace(0, t_fall, 100)

# Hitung kecepatan dan posisi untuk setiap titik waktu
v_t = velocity(t, g)
h_t = position(t, h0, g)

# Plot grafik kecepatan sebagai fungsi waktu
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(t, v_t)
plt.title("Grafik Kecepatan vs Waktu")
plt.xlabel("Waktu (detik)")
plt.ylabel("Kecepatan (m/s)")
plt.grid(True)

# Plot grafik posisi sebagai fungsi waktu
plt.subplot(1, 2, 2)
plt.plot(t, h_t)
plt.title("Grafik Posisi vs Waktu")
plt.xlabel("Waktu (detik)")
plt.ylabel("Ketinggian (meter)")
plt.grid(True)

plt.tight_layout()
plt.show()
