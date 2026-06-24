def solution(arr):
    x = 0
    l = len(arr)
    while True:
        arr_pre = arr.copy()
        for i in range(l):
            fi = (arr[i] >= 50)
            od = (arr[i] & 1 == 0)
            if fi and od:
                arr[i] //= 2
            elif not fi and not od:
                arr[i] = arr[i] * 2 + 1
        if arr_pre == arr:
            return x
        x += 1