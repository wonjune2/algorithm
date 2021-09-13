a = input().upper()
max_num = 0
e = ""

for i in a:
    if max_num < a.count(i):
        max_num = a.count(i)
        a = a.replace(i, "")
        e = i
    elif max_num == a.count(i):
        e = "?"
    else:
        a = a.replace(i, "")
print(e)

# 다른 풀이
# s=input().lower()
# s_list=list(set(s))
# cnt=[]
# for i in s_list:
#     count = s.count(i)
#     cnt.append(count)
# if cnt.count(max(cnt)) >=2:
#     print("?")
# else:
#     print(s_list[(cnt.index(max(cnt)))].upper())