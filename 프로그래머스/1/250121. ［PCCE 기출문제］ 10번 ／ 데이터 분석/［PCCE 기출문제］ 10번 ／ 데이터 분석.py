def solution(data, ext, val_ext, sort_by):
    ex = {'code':0, 'date':1, 'maximum':2, 'remain':3}
    ext = ex[ext]
    sort_by = ex[sort_by]
    res = [row for row in data if row[ext] < val_ext]
    res.sort(key=lambda x: x[sort_by])

    return res