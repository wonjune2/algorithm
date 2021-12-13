n, m, k = map(int, input().split())
array = list(map(int, input().split()))

array.sort(reverse=True)
first = array[0]
second = array[1]

count = (m // (k + 1)) * k
count += m % (k + 1)

result = 0
result += first * count
result += second * (m - count)

print(result) 