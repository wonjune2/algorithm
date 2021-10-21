def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        budget -= i
        if budget >= 0:
            answer += 1
        else:
            break
    print(answer)
    return answer

d = [1,3,2,5,4]
budget = 9

solution(d, budget)