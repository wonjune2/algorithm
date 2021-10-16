def solution(n, lost, reserve):
    answer = n
    lost.sort()
    reserve.sort()
    _reserve = [i for i in reserve if i not in lost]
    _lost = [i for i in lost if i not in reserve]
    for i in _reserve:
        f = i - 1
        b = i + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)

    answer -= len(_lost)
    return answer

n = 5
lost = [2, 4]
reserve = [1, 3, 5]
solution(n, lost, reserve)