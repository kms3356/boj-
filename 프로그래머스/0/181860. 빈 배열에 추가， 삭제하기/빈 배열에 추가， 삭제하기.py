def solution(arr, flag):
    res = []
    for i in range(len(arr)):
        if flag[i]:
            res.extend([arr[i]] * arr[i]*2)
        else:
            res = res[:-arr[i]]
    return res