def solution(num_list):
    dic = [2,4,8,16]
    answer = 0
    for num in num_list:
        for i in range(4):
            if num//dic[i] == 1:
                answer += i+1
    return answer