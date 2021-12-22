e, s, m = map(int, input().split())

a = 0
b = 0
c = 0
count = 0

while a != e or b != s or c != m:
    a = ((a + 1 - 1) % 15) + 1
    b = ((b + 1 - 1) % 28) + 1
    c = ((c + 1 - 1) % 19) + 1
    count += 1

print(count)
