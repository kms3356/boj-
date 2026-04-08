def fivo(n):
    if n==0: return 0
    if res[n]: return res[n]

    cur = fivo(n-1) + fivo(n-2)
    res[n] = cur
    return cur

num = int(input())
res = [0,1] + [0] * (num-1)
print(fivo(num))