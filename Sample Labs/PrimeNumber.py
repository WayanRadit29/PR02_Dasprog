#Mendeklarasikan sebuah fungsi untuk mengecek bilangan prima atau tidak
def cek_prima(number):
    if number <= 1:
        return False  # Bilangan kurang dari atau sama dengan 1 bukan prima
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False  # Jika bisa dibagi, bukan prima
    return True  # Jika tidak ada pembagi, maka prima

# Input dari pengguna
number = int(input("Masukkan sebuah bilangan: "))

# Mengecek apakah bilangan prima
if cek_prima(number):
    print(f"{number} adalah bilangan prima")
else:
    print(f"{number} bukan bilangan prima")

