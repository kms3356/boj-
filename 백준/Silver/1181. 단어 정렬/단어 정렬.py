import sys
def solve():
    inp = sys.stdin.read().split()
    ls = list(set(inp[1:]))
    print(*sorted(ls, key=lambda x: (len(x), x)), sep='\n')
solve()