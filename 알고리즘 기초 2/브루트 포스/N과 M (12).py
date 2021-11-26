# 15666번

from itertools import combinations_with_replacement

N, M = map(int, input().split())
data = list(map(int, input().split()))

data = sorted(data)
perdata = list(combinations_with_replacement(data, M))
perdata = sorted(list(set(perdata)))

for li in perdata:
    for num in li:
        print(num, end=' ')
    print()
