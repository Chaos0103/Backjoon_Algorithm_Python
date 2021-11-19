# 11576번

A, B = map(int, input().split())
m = int(input())
data = list(map(int, input().split()))

AtoB = 0
for n in data:
    AtoB *= A
    AtoB += n

result = []
while AtoB != 0:
    result.append(str(AtoB % B))
    AtoB //= B

print(' '.join(reversed(result)))
