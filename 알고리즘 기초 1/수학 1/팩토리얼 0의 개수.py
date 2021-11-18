# 1676번

N = int(input())

mul = 1
cnt = 0

while N >= 5:
    cnt += N // 5
    N //= 5

print(cnt)
