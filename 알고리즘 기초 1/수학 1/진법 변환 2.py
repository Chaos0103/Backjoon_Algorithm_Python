# 11005번

data = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = []
N, B = map(int, input().split())

while N != 0:
    result.append(data[N % B])
    N //= B

print(''.join(reversed(result)))
