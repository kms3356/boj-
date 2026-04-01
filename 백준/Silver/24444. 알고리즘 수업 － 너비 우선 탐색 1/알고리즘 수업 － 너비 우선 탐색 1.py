import sys
from collections import deque

def solve():
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
    queue = deque([r])
    i = 1
    visited[r] = i
    while(queue):
        cur = queue.popleft()
        for post in graph[cur]:
            if not visited[post]:
                i+=1
                queue.append(post)
                visited[post] = i
    sys.stdout.write('\n'.join(map(str,visited[1:])))
solve()