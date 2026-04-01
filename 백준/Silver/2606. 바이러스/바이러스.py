import sys
input = sys.stdin.readline

def dfs(node):
    visited[node] = True
    count = 1
    for post in graph[node]:
        if not visited[post]: 
            count += dfs(post)
    return count


n = int(input())
m = int(input())

graph = {key : [] for key in range(1,n+1)}
for _ in range(m):
    c1, c2 = map(int, input().split())
    graph[c1].append(c2)
    graph[c2].append(c1)
for i in range(1,n+1):
    graph[i].sort()
visited = [False] * (n+1)
co = dfs(1)-1
print(co)