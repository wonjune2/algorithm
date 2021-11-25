def solution(s):
    answer = True
    p = 0
    y = 0
    for i in s.lower():
        if i == 'p':
            p += 1
        elif i == 'y':
            y += 1
        else:
            continue
    if p != y:
        answer = False
    return answer