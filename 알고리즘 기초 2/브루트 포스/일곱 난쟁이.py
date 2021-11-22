# 2309번

from itertools import combinations
data = list()
for _ in range(9):
    data.append(int(input()))

data.sort()
result = list(combinations(data, 7))

for li in result:
    if sum(li) == 100:
        for num in li:
            print(num)
        break
