import sys

def solve():
    inp = iter(sys.stdin.read().split())
    n = int(next(inp))
    res = []
    for _ in range(n):
        a,b,c,d = next(inp), next(inp), next(inp), next(inp)
        res.append((a,int(b),int(c),int(d)))
    res.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
    ans = [x[0] for x in res]
    sys.stdout.write("\n".join(ans))

solve()
