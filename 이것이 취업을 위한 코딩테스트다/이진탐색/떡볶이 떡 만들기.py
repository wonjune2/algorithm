import sys
def binary_search(array, target, start, end, c):
    while start <= end:
        mm = 0
        mid = (start + end) // 2
        cut = array[mid]
        for i in c:
            if i > cut: mm += i - cut
        
        if mm > target:
            start = mid + 1
        elif mm < target:
            end = mid - 1
        else:
            return mid
        
n, m = map(int, input().split())
c = list(map(int, input().split()))
array = [i for i in range(max(c) + 1)]
# print(array)
result = binary_search(array, m, 0, len(array) - 1, c)
print(result)
        