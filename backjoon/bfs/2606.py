from collections import deque
n = int(input())
c = int(input())

graph = [[] for _ in range(n + 1)]

for i in range(1, c + 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    queue = deque([v])
    visited = []
    visited.append(v)
    count = 0
    while queue:
        s = queue.popleft()
        count += 1
        for i in graph[s]:
            if i not in visited:
                queue.append(i)
                visited.append(i)
    return count

print(bfs(1) - 1)