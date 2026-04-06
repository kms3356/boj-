import sys
input = sys.stdin.readline
def mid(left, right,i):
    if right < left : return
    middle = (left+right)//2
    res[i].append(nums[middle])
    mid(left, middle-1, i+1)
    mid(middle+1, right, i+1)


k = int(input())
res = [[] for _ in range(k)]
nums = list(map(int, input().split()))
mid(0, len(nums)-1,0)
for cur in res:
    print(*cur)