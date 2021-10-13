# N = 11 + 1
# prime = [True] * N
# for i in range(2, int(N**0.5)+1):
#     if prime[i]:
#         for j in range(i+i, N, i):
#             print(j)
#             prime[j] = False

# for i in range(N):
#     print(f"{i} = {prime[i]}")

from itertools import combinations

def primeNumber(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    else:
        return True

def solution(nums):
    answer = 0
    for i in list(combinations(nums, 3)):
        if sum(i) % 2 == 0:
            continue
        if primeNumber(sum(i)):
            answer += 1
    print(answer)
    return answer

nums = [1,2,7,6,4]
solution(nums)