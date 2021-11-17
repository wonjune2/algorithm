def solution(sizes):
    w = 0
    h = 0
    for i in sizes:
        w = max(w, i[0])
        h = max(h, i[1])

    if w > h:
        h = 0
        for i in range(len(sizes)):
            if sizes[i][1] > sizes[i][0]:
                sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
            h = max(h, sizes[i][1])
    else:
        w = 0
        for i in range(len(sizes)):
            if sizes[i][1] < sizes[i][0]:
                sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
            w = max(w, sizes[i][0])
    return w * h

sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
print(solution(sizes))
