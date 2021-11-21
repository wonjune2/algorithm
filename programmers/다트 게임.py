import re
def solution(dartResult):
    answer = 0
    arr = list(re.finditer(r'\d+', dartResult))
    result = [0] * 3
    for i in range(len(arr)):
        if i < 2:
            string = dartResult[arr[i].start():arr[i+1].start()]
        else:
            string = dartResult[arr[i].start():]
        result[i] = int(re.search(r'\d+', string).group())
        al = re.search(r'[A-Z]', string).group()
        if al == 'D':
            result[i] = result[i] ** 2
        elif al == 'T':
            result[i] = result[i] ** 3
        s = re.search(r'\W', string)
        if s is not None:
            if s.group() == '#':
                result[i] = result[i] * (-1)
            elif s.group() == '*':
                result[i] = result[i] * 2
                if i - 1 >= 0:
                    result[i-1] = result[i-1] * 2
    answer = result[0] + result[1] + result[2]
    return answer

dartResult = '1D#2S*3S'
arr = list(re.finditer(r'\d+', dartResult))
result = [0] * 3
for i in range(len(arr)):
    if i < 2:
        string = dartResult[arr[i].start():arr[i+1].start()]
    else:
        string = dartResult[arr[i].start():]
    result[i] = int(re.search(r'\d+', string).group())
    al = re.search(r'[A-Z]', string).group()
    if al == 'D':
        result[i] = result[i] ** 2
    elif al == 'T':
        result[i] = result[i] ** 3
    s = re.search(r'\W', string)
    if s is not None:
        if s.group() == '#':
            result[i] = result[i] * (-1)
        elif s.group() == '*':
            result[i] = result[i] * 2
            if i - 1 >= 0:
                result[i-1] = result[i-1] * 2
print(result[0] + result[1] + result[2])