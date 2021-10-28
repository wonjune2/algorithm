s = "ababcdcdababcdcd"

def solution(s):
    answer = []
    if len(s) > 1:
        for i in range(1, len(s) // 2 + 1,):
            cnt = 1
            b = ''
            temp = s[:i]
            for j in range(i, len(s), i):
                if temp == s[j:i+j]:
                    cnt += 1
                else:
                    if cnt > 1:
                        b += str(cnt) + temp
                    else:
                        b += temp
                    temp = s[j:i+j]
                    cnt = 1
            if cnt > 1:
                b += str(cnt) + temp
            else:
                b += temp
            answer.append(len(b))
        
        return min(answer)
    else:
        return 1
    
print(solution(s))



