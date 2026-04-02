import sys
input = sys.stdin.readline
def solve():
    n,m= map(int, input().split())
    a = sorted(map(int, input().split()))
    ans = 0
    flag = False
    for i in range(n):
        left = i+1
        right = n-1
        while left < right:
            s = a[i] + a[left] + a[right]
            if s == m:
                ans = s
                flag = True
                break
            elif s < m:
                left += 1
                if s > ans:
                    ans = s
            else:
                right -= 1
        if flag:
            break
    print(ans)


solve()