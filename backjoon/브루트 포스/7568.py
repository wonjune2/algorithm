n = int(input())
men = []
for i in range(n):
    x, y = map(int, input().split())
    men.append([x, y])

for i in men:
    k = 1
    for j in men:
        if i[0] < j[0] and i[1] < j[1]:
            k += 1
    print(k, end=" ")