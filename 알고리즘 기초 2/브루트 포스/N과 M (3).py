# 15651번

from itertools import product

N, M = map(int, input().split())
data = [i for i in range(1, N+1)]

result = list(product(data, repeat = M))

for d in result:
    for num in d:
        print(num, end=' ')
    print()
