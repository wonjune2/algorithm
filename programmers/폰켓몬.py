def solution(nums):
    answer = 0
    length = len(nums) // 2
    unique = set(nums)
    if len(unique) < length:
        answer = len(unique)
    else:
        answer = length
    return answer

nums = [3,3,3,2,2,2]
solution(nums)