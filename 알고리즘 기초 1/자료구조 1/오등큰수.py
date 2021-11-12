# 17299번

import sys
from collections import Counter
N = int(input())
data = list(map(int, sys.stdin.readline().split()))
result = [-1] * len(data)
cnt = Counter(data)
stack = list()

stack.append(0)
for idx in range(1, N):
    while stack and cnt[data[stack[-1]]] < cnt[data[idx]]:
        result[stack.pop()] = data[idx]
    stack.append(idx)

print(*result)
