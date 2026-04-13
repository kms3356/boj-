import sys
from collections import deque
input = sys.stdin.readline
def solve():
    t = int(input())
    res = []
    for _ in range(t):
        n,m = map(int, input().split())
        inp = map(int, input().split())
        nums = deque([(i, val) for i, val in enumerate(inp)])
        count = 0
        while nums:
            a = nums.popleft()
            
            
            if any(a[1] < num[1] for num in nums):
                nums.append(a)
            else:
                count +=1
                if a[0] == m: 
                    res.append(count)
                    break
    sys.stdout.write('\n'.join(str(a) for a in res))
solve()