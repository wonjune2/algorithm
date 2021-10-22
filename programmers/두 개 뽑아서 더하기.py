def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            print(numbers[i], numbers[j], end=' ')
            answer.append(numbers[i] + numbers[j])
    answer = list(set(answer))
    answer.sort()
    print(answer)
    return answer

numbers = [5,0,2,7]
solution(numbers)

