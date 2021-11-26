# 15663번

import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

data = sorted(data)
perdata = list(permutations(data, M))
perdata = sorted(list(set(perdata)))

for li in perdata:
    for num in li:
        print(num, end=' ')
    print()
