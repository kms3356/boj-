import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    res = []
    for _ in range(n):
        a,b = map(int,input().split())
        res.append((a,b))
    res.sort(key=lambda x: (x[1], x[0]))
    for a,b in res:
        print(a,b)

solve()
