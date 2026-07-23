def solution(array):
    res = sorted([val, idx] for idx, val in enumerate(array))
    
    return res[-1]