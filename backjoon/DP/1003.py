t = int(input())

for i in range(t):
    d = [(0, 0)] * 41
    d[0] = (1, 0)
    d[1] = (0, 1)
    n = int(input())
    for j in range(2, n + 1):
        x = d[j - 1][0] + d[j - 2][0]
        y = d[j - 1][1] + d[j - 2][1]
        d[j] = (x, y)
    
    print(d[n][0], d[n][1])