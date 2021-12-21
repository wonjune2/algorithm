n, k = map(int, input().split())

array = [i for i in range(1, n + 1)]
index = (k - 1) % n
result = []
while True:
    result.append(array[index])
    del array[index]
    index += k - 1
    if len(array) <= 0:
        break
    index = index % len(array)

print('<', end ="")
for i in range(len(result)):
    if i < len(result) - 1:
        print(result[i], end=", ")
    else:
        print(result[i], end="")
print('>')