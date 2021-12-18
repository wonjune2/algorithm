n, k = map(int, input().split())
coins = [0] * n
result = 0
for i in range(n-1, -1, -1):
    coins[i] = int(input())

while k != 0:
    for i in coins:
        if k >= i:
            result += k // i
            k %= i
            
print(result)