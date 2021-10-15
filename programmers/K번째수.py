def solution(array, commands):
    answer = []
    for c in commands:
        i, j, k = c
        lst = array[i-1:j]
        lst.sort()
        answer.append(lst[k-1])
    return answer

commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
array = [1, 5, 2, 6, 3, 7, 4]

print(solution(array, commands))
