array = list(map(int, input().split()))
i = int(input())
j = int(input())
for _ in range(j):
    temp = array[:7-i]
    array[:7-i] = array[-i:]
    array[-i:] = temp
    # print(arr)
k, l, m = map(int,input().split())
print(array[k], array[l], array[m])