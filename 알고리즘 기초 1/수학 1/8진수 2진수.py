# 1212번

import sys
from collections import deque
num = sys.stdin.readline().rstrip()
result = deque()
for c in num:
    if c == '0':
        result += '000'
    elif c == '1':
        result += '001'
    elif c == '2':
        result += '010'
    elif c == '3':
        result += '011'
    elif c == '4':
        result += '100'
    elif c == '5':
        result += '101'
    elif c == '6':
        result += '110'
    elif c == '7':
        result += '111'

for _ in range(2):
    if result[0] == '0':
        result.popleft()
print(''.join(result))
