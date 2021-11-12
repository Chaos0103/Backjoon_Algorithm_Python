# 1935번

import sys

N = int(input())
I = sys.stdin.readline().rstrip()
data = list()
stack = []

for _ in range(N):
    data.append(int(input()))

for c in I:
    if c in '+-*/':
        num1 = stack.pop()
        num2 = stack.pop()
        if c == '+':
            stack.append(num2 + num1)
        elif c == '-':
            stack.append(num2 - num1)
        elif c == '*':
            stack.append(num2 * num1)
        elif c == '/':
            stack.append(num2 / num1)
    else:
        stack.append(data[ord(c)-ord('A')])

print('%.2lf'%stack[0])
