import sys
def solve():
    inp = map(int, sys.stdin.read().split())
    n = next(inp)
    k = next(inp)
    A = list(inp)
    count = 0
    for i in range(n-1, -1, -1):
        a, b = divmod(k,A[i])
        if a:
            count += a
            if b == 0:
                break
            k = b
    print(count)
solve()