# 9093번
import sys

T = int(input())
for _ in range(T):
    s = list(sys.stdin.readline().split())
    for i in range(len(s)):
        for j in range(len(s[i]) - 1, -1, -1):
            print(s[i][j], end='')
        print(end=' ')
    print()
