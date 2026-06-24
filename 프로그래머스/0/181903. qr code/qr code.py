def solution(q, r, code):
    res = []
    for i, c in enumerate(code):
        if i % q == r:
            res.append(c)
    return ''.join(res)