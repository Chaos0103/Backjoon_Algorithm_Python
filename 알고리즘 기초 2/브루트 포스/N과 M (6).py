# 15655번

from itertools import combinations

N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

result = list(combinations(data, M))

for d in result:
    for num in d:
        print(num, end=' ')
    print()
