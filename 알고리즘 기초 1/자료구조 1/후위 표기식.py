# 1918번

import sys

line = sys.stdin.readline().rstrip()
stack = list()
result = list()

for c in line:
    if c.isalpha():
        result.append(c)
    else:
        if c == '(':
            stack.append(c)
        elif c == '*' or c == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                result.append(stack.pop())
            stack.append(c)
        elif c == '+' or c == '-':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()

while stack:
    result.append(stack.pop())
print(''.join(result))
