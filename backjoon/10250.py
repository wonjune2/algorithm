import math
C = int(input())

for _ in range(C):
    H, W, N = map(int,input().split())

    f = ((N - 1) % H) + 1
    r = math.ceil(N / H)
    print(f * 100 + r)