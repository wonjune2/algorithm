t = int(input())

for i in range(t):
    d = [0] * 100
    d[1] = 1
    d[2] = 2
    d[3] = 4
    n = int(input())
    for j in range(4, n + 1):
        d[j] = d[j - 1] + d[j - 2] + d[j - 3]
    
    print(d[n])