import sys
def solve():
    nums = sys.stdin.readline().rstrip()
    n = sorted(nums,reverse=True)
    sys.stdout.write(''.join(str(i) for i in n))
solve()