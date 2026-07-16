def solution(a, b, c, d):
    dic = {}
    for i in [a,b,c,d]:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    result = sorted(dic.items(), key=lambda x:(x[1], x[0]))
    L = len(result)
    match L:
        case 4:
            answer = result[0][0]
        case 3:
            answer = result[0][0] * result[1][0]
        case 2:
            if result[0][1] == 1:
                answer = (10 * result[1][0] + result[0][0]) ** 2
            else:
                answer = (result[0][0] + result[1][0]) * abs(result[0][0] - result[1][0])
        case 1:
            answer = result[0][0] * 1111
    return answer