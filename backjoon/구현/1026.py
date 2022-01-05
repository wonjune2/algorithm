n = int(input())
res = 0
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)
for i in range(n):
    res += A[i] * B[i]
    
print(res)