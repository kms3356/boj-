def solution(ineq, eq, n, m):
    if ineq == '>':
        if eq == '=':
            answer = (n >= m)
        else:
            answer = (n > m)
    else:
        if eq == '=':
            answer = (n <= m)
        else:
            answer = (n < m)
    return int(answer)