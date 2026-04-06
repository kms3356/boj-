import sys
input = sys.stdin.readline
from collections import deque
def solve():
    n = int(input())
    res = [[] for _ in range(n+1)]
    for _ in range(n-1):
        n1, n2 = map(int, input().split())
        res[n1].append(n2)
        res[n2].append(n1)
    
    visited = [0] * (n+1)
    queue = deque([1])
    visited[1] = 1
    while(queue):
        cur = queue.popleft()

        for post in res[cur]:
            if not visited[post]:
                queue.append(post)
                visited[post] = cur
    sys.stdout.write('\n'.join(map(str, visited[2:])))
solve()