n = int(input())
road = list(map(int, input().split()))
cost = list(map(int, input().split()))
now = cost[0]
total = 0
for i in range(len(road)):
    now = min(now, cost[i])
    total += now * road[i]

print(total)