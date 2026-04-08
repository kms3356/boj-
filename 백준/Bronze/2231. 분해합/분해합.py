def solve():
    n = int(input())
    m = max(1, n - 54)
    for i in range(m, n):
        rs = temp = i
        while i > 0:
            rs += i % 10
            i //= 10
        if rs == n:
            print(temp)
            return
    print(0)    
solve()