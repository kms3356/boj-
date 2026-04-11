import sys
input = sys.stdin.readline
def solve():
    n, m = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(n)]
    answer = [['W','B','W','B','W','B','W','B'], ['B','W','B','W','B','W','B','W'], ['W','B','W','B','W','B','W','B'], ['B','W','B','W','B','W','B','W'], ['W','B','W','B','W','B','W','B'], ['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'], ['B','W','B','W','B','W','B','W']]
    M = 64
    for i in range(n-7):
        for j in range(m-7):
            rows = board[i:i+8]
            count = 0
            for idx in range(8):
                row, ans = rows[idx][j:j+8], answer[idx]
                count += sum(1 for a,b in zip(row, ans) if a!=b)
            M = min(M, count, 64-count)
    print(M)

solve()