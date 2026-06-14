def solution(strArr):
    dic = {}
    for s in strArr:
        l = len(s)
        if l in dic:
            dic[l] += 1
        else:
            dic[l] = 1
    return max(dic.values())