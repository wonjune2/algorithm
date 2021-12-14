n, k = map(int, input().split())
result = 0
# n 25, k 3
while True:
    target = (n // k) * k
    result += (n - target)
    
    n = target
    print(n)
    if n < k:
        break
    result += 1
    n //= k

result += n - 1
print(result)