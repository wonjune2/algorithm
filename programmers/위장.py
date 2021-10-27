def solution(clothes):
    answer = 1
    val = {}
    for i in clothes:
        if i[1] in val: val[i[1]] += 1
        else: val[i[1]] = 1
    for i in val.values():
        answer *= (i + 1)
    print(answer - 1)
    return answer - 1

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
solution(clothes)