T = int(input())

for _ in range(T):
    x, y = map(int,input().split())
    distance = y - x
    N = int(distance ** 0.5)
    Z = N + 1
    if N == 1:
        print(distance)
    elif distance >= N * Z + 1:
        print(N * 2 + 1)
    elif distance >= (N ** 2) + 1:
        print(N*2)
    else :
        print(N * 2 -1)