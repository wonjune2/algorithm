n = list(input())

n.sort(reverse=True)
res = int(''.join(n))

if res % 30 == 0:
    print(res)
else:
    print(-1)