from collections import Counter
import sys
n = int(input())
arr = []
for i in range(n):
    a = int(sys.stdin.readline())
    arr.append(a)
arr.sort()

count = Counter(arr).most_common()
print(round(sum(arr) / n))
print(arr[(len(arr) // 2)])
if len(count) > 1 and count[0][1] == count[1][1]:
    print(count[1][0])
else:
    print(count[0][0])
print(arr[-1] - arr[0])