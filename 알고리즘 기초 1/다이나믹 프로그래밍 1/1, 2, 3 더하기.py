# 9095번

DT = [0] * 11
DT[1] = 1
DT[2] = 2
DT[3] = 4

for i in range(4, 11):
    for j in range(3):
        DT[i] += DT[i-j-1]

n = int(input())

for i in range(n):
    num = int(input())
    print(DT[num])
