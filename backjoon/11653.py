n = int(input())
c = 3

while n > 1:
    if n % 2 == 0:
        n = n // 2
        print(2)
    elif n % c == 0:
        n = n // c
        print(c)
    else:
        c += 2