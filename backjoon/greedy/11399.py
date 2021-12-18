n = int(input())
array = list(map(int, input().split()))
array.sort()
result = array[0]
for i in range(1, len(array)):
    for j in range(i + 1):
        result += array[j]

print(result)