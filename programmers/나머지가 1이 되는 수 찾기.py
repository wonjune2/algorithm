def solution(n):
    answer = n - 1
    for i in range(2, int(n**0.5) + 1):
        if answer % i == 0:
            answer = i
            break
    print(answer)
    return answer

solution(10)