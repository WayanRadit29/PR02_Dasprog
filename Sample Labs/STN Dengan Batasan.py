def sever_or_unite(N):
    # Pastikan N adalah dalam batasan -100000 sampai 100000
    if -100000 <= N <= 100000:
        N_str = str(N)  # Ubah N menjadi string untuk pengecekan '4'
        if '4' in N_str:
            print("SEVER")
        else:
            print("UNITE")
    else:
        print("Maaf, nilai yang anda masukkan tidak ada dalam batas ")

# Input nilai N
try:
    # Memastikan input hanya menerima angka bulat (integer)
    N = int(input())
    # Panggil fungsi untuk menjalankan program
    sever_or_unite(N)
except ValueError:
    print("Input tidak valid. Masukkan angka bulat.")
