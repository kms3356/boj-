def solution(numLog):
    res = {1:'w', -1:'s', 10:'d', -10:'a'}
    answer = ''.join(res[numLog[i+1]-numLog[i]] for i in range(len(numLog)-1))
        
    return answer