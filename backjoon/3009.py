x = [None] * 3
y = [None] * 3
for i in range(3):
    a, b = map(int,input().split())
    x[i] = a
    y[i] = b
xx = 0
yy = 0
for i in range(3):
    if x.count(x[i]) == 1: xx = x[i]
    if y.count(y[i]) == 1: yy = y[i]
print(xx, yy)