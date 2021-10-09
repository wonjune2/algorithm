def solution(numbers, hand):
    answer = ''
    left = '*'
    right = '#'
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            left = i
            answer += "L"
        elif i == 3 or i == 6 or i == 9:
            right = i
            answer += "R"
        else:
            line, col = pos(i)
            leftL, leftC = pos(left)
            rightL, rightC = pos(right)
            leftLen = abs(col - leftC) + abs(line - leftL)
            rightLen = abs(col - rightC) + abs(line - rightL)
            if leftLen < rightLen:
                left = i
                answer += 'L'
            elif rightLen < leftLen:
                right = i
                answer += 'R'
            else:
                if hand == 'left':
                    left = i
                    answer += 'L'
                else:
                    right = i
                    answer += 'R'
    return answer

def pos(num):
    if num == 0 or num == '*' or num == '#':
        line = 3
        if num == '*': col = 0
        elif num == 0: col = 1
        else: col = 2
    else:
        line = (num - 1) // 3
        col = (num - 1) % 3
    return line, col

pad = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hands = 'right'

