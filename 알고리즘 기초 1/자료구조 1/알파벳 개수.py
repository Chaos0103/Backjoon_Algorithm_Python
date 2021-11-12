# 10808번

import sys
data = [0] * 26
s = sys.stdin.readline().rstrip()

for c in s:
    data[ord(c) - ord('a')] += 1

print(*data)
