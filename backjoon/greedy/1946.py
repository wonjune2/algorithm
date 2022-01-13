import sys
t = int(input())

for i in range(t):
    n = int(input())
    arr = []
    for j in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))

    arr.sort()
    m = arr[0][1]
    c = 1
    for _, b in arr:
        if b < m:
            m = b
            c += 1
    print(c)
            