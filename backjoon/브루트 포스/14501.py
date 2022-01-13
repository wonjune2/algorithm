import sys
n = int(input())
arr = []
res = []
for i in range(n):
    arr.append(tuple(map(int, sys.stdin.readline().split())))
for i in range(n):
    count = 0
    val = 0
    while True:
        a, b = arr[i]
        i += a
        if i >= n:
            break
        count += 1
        val += b
    res.append((count, val))
print(max(res[1]))