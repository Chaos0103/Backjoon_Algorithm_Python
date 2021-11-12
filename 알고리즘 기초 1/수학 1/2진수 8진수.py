# 1373번

import sys
num = 0
mul = 1
result = list()
binary = list(sys.stdin.readline().rstrip())

binary.reverse()

for i in range(len(binary)):
    if i % 3 == 0 and i != 0:
        mul = 1
        result.append(num)
        num = 0
    if binary[i] == '1':
        num += mul
    mul *= 2
result.append(num)
result.reverse()

for n in result:
    print(n, end='')
