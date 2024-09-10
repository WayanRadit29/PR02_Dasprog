# Input dari pengguna berupa karakter
color = input("Masukkan huruf pertama warna tabung: ").lower() #lower adalah fungsi yang mengubah huruf string ke versi kecilnya

# Cek isi berdasarkan warna
if color == 'o':
    print("Isi tabung: Ammonia")
elif color == 'b':
    print("Isi tabung: Carbon Monoxide")
elif color == 'y':
    print("Isi tabung: Hydrogen")
elif color == 'g':
    print("Isi tabung: Oxygen")
else:
    print("Isi tabung: Contents unknown")
