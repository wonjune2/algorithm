t = int(input())

def dfs(x, y):
    
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

for i in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for j in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1
    result = 0
    
    for q in range(n):
        for w in range(m):
            if dfs(q, w):
                result += 1
    print(result)


    