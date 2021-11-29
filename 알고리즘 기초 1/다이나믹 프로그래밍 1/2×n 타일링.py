# 11726번

n = int(input())

DT = [0] * 1001
DT[1] = 1
DT[2] = 2

for i in range(3, n+1):
    DT[i] = (DT[i-1] + DT[i-2]) % 10007

print(DT[n])
