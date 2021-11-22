# 15654번

from itertools import permutations

N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

result = list(permutations(data, M))

for d in result:
    for num in d:
        print(num, end=' ')
    print()
