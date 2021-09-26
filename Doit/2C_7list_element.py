# 자료형을 정하지 않은 리스트 원소 확인하기

x = [[1,2,3],[4,5,6]]
y = x.copy()
x[0][1] = 9
print(x)
print(y) # 얕은 복사

import copy
x = [[1,2,3],[4,5,6]]
y = copy.deepcopy(x) # 깊은 복사 
x[0][1] = 9
print(x)
print(y)