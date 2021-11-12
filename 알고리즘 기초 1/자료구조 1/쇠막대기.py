# 10799번

import sys
data = []

order = sys.stdin.readline().rstrip()
idx = -1
cnt = 0
for c in order:
    if c == '(':
        data.append(1)
        idx += 1
    else:
        if data[idx] == 1:
            for i in range(idx):
                data[i] += 1
            data.pop()
            idx -= 1
        else:
            cnt += data.pop()
            idx -= 1

print(cnt)
