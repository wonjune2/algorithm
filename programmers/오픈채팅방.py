def solution(record):
    answer = []
    dic = {}
    for i in record:
        n = i.split()
        if n[0] == 'Enter' or n[0] == "Change":
            dic[n[1]] = n[2]
    for i in record:
        n = i.split()
        if n[0] == 'Enter':
            s = dic[n[1]] + '님이 들어왔습니다.'
            answer.append(s)
        elif n[0] == 'Leave':
            s = dic[n[1]] + '님이 나갔습니다.'
            answer.append(s)
        else:
            pass
    print(answer)
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
solution(record)
