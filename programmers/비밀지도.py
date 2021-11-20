def solution(n, arr1, arr2):
    answer = [''] * n
    for i in range(n):
        one = format(arr1[i], 'b').zfill(n)
        two = format(arr2[i], 'b').zfill(n)
        for j in range(len(one)):
            if one[j] == '0' == two[j]:
                answer[i] += ' '
            else:
                answer[i] += '#'
    return answer

n = 5
arr1 = 	[9, 20, 28, 18, 11]
arr2 = 	[30, 1, 21, 17, 28]
solution(n, arr1, arr2)