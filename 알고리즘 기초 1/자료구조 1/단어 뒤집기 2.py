# 17413번
from collections import deque
import sys

data = deque(sys.stdin.readline().rstrip())
arr = []
result = []

while True:
    if len(data) == 0:
        break
    if data[0] == '<':
        while True:
            if data[0] == '>':
                arr.append(data.popleft())
                result.append(arr)
                arr = []
                break
            arr.append(data.popleft())
    else:
        while True:
            if len(data) == 0 or data[0] == '<':
                result.append(arr)
                arr = []
                break
            if data[0] == ' ':
                arr.append(data.popleft())
                result.append(arr)
                arr = []
                break
            arr.append(data.popleft())

for i in range(len(result)):
    if result[i][0] == '<':
        print(''.join(result[i]), end='')
    else:
        if result[i][len(result[i])-1] == ' ':
            result[i].pop()
            print(''.join(reversed(result[i])), end=' ')
        else:
            print(''.join(reversed(result[i])), end='')
