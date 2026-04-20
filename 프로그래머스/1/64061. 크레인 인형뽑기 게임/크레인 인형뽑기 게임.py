from collections import deque
def solution(board, moves):
    n = len(board)
    stack = [deque([board[j][i] for j in range(n) if board[j][i]]) for i in range(n)]
    res = [-1]
    count = 0
    for cur in moves:
        if stack[cur-1]:
            po = stack[cur-1].popleft()
        else : continue
        if res[-1] == po:
            res.pop()
            count += 2
        else:
            res.append(po)
    
    return count