def solution(s):
    answer = 0
    stack = []
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
        elif stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    if stack:
        return 0
    return 1

s = 'baabaa'
print(solution(s))
# stack = []

# for i in range(len(s)):
#     if not stack:
#         stack.append(s[i])
#     elif stack[-1] == s[i]:
#         stack.pop()
#     else:
#         stack.append(s[i])

# print(stack)

        
