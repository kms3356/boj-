def solution(rank, attendance):
    res = [(idx, rnk) for idx, rnk in enumerate(rank) if attendance[idx]]
    res.sort(key=lambda x:x[1])
    
    answer = res[0][0] * 10000 + res[1][0] * 100 + res[2][0]
    return answer