def solution(a, d, included):
    answer = 0
    for cur in included:
        if cur:
            answer += a
        a += d
    return answer