def solution(intStrs, k, s, l):
    answer = [int(cur[s:s+l]) for cur in intStrs if int(cur[s:s+l]) > k]
    return answer