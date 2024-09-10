#Program untuk menghitung diskon dan pajak untuk pembelian suatu barang oleh murid atau tidak


from decimal import Decimal

# Memasukkan total pembelian
TotalP = Decimal(input("Masukkan Total Pembelian : "))

# Memasukkan status apakah siswa atau bukan
Status = str(input("Apakah dia Siswa atau tidak (Ketik Ya / Tidak) :"))

# Jika status siswa
if Status == "Ya":
    print(f"Total Purchase : {TotalP}")
    
    # Menghitung diskon 20%
    discount = "%.2f" %((20 * TotalP) / 100)
    print(f"Student's discount : {discount}")
    discount = Decimal(discount)
    
    # Menghitung harga setelah diskon
    Hdiscount = TotalP - discount
    print(f"Discounted Total : {Hdiscount}")
    
    # Menghitung pajak 5%
    tax = "%.2f" %((5 * Hdiscount) / 100)
    print(f"Sales Tax (5%) : {tax}")
    tax = Decimal(tax)
    
    # Menghitung total bayar
    TotalB = Hdiscount + tax
    print(f"Total : {TotalB}")

# Jika bukan siswa
elif Status == "Tidak":
    print(f"Total Pembelian: {TotalP}")
    
    # Menghitung pajak 5% tanpa diskon
    tax = "%.2f" % ((5 * TotalP) / 100)
    print(f"Sales Tax (5%) : {tax}")
    #Mendeklarasi tax menjadi tipe data decimal kembali
    tax = Decimal(tax) 
    
    # Menghitung total bayar
    TotalB = TotalP + tax
    print(f"Total yang harus dibayar: {TotalB}")

# Jika input status salah
else:
    print("Error: Input status tidak valid.")





    
