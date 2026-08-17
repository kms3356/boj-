def solution(num, k):
    ls = list(str(num))
    k = str(k)
    if k in ls:
        answer = ls.index(k)+1
    else:
        answer = -1
    return answer