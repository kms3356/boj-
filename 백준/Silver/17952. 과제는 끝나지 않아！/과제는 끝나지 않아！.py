import sys
def solve():
    inp = map(int, sys.stdin.read().split())
    n = next(inp)
    res = 0
    stack = []
    for _ in range(n):
        f = next(inp)
        if f == 1:
            stack.append([next(inp),next(inp)])
        if stack:
            stack[-1][1] -= 1
            if stack[-1][1] == 0:
                res += stack[-1][0]
                stack.pop()

    print(res)
solve()