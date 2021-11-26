# 15664번

from itertools import combinations

N, M = map(int, input().split())
data = list(map(int, input().split()))

data = sorted(data)
perdata = list(combinations(data, M))
perdata = sorted(list(set(perdata)))

for li in perdata:
    for num in li:
        print(num, end=' ')
    print()
