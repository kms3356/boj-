import sys
def solve():
    x = int(sys.stdin.readline())
    res = [0,0,1,1,2,3,2,3,3,2,3,4,3,4,4,4,4] + [0] * (x-15)
    if x <= 16:
        print(res[x])
    else:
        for i in range(17, x+1):
            if i%2==0 and i%3==0:
                res[i] = min(res[i-1], res[i//2], res[i//3]) + 1
            elif i%2==0:
                res[i] = min(res[i-1], res[i//2]) + 1
            elif i%3==0:
                res[i] = min(res[i-1], res[i//3]) + 1
            else:
                res[i] = res[i-1] + 1
        print(res[x])
solve()
