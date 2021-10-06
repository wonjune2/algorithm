import re
def solution(new_id):
    res = new_id.lower()
    res = re.findall('[\w._-]', res)
    new = ''
    for i in res:
       new += i
    new = re.sub('(([.])\\2{1,})','.',new)
    if len(new) > 0 and '.' in new[0]: new = new[1:]
    if len(new) > 0 and '.' in new[-1]: new = new[:-1]
    if not new:
        new += 'a'
    if len(new) > 15:
        new = new[:15]
        if '.' in new[0]: new = new[1:]
        if '.' in new[-1]: new = new[:-1]
    while len(new) < 3:
        new += new[-1]
    return new


test = "abcdefghijklmn.p"
solution(test)