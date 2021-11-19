def solution(price, money, count):
    price = price * count * (count + 1) // 2
    answer = price - money
    if answer < 0:
        answer = 0
    return answer