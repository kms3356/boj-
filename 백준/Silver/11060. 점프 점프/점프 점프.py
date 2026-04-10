import sys
from collections import deque
def solve():
    inp = map(int, sys.stdin.read().split())
    n = next(inp)
    res = [0] * n
    A = list(inp)
    queue = deque([0])
    while queue:
        cur = queue.popleft()
        if cur == n-1:
            ans = res[cur]
            return ans
        for i in range(1,A[cur]+1):
            post = cur+i
            if post < n and not res[post]:
                res[post] = res[cur] + 1
                queue.append(post)
    return -1
print(solve())