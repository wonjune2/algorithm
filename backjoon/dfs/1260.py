from collections import deque
n, m, v = map(int, input().split())
visited = [False] * (n + 1)
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def DFS(start):
    stack = deque([start])
    visited = []

    while stack:
        now = stack.pop()
        if now not in visited:
            visited.append(now)
            temp = []
            for v in graph[now]:
                if v not in visited:
                    temp.append(v)
            temp.sort(reverse=True)
            stack += temp
    visited_str = [str(i) for i in visited]
    return ' '.join(visited_str)

print(DFS(v))

# bfs
visited = [False] * (n + 1)
def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, v, visited)