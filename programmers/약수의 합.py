def solution(n):
    answer = 0
    print(int(n ** 0.5) + 1)
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if n // i != i:
                answer += i + (n // i)
            else:
                answer += i
    return answer