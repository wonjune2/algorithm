import sys
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
        else:
            return mid

n = int(input())
array = list(map(int, sys.stdin.readline().split()))
array.sort()
m = int(input())
mar = list(map(int, sys.stdin.readline().split()))

for i in mar:
    res = binary_search(array, i, 0, n - 1)
    if res:
        print('Yes', end=" ")
    else:
        print('No', end=" ")