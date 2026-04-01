import sys
from collections import deque
input = sys.stdin.readline

def solve():
    n,m,r = map(int,input().split())
    graph = {key : [] for key in range(1,n+1)}
    res = {key : 0 for key in range(1,n+1)}
    for _ in range(m):
        c1, c2 = map(int, input().split())
        graph[c1].append(c2)
        graph[c2].append(c1)
    for i in range(1,n+1):
        graph[i].sort()

    visited = [False] * (n+1)

    queue = deque([r])
    visited[r] = True
    i = 1
    res[r] = i
    while(queue):
        cur = queue.popleft()
        for post in graph[cur]:
            if not visited[post]:
                i+=1
                queue.append(post)
                visited[post] = True
                res[post] = i
    print(*res.values(), sep='\n')
solve()