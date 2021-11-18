# 1929번

import math

M, N = map(int, input().split())

data = [True] * (N + 1)
data[1] = False

for i in range(2, int(math.sqrt(N)) + 1):
    if data[i] == True:
        j = 2
        while i * j <= N:
            data[i * j] = False
            j += 1

for i in range(M, N + 1):
    if data[i]:
        print(i)
