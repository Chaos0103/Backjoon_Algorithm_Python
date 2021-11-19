# 2089번

num = int(input())
data = []

if num == 0:
    print(0)
    exit()
while num != 0:
    if num % -2:
        data.append('1')
        num //= -2
        num += 1
    else:
        data.append('0')
        num //= -2

print(''.join(reversed(data)))
