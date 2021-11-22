# 15649번

from itertools import permutations

N, M = map(int, input().split())
data = [i for i in range(1, N+1)]

result = list(permutations(data, M))

for d in result:
    for num in d:
        print(num, end=' ')
    print()
