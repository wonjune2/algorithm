n = input().split()
if n[0][::-1] < n[1][::-1]:
    print(n[1][::-1])
else:
    print(n[0][::-1])