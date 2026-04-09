import sys
input = sys.stdin.readline

def solve():
    inp = map(int,sys.stdin.read().split())
    next(inp)
    line = list(inp)
    sort = sorted(set(line))
    dic = {key:i for i, key in enumerate(sort)}
    res = [dic[k] for k in line]
    sys.stdout.write(' '.join(map(str, res)))
            
solve()