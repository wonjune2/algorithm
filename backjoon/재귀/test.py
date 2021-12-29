from collections import Counter
v = [[1,4], [3,4], [3, 10]]
v1 = [[1,1], [2,2], [1, 2]]
x = Counter([v[0][0], v[1][0], v[2][0]]).most_common()
y = Counter([v[0][1], v[1][1], v[2][1]]).most_common()
print(x[1][0])