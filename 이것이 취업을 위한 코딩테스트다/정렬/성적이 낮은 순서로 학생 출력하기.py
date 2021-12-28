n = int(input())

array = []
for i in range(n):
    a, b = input().split()
    array.append((a, int(b)))

print(sorted(array, key=lambda a: a[1]))
