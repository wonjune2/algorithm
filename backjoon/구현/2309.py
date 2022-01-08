from itertools import combinations
array = []
for i in range(9):
    array.append(int(input()))

res = combinations(array, 7)

for i in res:
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break