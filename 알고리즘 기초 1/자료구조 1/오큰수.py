# 17298번

import sys
N = int(input())
data = list(map(int, sys.stdin.readline().split()))
result = [-1] * len(data)
stack = list()

stack.append(0)
for idx in range(1, N):
    while stack and data[stack[-1]] < data[idx]:
        result[stack.pop()] = data[idx]
    stack.append(idx)

print(*result)
