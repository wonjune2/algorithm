def solution(rows, columns, queries):
    answer = []
    array = [[j for j in range(i, i + columns)] for i in range(1, rows * columns, columns)]
    for x1, y1, x2, y2 in queries:
        tmp = array[x1-1][y1-1]
        mini = tmp

        # left
        for i in range(x1 - 1, x2 - 1):
            temp = array[i+1][y1-1]
            array[i][y1-1] = temp
            mini = min(temp, mini)
        
        # bottom
        for i in range(y1 - 1, y2 - 1):
            temp = array[x2-1][i+1]
            array[x2-1][i] = temp
            mini = min(temp, mini)

        # right
        for i in range(x2-1, x1-1, -1):
            temp = array[i-1][y2-1]
            array[i][y2-1] = temp
            mini = min(temp, mini)
        
        # top
        for i in range(y2 - 1, y1 - 1, -1):
            temp = array[x1-1][i-1]
            array[x1-1][i] = temp
            mini = min(temp, mini)
    
        array[x1-1][y1] = tmp
        answer.append(mini)
    return answer

rows = 6
columns = 6
queries = [[2,2,5,4]]
solution(rows, columns, queries)
# array = [[j for j in range(i, i + columns)] for i in range(1, rows * columns, columns)]
# answer = []
# for x1, y1, x2, y2 in queries:
#     tmp = array[x1-1][y1-1]
#     mini = tmp

#     # left
#     for i in range(x1 - 1, x2 - 1):
#         temp = array[i+1][y1-1]
#         array[i][y1-1] = temp
#         mini = min(temp, mini)
    
#     # bottom
#     for i in range(y1 - 1, y2 - 1):
#         temp = array[x2-1][i+1]
#         array[x2-1][i] = temp
#         mini = min(temp, mini)

#     # right
#     for i in range(x2-1, x1-1):
#         temp = array[i-1][y2-1]
#         array[i][y2-1] = temp
#         mini = min(temp, mini)
    
#     # top
#     for i in range(y2 - 1, y1 - 1):
#         temp = array[x1-1][i-1]
#         array[x1-1][i] = temp
#         mini = min(temp, mini)
    
#     array[x1-1][y1] = tmp
#     answer.append(mini)

# print(answer)