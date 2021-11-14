from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for i in course:
        temp = []
        for order in orders:
            temp += combinations(sorted(order), i)
        counter = Counter(temp)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]
    return sorted(answer)
orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
print(solution(orders, course))