import sys
input = sys.stdin.readline

n = int(input())
nums = map(int,input().split())
res = [next(nums)] + [0] * (n-1)
for i in range(1,n):
    cur = next(nums)
    ma = max(res[i-1] + cur, cur)
    res[i] = ma


print(max(res))