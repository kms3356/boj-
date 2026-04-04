import sys
input = sys.stdin.readline
def solve():
    n = int(input())
    res = [0] * 10001

    for _ in range(n):
        r = int(input())
        res[r] += 1
    for i in range(1,10001):
        for _ in range(res[i]):
            print(i)
solve()
