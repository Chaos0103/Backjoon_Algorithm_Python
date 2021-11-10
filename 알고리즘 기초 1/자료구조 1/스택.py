# 10828번
from collections import deque
import sys
STACK = deque()
idx = -1
N = int(input())
for _ in range(N):
    order = list(sys.stdin.readline().split())
    if order[0] == 'push':
        STACK.append(int(order[1]))
        idx += 1
    elif order[0] == 'pop':
        if idx == -1:
            print(-1)
        else:
            print(STACK[idx])
            STACK.pop()
            idx -= 1
    elif order[0] == 'size':
        print(idx + 1)
    elif order[0] == 'empty':
        if idx == -1:
            print(1)
        else:
            print(0)
    elif order[0] == 'top':
        if idx == -1:
            print(-1)
        else:
            print(STACK[idx])
