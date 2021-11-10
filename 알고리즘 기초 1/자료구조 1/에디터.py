# 1406번
import sys

stack1 = list(sys.stdin.readline().strip())
stack2 = list()

M = int(input())

for _ in range(M):
    order = sys.stdin.readline().rstrip()
    if order[0] == 'P':
        stack1.append(order[2])
    elif order == 'L':
        if stack1 != []:
            stack2.append(stack1.pop(-1))
    elif order == 'D':
        if stack2 != []:
            stack1.append(stack2.pop(-1))
    elif order == 'B':
        if stack1 != []:
            stack1.pop(-1)
            
print(''.join(stack1 + list(reversed(stack2))))
