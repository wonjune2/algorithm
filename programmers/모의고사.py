def solution(answers):
    answer = []
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    res = [0] * 3
    for i in range(len(answers)):
        if answers[i] == one[i % len(one)]:
            res[0] += 1
        if answers[i] == two[i % len(two)]:
            res[1] += 1
        if answers[i] == three[i % len(three)]:
            res[2] += 1
    answer = [i+1 for i, v in enumerate(res) if v == max(res)]
    print(answer)
    return answer

answers = [1,2,3,4,5]
solution(answers)
