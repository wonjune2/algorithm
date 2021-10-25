from itertools import combinations

def solution(nums):
    answer = 0
    res = list(combinations(nums, 3))
    for i in res:
        num = sum(i)
        for j in range(2, int(num**0.5)+1):
            if num % j == 0:
                break
        else:
            answer += 1
    print(answer)
    return answer

nums = [1,2,7,6,4]

solution(nums)