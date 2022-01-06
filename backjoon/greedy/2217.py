n = int(input())
rope = []
for i in range(n):
    rope.append(int(input()))

rope.sort()
for i in range(n):
    rope[i] = rope[i] * (len(rope) - i)

print(max(rope))