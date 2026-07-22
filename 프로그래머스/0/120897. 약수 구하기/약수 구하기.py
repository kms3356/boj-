def solution(n):
    res = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            res.append(i)
            res.append(n // i)
    if res[-1] == res[-2]:
        res.pop()    
    res.sort()
    return res