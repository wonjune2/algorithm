# def solution(arr):
#     answer = []
#     c = None
#     for i in arr:
#         if i != c:
#             c = i
#             answer.append(i)
#     return answer

# arr = [1,1,3,3,0,1,1]
# answer = []
# c = None
# for i in arr:
#     if i != c:
#         c = i
#         answer.append(i)
# print(answer)

def no_continuous(s):
    a = []
    for i in s:
        print(a[-1:], [i])
        if a[-1:] == [i]: continue
        a.append(i)
    return a

s = [1,1,3,3,0,1,1]
no_continuous(s)