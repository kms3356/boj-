import sys
input = sys.stdin.readline
def solve():
    n = input()
    dic = {}
    nums = input().split()
    for cur in nums:
        if cur in dic:
            dic[cur] += 1
        else:
            dic[cur] = 1
    input()
    nums2 = input().split()
    res = [dic[cur] if cur in dic else 0 for cur in nums2]
    sys.stdout.write(' '.join(map(str,res)))
    
solve()