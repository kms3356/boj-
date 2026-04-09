import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    line = list(map(int,input().split()))
    sort = sorted(set(line))
    dic = {key:i for i, key in enumerate(sort)}
    res = [str(dic[k]) for k in line]
    sys.stdout.write(' '.join(res))
            
solve()