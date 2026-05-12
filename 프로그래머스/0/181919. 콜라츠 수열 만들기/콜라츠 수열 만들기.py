def solution(n):
    answer = []
    while n > 1:
        answer.append(n)
        if n&1:
            n = 3*n + 1
        else:
            n //= 2
    answer.append(1)
    return answer