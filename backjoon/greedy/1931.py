n = int(input())
count = 0

array = []
for _ in range(n):
    array.append(tuple(map(int, input().split())))

array = sorted(array, key=lambda a: a[0])
array = sorted(array, key=lambda a: a[1])

focus = 0
for x, y in array:
    if focus <= x:
        focus = y
        count += 1
        
print(count)