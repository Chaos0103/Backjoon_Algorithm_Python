# 17087번

import math

N, S = map(int, input().split())
data = list(map(int, input().split()))

data.append(S)
data.sort(reverse=True)

dif = list()
for i in range(N):
    dif.append(data[i] - data[i+1])

result = dif[0]

for i in range(1, N):
    result = math.gcd(result, dif[i])

print(result)
