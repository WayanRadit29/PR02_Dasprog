#Program ini meminta kita untuk menenetukan status berdasarkan umur yang diinput


age_max = int(input("Masukan Batas Umur Maksimum : "))
age_min = int(input("Masukan Batas Umur Minimum :"))
age = int(input("Masukan Umur : "))
smoker = int(input("Apakah dia smoker atau tidak? (Ketik 1 jika benar dan 0 jika salah): "))

if age_min <= age <= age_max and smoker == 0:
    if age > 59:
        sts = str(input("Masukan Status : "))
        if sts == 'W':
            print("Working Senior")
        else:
            print("Retired Senior")
    elif age > 20: 
        print("Adult")
    elif age > 12:
        print("Teen")
    else:
        print("Child")
else:
    print("Maaf program tidak bisa dijalankan")