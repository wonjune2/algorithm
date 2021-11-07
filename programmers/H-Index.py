def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0

citations = [3, 0, 6, 1, 5]
# solution(citations)
citations = sorted(citations)
l = len(citations)
print(l)
for i in range(l):
    print(citations[i])
    if citations[i] >= l-i:
        break
# citations.sort()
# answer = 0
# for i in range(len(citations)):
#     c = 0
#     for j in range(i, len(citations)):
#         if citations[i] <= citations[j]:
#             c += 1
#     if citations[i] <= c >= len(citations) - c:
#         answer = citations[i]
# print(answer)