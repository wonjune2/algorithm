from itertools import permutations
from collections import Counter
def operation(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    elif op == '-':
        return str(int(num1) - int(num2))
    else:
        return str(int(num1) * int(num2))

def calculate(exp, op):
    array = []
    nums = ''
    for i in exp:
        if i.isdigit():
            nums += i
        else:
            array.append(nums)
            array.append(i)
            nums = ''
    array.append(nums)
    print(array)

    for o in op:
        stack = []
        while len(array) != 0:
            nums = array.pop(0)
            if nums == o:
                stack.append(operation(stack.pop(), array.pop(0), o))
            else:
                stack.append(nums)
        array = stack
    return abs(int(array[0]))

def solution(expression):
    op = ['+', '-', '*']
    op = list(permutations(op, 3))
    result = []
    for i in op:
        result.append(calculate(expression, i))
    return max(result)

expression = "100-200*300-500+20"
print(solution(expression))