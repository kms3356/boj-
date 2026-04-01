import sys
from collections import deque
input = sys.stdin.readline

def solve():
    n,m,r = map(int,input().split())
    graph = {key : [] for key in range(1,n+1)}

    for _ in range(m):
        c1, c2 = map(int, input().split())
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