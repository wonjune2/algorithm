def max3(a,b,c) :
    """a,b,c의 최대값을 구하여 반환"""
    maximum = a
    if b > maximum: maximum = b
    if c > maximum: maximum = c
    return maximum # 최댓값 반환

print(f'max3(a, b, c) = {max3(3, 2, 1)}')
print(f'max3(a, b, c) = {max3(3, 2, 2)}')
print(f'max3(a, b, c) = {max3(3, 1, 2)}')
print(f'max3(a, b, c) = {max3(3, 2, 3)}')
print(f'max3(a, b, c) = {max3(2, 1, 3)}')
print(f'max3(a, b, c) = {max3(3, 3, 2)}')
print(f'max3(a, b, c) = {max3(3, 3, 3)}')
print(f'max3(a, b, c) = {max3(2, 2, 3)}')
print(f'max3(a, b, c) = {max3(2, 3, 1)}')
print(f'max3(a, b, c) = {max3(2, 3, 2)}')
print(f'max3(a, b, c) = {max3(1, 3, 2)}')
print(f'max3(a, b, c) = {max3(2, 3, 3)}')
print(f'max3(a, b, c) = {max3(1, 2, 3)}')