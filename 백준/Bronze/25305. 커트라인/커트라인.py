import sys
def solve():
    inp = map(int, sys.stdin.read().split())
    n, k = next(inp), next(inp)
    print(sorted(inp)[-k])
solve()