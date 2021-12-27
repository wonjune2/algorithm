import sys
n = int(input())
array = []
for i in range(n):
    array.append(int(sys.stdin.readline()))

array.sort()    
for i in array:
    print(i)