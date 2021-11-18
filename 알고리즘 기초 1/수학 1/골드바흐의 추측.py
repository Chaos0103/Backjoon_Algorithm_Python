# 6588번

import sys

data = [True] * 1000001

for i in range(2, 1000000):
    if data[i]:
        j = 2
        while i * j <= 1000000:
            data[i * j] = False
            j += 1

while True:
    num = int(sys.stdin.readline())
    if num == 0:
        break

    switch = 0
    for i in range(2, num + 1):
        if data[i] and data[num - i]:
            print(f'{num} = {i} + {num - i}')
            break
