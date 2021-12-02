# 11727번

n = int(input())
DT = [0,1,3]

for i in range(3, n+1):
    DT.append(DT[i-2]*2 + DT[i-1])

print(DT[n] % 10007)
