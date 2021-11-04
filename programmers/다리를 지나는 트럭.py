from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    length = len(truck_weights)
    queue = deque(truck_weights)
    bridge_crossing = deque([])
    time = deque([])
    bridge_crossed = deque([])
    now = 0
    while len(bridge_crossed) < length:
        answer += 1
        for i in range(len(bridge_crossing)):
            time[i] += 1
        
        if len(bridge_crossing) > 0:
            if time[0] > bridge_length:
                now -= bridge_crossing[0]
                bridge_crossed.append(bridge_crossing.popleft())
                time.popleft()
        
        if len(queue) > 0:
            if now + queue[0] <= weight:
                now += queue[0]
                bridge_crossing.append(queue.popleft())
                time.append(1)
    print(answer)
    return answer

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
solution(bridge_length, weight, truck_weights)
# length = len(truck_weights)
# queue = deque(truck_weights)
# bridge_crossing = deque([])
# time = deque([])
# bridge_crossed = deque([])
# now = 0
# print(length, len(bridge_crossed))
# while len(bridge_crossed) < length:
#     answer += 1
#     for i in range(len(bridge_crossing)):
#         time[i] += 1
    
#     if len(bridge_crossing) > 0:
#         if time[0] > bridge_length:
#             now -= bridge_crossing[0]
#             bridge_crossed.append(bridge_crossing.popleft())
#             time.popleft()
    
#     if len(queue) > 0:
#         if now + queue[0] <= weight:
#             now += queue[0]
#             bridge_crossing.append(queue.popleft())
#             time.append(1)
# print(answer)
    # if len(queue) > 0:
    #     if now + queue[0] <= weight:
    #         now += queue[0]
    #         bridge_crossing.append(queue.popleft())
    #         time.append(0)
    # for i in range(len(bridge_crossing)):
    #     time[i] += 1
    # if time[0] > bridge_length:
    #     now -= bridge_crossing[0]
    #     bridge_crossed.append(bridge_crossing.popleft())
    #     time.popleft()
    # total += 1