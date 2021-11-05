def solution(numbers):
    answer = ''
    n = list(map(str, numbers)) 
    n.sort(key=lambda x:x*3, reverse=True)
    answer = str(int(''.join(n)))
    return answer

numbers = [0,0,0,0]
solution(numbers)
# n = list(map(str, numbers)) 
# n.sort(key=lambda x:x*3, reverse=True)
# print(n)

