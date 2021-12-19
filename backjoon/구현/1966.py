from collections import deque
c = int(input())

for i in range(c):
    n, m = map(int,input().split())
    queue = deque(map(int, input().split()))
    c = 0
    for j in range(n):
        queue[j] = (queue[j], j)
    # print(queue)
    while True:
        focus = queue.popleft()
        if len(queue) <= 0:
            c += 1
            break
        else:
            if focus[0] >= max(queue)[0]:
                c += 1
                if focus[1] == m:
                    break
            else:
                queue.append(focus)
    print(c)
