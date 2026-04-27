def solution(arr, n):
    i = (1 if len(arr)%2==0 else 0)
    for idx in range(i,len(arr),2):
        arr[idx] += n
    return arr