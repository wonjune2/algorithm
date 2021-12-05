n = int(input())
answer = 0
for i in range(1, n):
    answer = i + sum(list(map(int,str(i))))
    if answer == n:
        print(i)
        break
else:
    print(0)