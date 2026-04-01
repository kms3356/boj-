import sys
sys.setrecursionlimit(10**6)
def dfs(node):
    global count
    visited[node] = count
    for cur in graph[node]:
        if visited[cur] == 0: 
            count+=1
            dfs(cur)


inp = map(int, sys.stdin.read().split())
n = next(inp)
m = next(inp)
r = next(inp)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    c1 = next(inp)
    c2 = next(inp)
    graph[c1].append(c2)
    graph[c2].append(c1)
for i in range(1,n+1):
    graph[i].sort()
visited = [0] * (n+1)
count = 1
dfs(r)
print(*visited[1:], sep='\n')