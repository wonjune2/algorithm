import heapq
n = int(input())

heap = [int(input()) for _ in range(n)]
heapq.heapify(heap)
res = 0
if len(heap) == 0:
    print(0)
else:
    while len(heap) > 1:
        num1 = heapq.heappop(heap)
        num2 = heapq.heappop(heap)
        res += num1 + num2
        heapq.heappush(heap, num1 + num2)
    
    print(res)