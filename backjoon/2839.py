n = int(input())

x = n // 5
if n % 5 >= 3:
    a = (n % 5)
    x += a // 3
    x += a % 3
else :
    x += n % 5
if n == 4 or n == 7:
    print(-1)
else:
    print(x)

# sugar = int(input())

# bag = 0

# while sugar >= 0 :
#     if sugar % 5 == 0 :  # 5의 배수이면
#         bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
#         print(bag)
#         break
#     sugar -= 3  
#     bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1