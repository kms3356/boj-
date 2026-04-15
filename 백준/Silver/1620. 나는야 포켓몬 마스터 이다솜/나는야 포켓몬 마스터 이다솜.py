import sys
def solve():
    inp = sys.stdin.read().split()
    n, m = int(inp[0]), int(inp[1])
    dic = {}
    idx = 1
    for i,val in enumerate(inp[2:2+n], 1):
        idx = str(i)
        dic[val] = idx
        dic[idx] = val
    res = [dic[v] for v in inp[2+n:]]
    print("\n".join(res))
solve()