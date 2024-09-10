def last_man_standing(N, C):
    # Jika N % 4 == 0, pemain yang memulai pertama akan menang
    if N % 4 == 0:
        return "Lala" if C == 1 else "Lili"
        
    else:
        # Jika N % 4 != 0, pemain yang memulai akan kalah
        return "Lala" if C == 2 else "Lili"

# Contoh Input
N, C = map(int, input().split())

# Output Pemenang
print(last_man_standing(N, C))
