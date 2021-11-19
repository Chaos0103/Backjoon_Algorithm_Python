# 11653번

num = int(input())
div = 2
while num != 1:
    if num % div == 0:
        print(div)
        num //= div
    else:
        div += 1
