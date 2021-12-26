from collections import deque
t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    res = 0
    while queue:
        x, y = queue.popleft()
        if graph[x][y] == 1:
            res += 1
            graph[x][y] = 0
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                
                if graph[nx][ny] == 0:
                    continue
                
                if graph[nx][ny] == 1:
                    queue.append((nx, ny))
    return res

for i in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for j in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1
    result = 0
    z = 0
    for q in range(n):
        for w in range(m):
            z = bfs(q, w)
            if z:
                result += 1
    print(result)