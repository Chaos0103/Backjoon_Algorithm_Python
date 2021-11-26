# 2667번

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y, cnt):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = cnt
        dfs(x-1, y, cnt)
        dfs(x, y-1, cnt)
        dfs(x+1, y, cnt)
        dfs(x, y+1, cnt)
        return True
    return False

result = 0
cnt = 2
for i in range(n):
    for j in range(n):
        if dfs(i, j, cnt) == True:
            result += 1
            cnt += 1

print(result)

count = [0] * result
for i in range(n):
    for j in range(2, cnt):
        count[j - 2] += graph[i].count(j)
count = sorted(count)
for n in count:
    print(n)
