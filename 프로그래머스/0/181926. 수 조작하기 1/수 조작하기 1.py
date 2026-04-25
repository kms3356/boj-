def solution(n, control):
    dic = {'w':1, 's':-1, 'd':10, 'a':-10}
    answer = n + sum(dic[k] for k in control)
    return answer