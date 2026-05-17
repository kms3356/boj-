def solution(num_list):
    odds = []
    even = []
    for i in num_list:
        if i&1:
            odds.append(str(i))
        else:
            even.append(str(i))
    answer = int(''.join(odds)) + int(''.join(even))
    return answer