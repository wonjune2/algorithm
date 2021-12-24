from collections import deque

def DFS(start):
    stack = deque([start])
    visited = []

    while stack:
        now = stack.pop()
        if now not in visited:
            visited.append(now)
            for v in sorted(graph[now], reverse=True):
                if v not in visited:
                    stack.append(v)
    visited_str = [str(i) for i in visited]
    return ' '.join(visited_str)
            
# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# visited = [False] * 9

# 정의된 DFS 함수 호출
print(DFS(1))