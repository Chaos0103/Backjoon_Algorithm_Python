# 1934번

import math

N = int(input())

for _ in range(N):
    n, m = map(int, input().split())
    print(math.lcm(n, m))

# PyPy3에서는 안됨
