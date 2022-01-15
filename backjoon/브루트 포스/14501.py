import sys
n = int(input())
arr = []
dp = [0] * (n + 1)
for i in range(n):
    arr.append(tuple(map(int, sys.stdin.readline().split())))

for i in range(n-1, -1, -1):
    if arr[i][0] + i > n: dp[i] = dp[i+1]
    else: dp[i] = max(dp[i + 1], arr[i][1] + dp[i + arr[i][0]])

print(dp[0])