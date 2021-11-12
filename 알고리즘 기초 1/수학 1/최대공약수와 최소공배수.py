# 2609번

import math

n, m = map(int, input().split())

print(math.gcd(n, m))
print(math.lcm(n, m))

# PyPy3에서는 안됨
