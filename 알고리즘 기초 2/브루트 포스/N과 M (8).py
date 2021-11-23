# 15657번

from itertools import combinations_with_replacement

N, M = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
result = list(combinations_with_replacement(data, M))

for li in result:
    for num in li:
        print(num, end = ' ')
    print()
