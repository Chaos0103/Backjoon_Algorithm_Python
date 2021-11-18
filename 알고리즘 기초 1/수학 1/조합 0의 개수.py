# 2004번

n, m = map(int, input().split())

def cnt(num, div):
    cnt = 0
    while num:
        num //= div
        cnt += num
    return cnt

five = cnt(n, 5) - cnt(m, 5) - cnt(n-m, 5)
two = cnt(n, 2) - cnt(m, 2) - cnt(n-m, 2)

result = min(five, two)

print(result)
