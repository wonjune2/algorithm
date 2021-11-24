from collections import defaultdict
def solution(strings, n):
    answer = []
    dic = defaultdict(list)
    for i in strings:
        dic[i[n]] += [i]

    for i in sorted(dic.keys()):
        answer += sorted(dic[i])
    print(answer)
    return answer

strings = ["qad", "sun", "bed", "afe", "car"]
n = 1
solution(strings, n)