n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()
res = 0
for i in range(n-1):
    res += res + arr[i]
print(res + res + arr[n - 1])