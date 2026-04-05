import sys
input = sys.stdin.readline
def solve():
    inp = input().rstrip()
    Sum = 0
    for i in range(13):
        if i%2 ==0:
            k = 1
        else:
            k = 3
        if inp[i] =='*':
            ans = k
            continue
        Sum += int(inp[i]) * k
    for i in range(10):
        if (Sum + i * ans) % 10 ==0:
            print(i)
            break
solve()
