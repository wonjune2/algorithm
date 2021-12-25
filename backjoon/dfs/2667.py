from collections import deque

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    stack = deque([(x, y)])
    a = 0
    while stack:
        x, y = stack.pop()
        if graph[x][y] == 1:
            a += 1
            graph[x][y] = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                
                if graph[nx][ny] == 0:
                    continue
                
                if graph[nx][ny] == 1:
                    stack.append((nx, ny))
    return a

arr = []
result = 0
for i in range(n):
    for j in range(n):
        a = dfs(i, j)
        if a:
            arr.append(a)
            result += 1
print(result)
for i in sorted(arr):
    print(i)
    
    
    
# n = int(input())
# graph = []
# num = []

# for i in range(n):
#     graph.append(list(map(int, input())))

# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]


# def DFS(x, y):
#     if x < 0 or x >= n or y < 0 or y >= n:
#         return False

#     if graph[x][y] == 1:
#         global count
#         count += 1
#         graph[x][y] = 0
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             DFS(nx, ny)
#         return True
#     return False


# count = 0
# result = 0

# for i in range(n):
#     for j in range(n):
#         if DFS(i, j) == True:
#             num.append(count)
#             result += 1
#             count = 0

# num.sort()
# print(result)
# for i in range(len(num)):
#     print(num[i])