p = "()))((()"

def uv(w):
    left = 0
    right = 0
    for i in range(len(w)):
        if w[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return w[:i+1], w[i+1:]
def check(u):
    stack = []

    for i in u:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()

    return True

def solution(p):
    if not p:
        return ""

    u, v = uv(p)

    if check(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        for i in u[1:len(u) - 1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('
        return answer
print(solution(p))