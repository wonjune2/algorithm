from itertools import permutations
def solution(numbers):
    answer = 0
    n = sorted(numbers, reverse=True)
    m = int("".join(n))
    array = [True] * (m + 1)
    array[0] = False
    array[1] = False
    for i in range(2, int(m ** 0.5) + 1):
        if array[i] == True:
            for j in range(i+i, m + 1, i):
                array[j] = False
    per = []
    for i in range(1, len(n) + 1):
        per.extend(list(permutations(n, r=i)))
    print(per)
    for i in per:
        c = int("".join(i))
        if array[c]:
            answer += 1
            array[c] = False
    return answer

numbers = "011"
print(solution(numbers))