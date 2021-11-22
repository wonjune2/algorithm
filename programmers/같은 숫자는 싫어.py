def solution(arr):
    answer = []
    c = None
    for i in arr:
        if i != c:
            c = i
            answer.append(i)
    return answer


