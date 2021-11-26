# 1463번

DT = [0] * 1000001

N = int(input())

for num in range(2, N + 1):
    DT[num] = DT[num - 1] + 1
    if num % 3 == 0:
        DT[num] = min(DT[num], DT[num // 3] + 1)
    if num % 2 == 0:
        DT[num] = min(DT[num], DT[num // 2] + 1)

print(DT[N])
