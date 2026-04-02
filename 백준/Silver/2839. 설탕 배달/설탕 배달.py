def solve():
    n = int(input())
    min = n//5 + n//3
    isChange = False
    for a5 in range(n//5 + 1):
        for a3 in range(n//3 + 1):
            if a5*5 + a3*3 == n:
                if min >= a5+a3: 
                    isChange = True
                    min = a5+a3
    if isChange:
        print(min)
    else:
        print(-1)
solve()