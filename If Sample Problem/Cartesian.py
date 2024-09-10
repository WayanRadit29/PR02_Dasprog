#Jadi disini kita mencoba membuat program untuk menentukan letak dua buah titik (x, y) 
#Kita perlu mengeluarkan output apakah dia terletak di kuadran atau dia terletak di sumbu x atau sumbu y

x, y = map(float, input("Masukan titik koordinat : ").split(","))

if x == 0 and y == 0:
    print(f"titik {x,y} adalah titik pusat")
elif x == 0 and (y > 0 or y < 0) :
    print(f"titik {x,y} terletak di sumbu Y")
elif y == 0 and (x > 0 or x < 0) :
    print(f"titik {x,y} terletak di sumbu X")
elif y > 0 and x > 0  :
    print(f"titik {x,y} terletak di kuadran I")
elif y > 0 and  x < 0 :
    print(f"titik {x,y} terletak di kuadran II")
elif y < 0 and x < 0 :
    print(f"titik {x,y} terletak di kuadran III")
elif y < 0 and x > 0 :
    print(f"titik {x,y} terletak di kuadran IV")

