import sys
def solve():
    inp = iter(sys.stdin.read().split())
    n = int(next(inp))
    res = [[] for _ in range(51)]
    for cur in inp:
        if cur not in res[len(cur)]:
            res[len(cur)].append(cur)
    for list in res:
        if list:
            list.sort()
            print(*list, sep='\n')

solve()