def solution(n):
    answer = 0
    array = [True for i in range(n+1)]
    for i in range(2, int(n ** 0.5) + 1):
        if array[i] == True:
            for j in range(i+i, n+1, i):
                array[j] = False
    return array[2:n+1].count(True)