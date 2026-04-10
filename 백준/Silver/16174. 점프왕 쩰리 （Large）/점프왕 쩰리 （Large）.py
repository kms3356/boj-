import sys
input = sys.stdin.readline
def dfs(i,j):
    if res[i][j]: return
    cur = M[i][j]
    res[i][j] = True
    if cur ==-1: return
    if i+cur < n :
        dfs(i+cur, j)
    if j+cur < n:
        dfs(i, j+cur)

n = int(input())
M = [tuple(map(int,input().split())) for _ in range(n)]

res = [[False] * n for _ in range(n)]
dfs(0,0)
if res[-1][-1]:
    print("HaruHaru")
else:
    print("Hing")
