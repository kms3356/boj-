def solution(arr, queries):
    res = []
    for s, e, k in queries:
        temp = []
        for i in range(s, e+1):
            if k < arr[i]:
                temp.append(arr[i])
        res.append(min(temp) if temp else -1)
    return res