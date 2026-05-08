def solution(arr, idx):
    for a,b in enumerate(arr):
        if a >= idx and b==1:
            return a
    
    return -1