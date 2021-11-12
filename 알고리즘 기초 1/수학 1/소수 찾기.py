# 1978번

N = int(input())
data = list(map(int, input().split()))
cnt = 0
for num in data:
    j = 2
    while j < num:
        if num % j == 0:
            break
        j += 1
    if j == num:
        cnt += 1

print(cnt)
