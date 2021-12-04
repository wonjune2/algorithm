from itertools import combinations
n, m = map(int, input().split())
array = list(map(int, input().split()))
array2 = list(combinations(array, 3))
mi = 0
for i in array2:
    b = sum(i)
    if b == m:
        mi = b
        break
    elif b < m:
        if mi < b:
            mi = b
    else:
        continue
print(mi)