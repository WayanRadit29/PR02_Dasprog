
M,N,T = map(int, input().split())
RTime = (T % 85)

if(RTime > 25):
    RGreen = RTime - 25
else:
    RGreen = 0
    
mobil_keluar = ( (T // 85) * 12 + RGreen // 5)
rem = (M + N + 1) - mobil_keluar

if(mobil_keluar >= M + 1):
    print(f"YES! {rem}")
else:
    print(f"NO! {rem}")
