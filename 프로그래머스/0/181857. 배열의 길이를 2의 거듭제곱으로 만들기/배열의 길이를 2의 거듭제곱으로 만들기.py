def solution(arr):
    l = len(arr)
    res = 1
    while res < l:
        res *= 2
    arr += [0] * (res - l)
    return arr