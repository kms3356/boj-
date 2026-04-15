import sys
def round(val):
    if val - int(val) >= 0.5:
        return int(val) + 1
    else:
        return int(val)


def solve():
    inp = map(int, sys.stdin.read().split())
    n = next(inp)
    de = round(n*0.15)
    nums = sorted(inp)[de:n-de]
    if len(nums) == 0:
        print(0)
        return
    print(round(sum(nums)/len(nums)))
solve()