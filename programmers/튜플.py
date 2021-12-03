from collections import defaultdict
def solution(s):
    s = s.replace("{", "")
    s = s.replace("}", "")
    s = s.split(",")
    dic = defaultdict(int)
    for i in s:
        dic[int(i)] += 1

    a = sorted(dic.items(), reverse=True, key=lambda x: x[1])
    return list(i for i, v in a)

s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
print(solution(s))

