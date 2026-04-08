import sys
input = sys.stdin.readline

def solve():
    input()
    A = set(input().split())
    input()
    nums = input().split()
    res = []
    for num in nums:
        res.append('1' if num in A else '0')

    sys.stdout.write('\n'.join(res))

solve()
