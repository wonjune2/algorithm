n = int(input())
sum = 0
for i in range(n):
    s = input()
    sum += 1
    for j in list(set(s)):
        pos = [pos for pos, char in enumerate(s) if char == j]
        if len(pos) != 1:
            if pos[-1] == pos[0] + len(pos) -1:
                pass
            else:
                sum -= 1
                break
print(sum)

# 다른 풀이!
# N = int(input())
# count = N
# for i in range(N):
#     word = input()
#     chr = [word[0]]
#     for j in range(1, len(word)):
#         if word[j] == word[j-1]:
#             pass
#         elif word[j] in chr:
#                 count -= 1
#                 break
#         else:
#             chr.append(word[j])

# print(count)