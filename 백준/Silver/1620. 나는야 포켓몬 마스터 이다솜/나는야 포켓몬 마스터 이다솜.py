import sys
def solve():
    inp = iter(sys.stdin.read().split())
    n, m = int(next(inp)), int(next(inp))
    dic = {}
    idx = 1
    res = []
    for _ in range(n):
        name = next(inp)
        i = str(idx)
        dic[name] = i
        dic[i] = name
        idx += 1
    for _ in range(m):
        q = next(inp)
        res.append(dic[q])
    print("\n".join(res))
solve()