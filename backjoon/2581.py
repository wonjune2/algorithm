M = int(input())
N = int(input())
sum = 0
prime_num = []
for i in range(M, N+1):
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime_num.append(i)
        sum += i
if sum > 0:
    print(f'{sum}\n{prime_num[0]}')
else:
    print(-1)