def solution(arr, divisor):
    answer = []
    arr.sort()
    for i in arr:
        if i % divisor != 0: continue
        answer.append(i)
    print(answer)
    return answer

arr = [5, 9, 7, 10]
divisor = 5
solution(arr, divisor)