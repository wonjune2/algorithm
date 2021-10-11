def solution(numbers):
    answer = 0
    add = []
    for i in range(10):
        if i in numbers:
            pass
        else:
            answer += i
    return answer

num = [1,2,3,4,6,7,8,0]
solution(num)