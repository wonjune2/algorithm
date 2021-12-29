from collections import Counter
def solution(phone_book):
    hash_map = {}
    for i in phone_book:
        hash_map[i] = 1
        
    for i in phone_book:
        number = ""
        for j in i:
            number += j
            if number in hash_map and number != i:
                return False

    return True



phone_book = ["119", "97674223", "1195524421"]

