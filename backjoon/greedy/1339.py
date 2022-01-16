import sys
n = int(input())
arr = [sys.stdin.readline().strip() for i in range(n)]
# arr.sort(key=len, reverse=True)

dic = {}

for i in arr:
    pow_val = len(i) - 1
    for j in i:
        if j in dic:
            dic[j] += pow(10, pow_val)
        else:
            dic[j] = pow(10, pow_val)
        pow_val -= 1
dic = sorted(dic.values(), reverse=True)
m = 9
result = 0
for i in dic:
    result += i * m
    m -= 1
print(result)