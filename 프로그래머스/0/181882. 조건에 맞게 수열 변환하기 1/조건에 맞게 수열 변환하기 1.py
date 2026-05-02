def solution(arr):
    for i, val in enumerate(arr):
        if val>=50 and val&1==0:
            arr[i] //= 2
        elif val<50 and val&1==1:
            arr[i] *= 2
    return arr