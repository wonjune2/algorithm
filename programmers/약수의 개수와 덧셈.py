def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        c = 0
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                c += 1
                if j ** 2 != i:
                    c += 1
        if c % 2 == 0:
            answer += i
        else:
            answer -= i
    print(answer)
    return answer

n = 100
for j in range(1, int(n**0.5) + 1):
    if n % j == 0:
        print(j)
        if j ** 2 != n:
            print(n // j)