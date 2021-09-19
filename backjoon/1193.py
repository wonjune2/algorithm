n = int(input())

total = 1
cnt = 1
while total < n:
    cnt += 1
    total += cnt

if cnt % 2 == 0:
    print(f'{cnt - (total - n)}/{1 + total - n}')
else:
    print(f'{1 + total - n}/{cnt - (total - n)}')