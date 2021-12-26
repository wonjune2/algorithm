from collections import deque
m, n = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(arr):
    queue = deque(arr)
    day = deque([0] * len(arr))
    md = 0
    while queue:
        x, y = queue.popleft()
        d = day.popleft()
        md = max(md, d)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx, ny))
                day.append(d + 1)
    return md

result = 0
arr = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            arr.append((i, j))

result = bfs(arr)

for i in range(n):
    if 0 in graph[i]:
        print(-1)
        break
else:
    print(result)