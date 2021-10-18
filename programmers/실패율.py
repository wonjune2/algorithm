def solution(N, stages):
    answer = []
    result = []
    k = len(stages)
    for i in range(1, N + 1):
        l = 0
        for j in range(len(stages)):
            if i == stages[j]:
                l += 1
        if l == 0:
            result.append(0)
        else:
            result.append(l / k)
        k = k - l
    ca = sorted(result, reverse=True)

    for i in range(len(ca)):
        answer.append(result.index(ca[i])+1)
        result[result.index(ca[i])] = 2
    print(answer)
    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
solution(N, stages)
