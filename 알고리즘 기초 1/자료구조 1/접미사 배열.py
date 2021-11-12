# 11656번

import sys

data = []
line = sys.stdin.readline().rstrip()

for i in range(len(line)):
    data.append(line[i:len(line)])

result = sorted(data)

for s in result:
    print(s)
