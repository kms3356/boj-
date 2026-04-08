import sys
def solve():
    n,m = map(int, sys.stdin.readline().split())
    nums = sorted(map(int, sys.stdin.readline().split()))
    ans = 0
    for i in range(n):
        left = i+1
        right = n-1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s==m:
                ans = s
                return ans
            elif s < m:
                if s > ans:
                    ans = s
                left += 1
            else:
                right -= 1
    return ans
print(solve())