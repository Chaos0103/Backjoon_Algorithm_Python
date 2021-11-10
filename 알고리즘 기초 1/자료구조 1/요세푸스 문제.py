# 1158번
from collections import deque
data = deque()
result = list()

N, K = map(int, input().split())

for i in range(1, N+1):
    data.append(i)

for _ in range(N):
    for _ in range(K - 1):
        data.append(data.popleft())
    result.append(data.popleft())

print(f'<{result[0]}', end='')
for i in range(1, len(result)):
    print(f', {result[i]}',end='')
print('>')
