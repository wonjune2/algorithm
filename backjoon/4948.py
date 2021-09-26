# max = 123456 * 2
# prime = [False] * (max + 1)
# prime[2] = True
# for i in range(3, max+1, 2):
#     for j in range(3, int(i**0.5)+1, 2):
#         if i % j == 0:
#             break
#     else:
#         prime[i] = True

# while True:
#     n = int(input())
#     if n == 0:
#         break
#     print(prime[n+1:n*2+1].count(True))

N = 11 + 1
prime = [True] * N
for i in range(2, int(N**0.5)+1):
    if prime[i]:
        for j in range(i+i, N, i):
            print(j)
            prime[j] = False

for i in range(N):
    print(f"{i} = {prime[i]}")