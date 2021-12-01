array = []
def hanoi(n, x, y):
    if n > 1:
        hanoi(n - 1, x, 6 - x - y)
    array.append(str(x) + " " +str(y))
    if n > 1:
        hanoi(n - 1, 6 - x - y, y)

n = int(input())

hanoi(n, 1, 3)
print(len(array))
for i in array:
    print(i)
