# 10866번
from collections import deque
import sys
Deque = deque()

N = int(input())

for _ in range(N):
    order = list(sys.stdin.readline().split())
    if order[0] == 'push_front':
        Deque.appendleft(int(order[1]))
    elif order[0] == 'push_back':
        Deque.append(int(order[1]))
    elif order[0] == 'pop_front':
        if len(Deque):
            print(Deque.popleft())
        else:
            print(-1)
    elif order[0] == 'pop_back':
        if len(Deque):
            print(Deque.pop())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(Deque))
    elif order[0] == 'empty':
        if len(Deque):
            print(0)
        else:
            print(1)
    elif order[0] == 'front':
        if len(Deque):
            print(Deque[0])
        else:
            print(-1)
    elif order[0] == 'back':
        if len(Deque):
            print(Deque[len(Deque) - 1])
        else:
            print(-1)
