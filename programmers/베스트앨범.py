from collections import defaultdict
def solution(genres, plays):
    answer = []
    hash_gen = defaultdict(int)
    hash_pla = defaultdict(list)
    for i in range(len(genres)):
        hash_gen[genres[i]] += plays[i]
        hash_pla[genres[i]].append((plays[i], i))
    
    maxplay = sorted(hash_gen.items(), key= lambda a: -a[1])
    for genre, totalPlay in maxplay:
        res = sorted(hash_pla[genre], key = lambda a: (-a[0], a[1]))
        answer += [v for i, v in res[:2]]
    print(answer)
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
solution(genres, plays)