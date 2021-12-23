from collections import deque

n = int(input())
s = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [1, 0]
dy = [0, 1]

def dfs(x, y):
    stack = deque([(x, y)])
    visited = []
    visited.append((x, y))
    while stack:
        x, y = stack.pop()
        if (x, y) not in visited:
            visited.append((x, y))
            for i in range(2):
                nx = x + dx[i]
                ny = y + dy[i]
            
    