def solution(s):
    match = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in range(len(match)):
        s = s.replace(match[i], str(i))
    s = int(s)
    return s

