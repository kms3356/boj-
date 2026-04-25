def solution(n, control):
    dic = {'w':0, 's':0, 'd':0, 'a':0}
    for i in control:
        dic[i] += 1
    answer = n + dic['w'] - dic['s'] + dic['d']*10 - dic['a']*10
    return answer