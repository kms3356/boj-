def solution(schedules, timelogs, startday):
    result = 0
    weekend = set(((6-startday)%7, 7-startday))
    for i in range(len(schedules)):
        a,b = divmod(schedules[i], 100)
        time = (a+(b+10>=60))*100 + (b+10)%60
        for j in range(7):
            if j in weekend:
                continue
            if timelogs[i][j] > time:
                break
        else:
            result += 1
    return result