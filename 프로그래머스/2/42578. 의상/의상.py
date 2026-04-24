import math
def solution(clothes):
    clo = {}
    for t,i in clothes:
        if i not in clo:
            clo[i] = 2
        else: clo[i] += 1
    return math.prod(clo.values())-1