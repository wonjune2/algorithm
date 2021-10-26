def solution(phone_book):
    answer = True
    phone_book.sort()
    print(phone_book)
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            answer = False
            break
    print(answer)
    return answer

phone_book = ["119", "97674223", "1195524421"]
solution(phone_book)