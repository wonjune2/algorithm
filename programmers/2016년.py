import datetime
def solution(a, b):
    answer = ''
    day = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    n = datetime.datetime(2016,a,b).weekday()
    answer = day[n]
    return answer