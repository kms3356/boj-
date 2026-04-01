import sys
from collections import deque
input = sys.stdin.readline

def solve():
    n,m = map(int,input().split())
    graph = {key : [] for key in range(1,n+1)}

    for _ in range(m):
        c1, c2 = map(int, input().split())
        graph[c1].append(c2)
        graph[c2].append(c1)

    visited = [False] * (n+1)

    count = 0
    for i in range(1,n+1):
        if not visited[i]:
            count += 1
            queue = deque([i])
            visited[i] = True
        while(queue):
            cur = queue.popleft()
            for post in graph[cur]:
                if not visited[post]:
                    queue.append(post)
                    visited[post] = True
    print(count)
solve()