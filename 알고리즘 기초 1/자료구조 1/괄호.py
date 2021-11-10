# 9012번
import sys

T = int(input())
for _ in range(T):
    S = sys.stdin.readline().rstrip()
    cnt = 0
    for c in S:
        if c == '(':
            cnt += 1
        elif c == ')':
            cnt -= 1
        if cnt < 0:
            break
    if cnt == 0:
        print('YES')
    else:
        print('NO')
