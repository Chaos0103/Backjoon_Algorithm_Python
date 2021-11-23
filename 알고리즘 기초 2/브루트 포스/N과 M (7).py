# 15656번

from itertools import product

N, M = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
result = list(product(data, repeat = M))

for li in result:
    for num in li:
        print(num, end = ' ')
    print()
