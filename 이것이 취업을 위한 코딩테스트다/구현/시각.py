h = int(input())
c = 0
for i in range(h+1):
    for j in range(60):
        for e in range(60):
            if '3' in str(i) + str(j) + str(e):
                c += 1
print(c)