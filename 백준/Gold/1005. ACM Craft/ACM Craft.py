import sys
sys.setrecursionlimit(10**6)
def Sum(node):
    if calc[node] != -1: return calc[node]
    ma = 0
    for cur in graph[node]:
        cur_sum = Sum(cur)
        if cur_sum > ma : ma = cur_sum
    calc[node] = D[node] + ma
    return calc[node]


inp = map(int, sys.stdin.read().split())
t = next(inp)
res = []
for _ in range(t):
    n = next(inp)
    k = next(inp)
    D = [0] + [next(inp) for _ in range(n)]
    graph = [[] for _ in range(n+1)]
    calc = [-1] * (n+1)
    for _ in range(k):
        n1 = next(inp)
        n2 = next(inp)
        graph[n2].append(n1)
    r = next(inp)
    res.append(str(Sum(r)))
sys.stdout.write('\n'.join(res))

