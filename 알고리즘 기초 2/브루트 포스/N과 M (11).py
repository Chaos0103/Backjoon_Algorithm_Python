# 15665번

from itertools import product

N, M = map(int, input().split())
data = list(map(int, input().split()))

data = sorted(data)
perdata = list(product(data, repeat = M))
perdata = sorted(list(set(perdata)))

for li in perdata:
    for num in li:
        print(num, end=' ')
    print()
