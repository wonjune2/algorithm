from collections import deque

n = int(input())
s = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False] * n for _ in range(n)]
print(visited)
dx = [1, 0]
dy = [0, 1]


def dfs(x, y, t):
    if x >= n or y >= n:
        return False
    if t > 2:
        return False
    
    if not visited[x][y]:
        visited[x][y] = True
        dfs(x + 1, y, y - t)
        dfs(x, y + 1, x - t)