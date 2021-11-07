def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0

citations = [3, 0, 6, 1, 5]
print(solution(citations))