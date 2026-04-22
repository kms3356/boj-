def solution(name, yearning, photo):
    dic = {key:value for key, value in zip(name,yearning)}
    answer = [sum(dic[k] for k in pho if k in dic) for pho in photo]
    return answer