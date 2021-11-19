# 2745번

data = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N, B = input().split()
result = 0

for c in N:
    result *= int(B)
    result += data.index(c)

print(result)
