import sys
n, m = map(int, input().split())
res = []
array = []
for i in range(n):
    array.append(list(sys.stdin.readline().rstrip()))

for i in range(n-7):
    for j in range(m-7):
        w = 0
        b = 0
        for e in range(i, i + 8):
            for q in range(j, j + 8):
                if (e + q) % 2 == 0:
                    if array[e][q] != 'W': w += 1
                    if array[e][q] != 'B': b += 1
                else:
                    if array[e][q] != 'B' : w += 1
                    if array[e][q] != 'W' : b += 1
        
        res.append(w)
        res.append(b)
print(min(res))