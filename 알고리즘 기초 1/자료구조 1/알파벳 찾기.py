# 10809번

import sys
data = [-1] * 26
s = sys.stdin.readline().rstrip()

for i in range(len(s)):
    if data[ord(s[i]) - ord('a')] == -1:
        data[ord(s[i]) - ord('a')] = i

print(*data)
