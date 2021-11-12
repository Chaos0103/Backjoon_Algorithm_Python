# 9613번

from math import gcd

N = int(input())

for _ in range(N):
    data = list(map(int, input().split()))
    sum = 0
    for i in range(1, data[0]):
        for j in range(i+1, data[0] + 1):
            sum += gcd(data[i], data[j])
    print(sum)
