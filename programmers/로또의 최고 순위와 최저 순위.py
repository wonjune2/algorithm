# lottos : 민우가 구매한 로또 번호
# win_nums : 당첨번호
def solution(lottos, win_nums):
    zero = lottos.count(0)
    while 0 in lottos:
        lottos.remove(0)
    c = 0
    for i in win_nums:
        for j in lottos:
            if i == j:
                c += 1
                break
    maxnum = 7 - (c + zero)
    minnum = 7 - c
    if maxnum == 7:
        maxnum = 6
    if minnum == 7:
        minnum = 6
    answer = [maxnum, minnum]
    return answer
