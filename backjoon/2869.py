A, B, V = map(int,input().split()) 

res = (V - B - 1) // (A - B) + 1
print(res)