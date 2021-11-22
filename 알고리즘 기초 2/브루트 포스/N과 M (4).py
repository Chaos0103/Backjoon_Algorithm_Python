# 15652번

from itertools import combinations_with_replacement

N, M = map(int, input().split())
data = [i for i in range(1, N+1)]

result = list(combinations_with_replacement(data, M))

for d in result:
    for num in d:
        print(num, end=' ')
    print()
