def solution(scoville, K):
    scoville.sort()
    answer = 0
    while scoville[0] < K:
        m1 = scoville.pop(0)
        m2 = scoville.pop(0)
        mix = m1 + (m2 * 2)
        if mix > m1:
            scoville.append(mix)
            scoville.sort()
        else:
            answer = -1
            break
        answer += 1
    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))
# answer = 0
# while scoville[0] < K:
#     m1 = scoville.pop(0)
#     m2 = scoville.pop(0)
#     mix = m1 + (m2 * 2)
#     if mix > m1:
#         scoville.append(mix)
#         scoville.sort()
#     else:
#         answer = -1
#         break
#     answer += 1
# print(answer)

