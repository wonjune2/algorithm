import sys
case = 0
while True:
    L, P, V = map(int, sys.stdin.readline().split())
    if L == 0 and P == 0 and V == 0:
        break;
    res = 0
    case += 1
    res += (V // P) * L
    res += V % P if V % P < L else L
    print("Case "+str(case)+":", res)