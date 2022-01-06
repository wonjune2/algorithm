import re
s = input()
num = re.findall('[-]|\d+', s)
res = 0
l = 1 # 부호
for i in range(len(num)):
    if num[i] == '-':
        l = -1
    else:
        res += (int(num[i]) * l)
print(res)
