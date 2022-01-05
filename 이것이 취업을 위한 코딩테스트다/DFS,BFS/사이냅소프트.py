n = int(input())
s = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    
# 이동할 방향 정의(오른쪽, 아래만 이동 가능하니 두 가지 경로만 설정)
dx = [1, 0]
dy = [0, 1]

print('==============출력 결과========')
for x in range(n):
    for y in range(n):
        for i in range(2): # 오른쪽, 아래로 이동할 경우 2가지 반복
            first = [graph[x][y]] # 시작 위치 및 첫번째 방향 값 저장할 배열
            # 첫 번째로 이동할 경로 설정
            nx = x
            ny = y
            while sum(first) < s:
                second = [] # 두번째 방향 값 저장할 배열
                # 첫 번째 방향 크기 증가
                nx += dx[i]
                ny += dy[i]
                
                # 범위를 벗어나면 break
                if nx >= n or ny >= n:
                    break
    
                first.append(graph[nx][ny]) # 첫 번째 방향 이동한 값 저장
                
                # 첫 번째 방향으로 주어진(S)값이랑 크거나 같으면 break
                if sum(first) == s:
                    for r in first:
                        print(r, end=" ")
                    break
                elif sum(first) > s:
                    break
                
                # 현재 위치로 부터 두번째 방향 설정
                lx = nx
                ly = ny
                # (첫 번째 방향 + 두 번째 방향) 크기가 주어진 값보다 적으면 반복문 진행
                while sum(first) + sum(second) < s:
                    # 첫번째 방향이랑 반대 되도록 증가
                    lx += dx[(i + 1) % 2]
                    ly += dy[(i + 1) % 2]
                    
                    # 범위를 벗어나면 break
                    if lx >= n or ly >= n:
                        break
                    
                    second.append(graph[lx][ly]) # 두 번째 방향 이동한 값 저장
                    
                    # (첫 번째 방향 + 두 번째 방향)으로 주어진(S)값이랑 크거나 같으면 break
                    if sum(first) + sum(second) == s:
                        first.extend(second)
                        for r in first:
                            print(r, end=" ")
                        print()
                        break
                    elif sum(first) + sum(second) > s:
                        break