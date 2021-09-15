b = input()
d = "  ABC DEF GHI JKL MNO PQRS TUV WXYZ"
sum = 0
for i in b:
    c = d[:d.find(i)].count(" ")
    sum += c + 1
print(sum)



