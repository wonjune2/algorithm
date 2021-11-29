def solution(s):
    answer = ''
    return answer

s = "try hello world"
answer = ''
n = 0
for i in range(len(s)):
    if s[i].isspace():
        answer += ' '
        n = 0
    else:
        if n % 2 == 0:
            answer += s[i].upper()
            n += 1
        else:
            answer += s[i].lower()
            n += 1
print(answer)