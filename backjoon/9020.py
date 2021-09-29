M = 10001
prime = [i for i in range(M)]
for i in range(2, int(M**0.5)+1):
    if prime[i]:
        for j in range(i+i, M, i):
            prime[j] = 0

T = int(input())
for _ in range(T):
    n = int(input())
    a = n // 2
    b = a
    while True:
        if prime[a] and prime[b]:
            print(a, b)
            break
        a -= 1
        b += 1