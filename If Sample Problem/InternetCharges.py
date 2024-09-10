# Input dari pengguna berupa jumlah data yang digunakan
data_usage = float(input("Masukkan jumlah penggunaan data (Gb): "))

# Cek biaya berdasarkan penggunaan data
if 0.0 <= data_usage <= 1.0:
    charges = 250
elif 1.0 < data_usage <= 2.0:
    charges = 500
elif 2.0 < data_usage <= 5.0:
    charges = 1000
elif 5.0 < data_usage <= 10.0:
    charges = 1500
elif data_usage > 10.0:
    charges = 2000
else:
    # Data tidak valid jika penggunaan data kurang dari 0
    charges = None

# Output biaya atau pesan error jika data tidak valid
if charges is not None: #not berarti negasi
    print(f"Biaya yang harus dibayar: {charges} rupiah")
else:
    print("Data tidak valid.")
