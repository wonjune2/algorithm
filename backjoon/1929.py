M, N = map(int,input().split())
prime = []
prime.append(2)

for n in range(3, N+1, 2):
    i = 0
    while prime[i] * prime[i] <= n:
        if n % prime[i] == 0:
            break
        i += 1
    else:
        prime.append(n)

for i in range(len(prime)):
    if prime[i] >= M:
        print(prime[i])