import datetime
answer = ''
day = ['MON','TUE','WED','THU','FRI','SAT','SUN']
n = datetime.datetime(2016,6,7).weekday()
answer = day[n]
print(answer)