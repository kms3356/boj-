import sys
def solve():
    inp = map(int, sys.stdin.read().split())
    n = next(inp)
    stack = []
    res = []
    i = 1
    for cur in inp:
        while i <= cur:
            stack.append(i)
            res.append('+')
            i += 1
        if stack[-1] == cur:
            stack.pop()
            res.append('-')
        else:
            print("NO")
            return
    sys.stdout.write('\n'.join(res))
solve()