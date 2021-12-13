n, m = map(int, input().split())

cards = [[] for i in range(n)]
result = 0

for i in range(n):
    cards[i] = list(map(int, input().split()))
    m = min(cards[i])
    if result < m:
        result = m
        
print(result)