input_data = input()
row = int(input_data[1])
column = ord(input_data[0]) - ord('a') + 1
case = 0
steps = [(-2, -1), ( -1, -2), (1, - 2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]


for i in steps:
    xrow = row + i[1]
    xcol = column + i[0]
    if 8 >= xrow >= 1 and 1 <= xcol <= 8:
        case += 1
print(case)