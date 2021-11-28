def solution(s, n):
    answer = ''
    for i in s:
        if i.islower():
            answer += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
        elif i.isupper():
            answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
        else:
            answer += ' '
    return answer

s = "a B z"
n = 4
# solution(s, n)
answer = ''
print((ord('z') - ord('a') + n) % 26 + ord('a'))
for i in s:
    if i.islower():
        answer += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
    elif i.isupper():
        answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
    else:
        answer += ' '
print(answer)
