import collections
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

# print(solution(participant, completion))

dict = {hash(participant[i]):'completion' for i in range(len(participant))}
print(dict)
print(dict.get(hash(participant[3])))
