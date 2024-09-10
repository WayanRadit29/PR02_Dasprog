#Program ini bertujuan untuk memberitahu selisih waktu untuk menonton live streaming dalam sebuah kondisi dimana ada dua zonz waktu yang berbeda.

HH, MM, SS = map(int, input().split(":"))
CH, CM, CS = map(int, input().split(":"))

SisaWaktu = (((HH * 3600) + (MM * 60) + SS) + (5 * 3600)) - ((CH * 3600) + (CM * 60) + CS)

if SisaWaktu >= 0:
    AH = SisaWaktu // 3600
    AM = (SisaWaktu - (AH * 3600)) // 60
    AS =  (SisaWaktu - (AH * 3600) - (AM * 60))
    print(f"{AH:02}:{AM:02}:{AS:02}")
   
else:
    print("See you on the next Pear Event!")





