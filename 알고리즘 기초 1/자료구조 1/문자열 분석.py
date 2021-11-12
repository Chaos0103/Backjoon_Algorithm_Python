# 10809번

import sys

while True:
    line = sys.stdin.readline().rstrip('\n')
    data = [0] * 4
    if not line:
        break

    for c in line:
        if 'a' <= c <= 'z':
            data[0] += 1
        elif 'A' <= c <= 'Z':
            data[1] += 1
        elif '0' <= c <= '9':
            data[2] += 1
        elif c == ' ':
            data[3] += 1
    print(*data)
