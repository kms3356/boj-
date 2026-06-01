def solution(date1, date2):
    for i, j in zip(date1, date2):
        if i < j: return 1
        if i > j: return 0
        
    return 0