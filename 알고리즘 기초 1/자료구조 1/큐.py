# 10845번
from collections import deque
import sys

queue = deque()
idx = -1
T = int(input())

for _ in range(T):
    order = list(sys.stdin.readline().split())
    if order[0] == 'push':
        queue.append(int(order[1]))
        idx += 1
    elif order[0] == 'pop':
        if idx == -1:
            print(-1)
        else:
            print(queue.popleft())
            idx -= 1
    elif order[0] == 'size':
        print(idx + 1)
    elif order[0] == 'empty':
        if idx == -1:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if idx == -1:
            print(-1)
        else:
            print(queue[0])
    elif order[0] == 'back':
        if idx == -1:
            print(-1)
        else:
            print(queue[idx])
