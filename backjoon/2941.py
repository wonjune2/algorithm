c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
sum = 0
for i in c:
    s = s.replace(i, " ")
sum += len(s)
print(sum)