import sys
def solve():
    inp = map(int, sys.stdin.read().split())
    n = next(inp)
    Sum = next(inp)
    Max = Sum
    for cur in inp:
        if Sum > 0: Sum += cur
        else: Sum = cur

        if Sum > Max: Max = Sum
    print(Max)
solve()
