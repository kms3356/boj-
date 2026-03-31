import sys
input = sys.stdin.readline
def solve():
    res = []
    while True:
        num = list(input().rstrip())
        if num[0] == '0': break
        mid = len(num)//2
        isPall = True
        for i in range(mid):
            if num[i] == num[-1-i]: continue
            else:
                isPall = False
                break
        if isPall:
            res.append("yes")
        else:
            res.append("no")
    sys.stdout.write('\n'.join(res))     
solve()