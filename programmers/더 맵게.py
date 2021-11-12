import heapq
scoville = [1, 2, 3]
k = 11
heapq.heapify(scoville)
c = 0
while len(scoville) > 1 and scoville[0] < k:
    m1 = heapq.heappop(scoville)
    m2 = heapq.heappop(scoville)
    print(m1, m2)
    new = m1 + (m2 * 2)
    heapq.heappush(scoville, new)
    c += 1
if scoville[0] < k:
    c = -1
print(c)
