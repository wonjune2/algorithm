n = 1000 - int(input())

array = [500, 100, 50, 10, 5, 1]
res = 0
for i in array:
    res += n // i
    n = n % i
print(res)
