def solution(board, k):
    len_b = len(board)
    len_ba = len(board[0])
    return sum(board[i][j] for i in range(len_b) for j in range(len_ba) if i+j <= k)