from collections import deque

def solution(priorities, location):
    num = []
    queue = deque(priorities)
    lqueue = deque([i for i in range(len(priorities))])
    while len(queue) > 0:
        m = max(queue)
        c = queue[0]
        if c >= m:
            queue.popleft()
            num.append(lqueue.popleft())
        else:
            queue.append(queue.popleft())
            lqueue.append(lqueue.popleft())
    return num.index(location) + 1

priorities = [2, 1, 3, 2]
location = 2
solution(priorities, location)

