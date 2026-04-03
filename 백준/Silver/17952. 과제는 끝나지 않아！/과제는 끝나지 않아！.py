import sys
def solve():
    inp = map(int, sys.stdin.read().split())
    n = next(inp)
    res = 0
    stack = []
    Sum = []
    for _ in range(n):
        f = next(inp)
        if f == 1:
            Sum.append(next(inp))
            stack.append(next(inp))
        if stack:
            stack[-1] -= 1
            if stack[-1] == 0:
                res += Sum.pop()
                stack.pop()
                
    print(res)
solve()