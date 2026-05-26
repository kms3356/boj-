def solution(participant, completion):
    dic = {}
    for cur in participant:
        if cur in dic:
            dic[cur] += 1
        else:
            dic[cur] = 1
    for cur in completion:
        dic[cur] -= 1
        if dic[cur] == 0: dic.pop(cur)
    
    answer = dic.popitem()
    return answer[0]