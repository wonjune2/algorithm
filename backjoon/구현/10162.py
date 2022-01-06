t = int(input())
time = [300, 60, 10]
for i in range(len(time)):
    now = time[i]
    time[i] = t // now
    t = t % now

if t:
    print(-1)
else:
    for i in time:
        print(i, end=" ")
    