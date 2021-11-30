def ff(n):
    if n > 1:
        return ff(n - 1) + ff(n - 2)
    else:
        return n

n = int(input())
print(ff(n))