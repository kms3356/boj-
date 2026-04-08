import sys

inp = map(int, sys.stdin.read().split())
t = next(inp)
res = [[1,0], [0,1]] + [[0,0] for _ in range(39)]
for i in range(2,41):
    res[i] = [res[i-1][0] + res[i-2][0], res[i-1][1] + res[i-2][1]]

for _ in range(t):
    idx = next(inp)
    print(*res[idx])