C = int(input())

N = map(int,input().split())
count = 0
for i in N:
    if i == 1 :
        continue
    for e in range(2, i):
        if i % e == 0:
            break
    else:
        count += 1
print(count)