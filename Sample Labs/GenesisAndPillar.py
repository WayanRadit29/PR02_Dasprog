# Input kemampuan lompat B dan jarak antar pilar :
Input = list(map(int, input().split()))

#Deklarasi variabel pada array :
l = Input[0]
jarak = Input[1:]

# Cek apakah B bisa melompati semua pilar
bisa_lompat = True  # Anggap B bisa melompati semua pilar

# Periksa setiap jarak antar pilar
for p in jarak:
    if p > l :  # Jika ada jarak yang lebih besar dari jarak lompatan B
        bisa_lompat = False  # B tidak bisa melompat
        break

# Output hasil
if bisa_lompat:
    print("YES HE CAN")
else:
    print("NO HE CAN'T")
