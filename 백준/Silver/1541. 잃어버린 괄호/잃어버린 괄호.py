import sys

def solve():
    inp = sys.stdin.readline().split('-')
    res = sum(map(int,inp[0].split('+')))
    for cur in inp[1:]:
        res -= sum(map(int,cur.split('+')))
    print(res)
solve()