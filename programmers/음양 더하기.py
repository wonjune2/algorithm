def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    print(answer)
    return answer

abos = [4,7,12]
sig = [True,False,True]
solution(abos, sig)