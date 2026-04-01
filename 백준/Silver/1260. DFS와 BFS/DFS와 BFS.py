import sys
from collections import deque
def dfs(node):
    visited[node] = True
    print(node, end=' ')
    for cur in graph[node]:
        if not visited[cur]: dfs(cur)

def bfs():
    queue = deque()
    queue.append(v)
    print(v, end=' ')
    visited[v] = True
    while(queue):
        cur = queue.popleft()
        for post in graph[cur]:
            if not visited[post]:
                queue.append(post)
                visited[post] = True
                print(post, end=' ')        

inp = map(int, sys.stdin.read().split())
n = next(inp)
m = next(inp)
v = next(inp)
graph = {key : [] for key in range(1,n+1)}
for _ in range(m):
    n1 = next(inp)
    n2 = next(inp)
    graph[n1].append(n2)
    graph[n2].append(n1)
for i in range(1,n+1):
    graph[i].sort()
visited = [False] * (n+1)
dfs(v)
print()

visited = [False] * (n+1)
bfs()
