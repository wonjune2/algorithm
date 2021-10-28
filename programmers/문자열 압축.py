def solution(s):
    answer = 0
    return answer

s = "abcabcabcdededededede"
res = []
dic = {}
for j in range(i, len(s), i): 
    if tmp==s[j:i+j]: 
        cnt+=1 
    else: 
        if cnt!=1: 
            b = b + str(cnt)+tmp 
        else: 
            b = b + tmp 
            tmp=s[j:j+i] 
            cnt = 1


