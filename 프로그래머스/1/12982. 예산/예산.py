def solution(d, budget):
    d.sort()
    S = 0
    for i in range(len(d)):
        S += d[i]
        if S > budget:
            return i
    else:
        return i+1
            