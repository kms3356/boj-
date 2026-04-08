import sys
from collections import deque

def solve():
    n,k = map(int, sys.stdin.readline().split())
    res = [0] * 1000001

    queue = deque([n])

    while queue:
        cur = queue.popleft()
        if cur == k: 
            print(res[cur])
            return
        for post in (cur-1,cur+1,cur*2):
            if 0<=post <=1000000 and not res[post]:
                res[post] = res[cur] + 1
                queue.append(post)
solve()