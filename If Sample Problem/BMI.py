#Program menghitung BMI dan Mengelompokkannya berdasarkan tabel yang diberikan

# Meminta input dari pengguna
berat_lb = float(input("Masukkan berat badan Anda dalam pon: "))
tinggi_in = float(input("Masukkan tinggi badan Anda dalam inci: "))

# Menghitung BMI/IMT
imt = (703 * berat_lb) / (tinggi_in ** 2)

# Menentukan kategori IMT
if imt < 18.5:
    status = "Underweight"
elif 18.5 <= imt <= 24.9:
    status = "Normal"
elif 25.0 <= imt <= 29.9:
    status = "Overweight"
else:
    status = "Obese"

# Menampilkan hasil
print(f"IMT Anda adalah: {imt:.1f}")
print(f"Status berat badan: {status}")
