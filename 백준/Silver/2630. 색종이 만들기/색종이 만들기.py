import sys

def sak(nums, row):
    color = nums[0][0]
    if sum(r.count(color) for r in nums) == row**2:
        col_list[color] += 1
        return
    else:
        srow = row//2
        s1 = []
        s2 = []
        s3 = []
        s4 = []
        for i in range(srow):
            s1.append(nums[i][:srow])
            s2.append(nums[i][srow:])
        for i in range(srow,row):
            s3.append(nums[i][:srow])
            s4.append(nums[i][srow:])
        sak(s1,srow)
        sak(s2,srow)
        sak(s3,srow)
        sak(s4,srow)

col_list = [0,0]
n = int(sys.stdin.readline())
nums = []
for _ in range(n):
    line = map(int,sys.stdin.readline().split())
    nums.append([i for i in line])


sak(nums,n)
print(*col_list, sep='\n')
