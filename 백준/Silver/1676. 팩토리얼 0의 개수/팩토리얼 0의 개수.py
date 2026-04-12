import sys
from math import factorial
input = sys.stdin.readline
def solve():
    n = int(input())
    nums = list(str(factorial(n)))
    count = 0
    for i in range(len(nums)-1, -1, -1):
        if nums[i] == '0': count += 1
        else: break
    print(count)

solve()