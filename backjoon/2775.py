T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    lst = [num for num in range(1, n+1)]
    for j in range(k):
        for e in range(1, n):
            lst[e] += lst[e - 1]
    print(lst[-1])
