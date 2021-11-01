def solution(progresses, speeds):
    answer = []
    while len(progresses) > 0:
        c = []
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while len(progresses) > 0 and progresses[0] >= 100:
            c.append(progresses.pop(0))
            speeds.pop(0)
        if len(c) > 0:
            answer.append(len(c))
    print(answer)
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]

solution(progresses, speeds)
# while len(progresses) > 0:
#     c = []
#     for i in range(len(progresses)):
#         progresses[i] += speeds[i]
#     while len(progresses) > 0 and progresses[0] >= 100:
#         progresses.pop(0)
#         speeds.pop(0)
#     if len(c) > 0:
#         answer.append(len(c))
