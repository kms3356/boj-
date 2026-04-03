import sys

def solve():
    inp = map(int, sys.stdin.read().split())
    res = 0
    for i in inp:
        res += i
        if res == 100: break
        if res > 100:
            if abs(100-res) <= abs(100-(res-i)):
                break
            else:
                res -= i
                break

    print(res)
solve()