list09 = list(range(7))
list10 = list(range(3,8))
list11 = list(range(3,13,2))
list12 = [None] * 5

# tuple
tuple01 = ()
tuple02 = 1,
tuple03 = (1,)
tuple04 = 1,2,3
tuple05 = 1,2,3,
tuple06 = (1,2,3)
tuple07 = (1,2,3,)
tuple08 = 'A', 'B', 'C'

tuple09 = tuple()
tuple10 = tuple('ABC')
tuple11 = tuple([1,2,3])
tuple12 = tuple({1,2,3})

tuple13 = tuple(range(7))
tuple14 = tuple(range(3,8))
tuple15 = tuple(range(3, 13, 2))

x = [1, 2, 3]
a, b, c = x
print(a, b, c)

x = [11,22,33,44,55,66,77]
x[2]
x[-3]
x[-4] = 3.14 # x[-4]는 float 3.14로 변환
x
# x[7] 인덱스 범위 벗어남
# x[7] = 3.14 인덱스가 존재하지 않으니 에러

# slice

s = [11,22,33,44,55,66,77]
s[0:6]
s[0:7]
s[0:7:2]
s[-4:-2]
s[3:1] # 오류 안남
