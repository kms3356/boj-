import sys
def solve():
    inp = map(int, sys.stdin.read().split())
    n = next(inp)
    print(*sorted(inp), sep='\n')
solve()