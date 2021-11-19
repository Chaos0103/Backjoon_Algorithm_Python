# 17103번

import math
data = [True] * 1000001
data[1] = False

for i in range(2, int(math.sqrt(1000000)) + 1):
    if data[i]:
        j = 2
        while i * j <= 1000000:
            data[i * j] = False
            j += 1

T = int(input())
for _ in range(T):
    num = int(input())
    cnt = 0
    for i in range(2, num // 2 + 1):
        if data[i] and data[num - i]:
            cnt += 1
    print(cnt)
