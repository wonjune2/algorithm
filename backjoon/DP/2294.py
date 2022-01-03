n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

d = [10001] * (k + 1)
d[0] = 0

for i in range(n):
    for j in range(coins[i], k + 1):
        if d[j  - coins[i]] != 10001:
            d[j] = min(d[j], d[j - coins[i]] + 1)
            
if d[k] == 10001:
    print(-1)            
else:
    print(d[k])