def solution(a, b, c):
    le = len(set([a,b,c]))
    answer = a+b+c
    if le <= 2:
        answer *= (a**2 + b**2 + c**2)
        if le == 1:
            answer *= (a**3 + b**3 + c**3)
    return answer