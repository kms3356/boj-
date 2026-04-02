import sys

def solve():
    min = m
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                cur = m-(nums[i]+nums[j]+nums[k])
                if 0 < cur < min:
                    min = cur
                    ans = nums[i]+nums[j]+nums[k]
                elif cur == 0:
                    ans = nums[i]+nums[j]+nums[k]
                    return ans
    return ans

n,m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
ans = solve()
print(ans)