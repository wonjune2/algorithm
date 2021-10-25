def solution(lottos, win_nums):
    answer = []
    lst = [6,6,5,4,3,2,1]
    z = lottos.count(0)
    c = 0
    for i in lottos:
        if i in win_nums:
            c += 1
    answer = [lst[c+z],lst[c]]
    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
solution(lottos, win_nums)