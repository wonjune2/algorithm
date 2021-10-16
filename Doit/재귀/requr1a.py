# 비재귀적으로 재귀 함수 구현하기(꼬리 재귀를 제거)

def recur(n: int) -> int:
    while n > 0:
        recur(n - 1)
        print(n)
        n = n - 2

x = int(input('숫자를 입력하세요.: '))

recur(x)