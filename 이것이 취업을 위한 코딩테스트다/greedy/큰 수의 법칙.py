n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
result = 0
c = 0
numbers.sort(reverse=True)
print(numbers)
for i in range(m):
    if c < k:
        result += numbers[0]
        c += 1
    else:
        result += numbers[1]
        c = 0
    
print(result)