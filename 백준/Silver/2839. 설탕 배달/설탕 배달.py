import sys
def solve():
    n = int(sys.stdin.readline())
    ans = 0
    while True:
        if n%5==0:
            ans += n//5
            break
        
        if 0 < n < 3:
            ans = -1
            break
        elif n == 0:
            break
        n -= 3
        ans += 1
    print(ans)
solve()