def solution(name):
    answer = 0
    a = 65
    count = 0
    for i in range(len(name)):
        # if i < len(name) and 
        s = ord(name[i]) - ord('A')
        z = abs(ord(name[i]) - ord('Z')) + 1
        if s < z:
            count += s
        else:
            count += z
        print(count)
    return answer

name = "JEROEN"
solution(name)