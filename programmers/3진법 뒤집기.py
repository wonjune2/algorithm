def solution(n):
    answer = 0
    res = ''
    while n > 0:
        res += str(n % 3)
        n = n // 3
    res = res[::-1]
    for i in range(len(res)):
        if int(res[i]) > 0:
            answer += int(res[i]) * (3**i)
    print(answer)
    return answer

solution(45)
