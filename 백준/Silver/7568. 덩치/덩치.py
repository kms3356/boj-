import sys
def solve():
    inp = map(int, sys.stdin.read().split())
    n = next(inp)
    data = [(next(inp), next(inp)) for _ in range(n)]
    dic = {i : 1 for i in range(n)}
    for i in range(n):
        for j in range(i+1, n):
            if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
                dic[i] += 1
            elif data[i][0] > data[j][0] and data[i][1] > data[j][1]:
                dic[j] += 1
    print(' '.join(str(i) for i in dic.values()))

solve()