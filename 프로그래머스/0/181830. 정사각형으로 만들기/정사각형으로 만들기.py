def solution(arr):
    if len(arr) < len(arr[0]):
        t = len(arr[0]) - len(arr)
        for _ in range(t):
            arr.append([0] * len(arr[0]))
        
    else:
        t = len(arr) - len(arr[0])
        for i in range(len(arr)):
            arr[i] += [0] * t
    return arr