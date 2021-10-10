def pocket(poc, val):
    if len(poc) < 1:
        poc.append(val)
    else:
        if poc[len(poc) - 1] == val:
            del poc[-1]
            return 2
        else:
            poc.append(val)
    return 0

def solution(board, moves):
    answer = 0
    baskets = []
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] > 0:
                doll = board[i][m-1]
                answer += pocket(baskets, doll)
                board[i][m-1] = 0
                break
    return answer

test = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
mov = [1, 5, 3, 5, 1, 2, 1, 4]
# mov = [1]
print(solution(test, mov))
