import sys
input = sys.stdin.readline
def dfs(i, sum):
    global count
    if i == n:
        if sum == s: 
            count += 1
        return

    
    dfs(i+1, sum)
    dfs(i+1, sum + nums[i])

n,s = map(int, input().split())
nums = list(map(int, input().split()))
count = 0
dfs(0, 0)
print(count-1 if s == 0 else count)