# 1874번
from collections import deque
STACK = deque()
data = list()
result = list()

T = int(input())

for _ in range(T):
    data.append(int(input()))

idx = 0
STACKidx = -1
for num in range(1, T + 1):
    STACK.append(num)
    result.append('+')
    STACKidx += 1
    for _ in range(T):
        if STACKidx == -1:
            break
        if STACK[STACKidx] == data[idx]:
            STACK.pop()
            result.append('-')
            idx += 1
            STACKidx -= 1
        else:
            break

if STACKidx == -1:
    for c in result:
        print(c)
else:
    print('NO')
