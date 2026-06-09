def solution(myString, pat):
    l = len(pat)
    for i in range(len(myString)-l+1):
        if myString[i:i+l] == pat:
            idx = i
    answer = myString[:idx+l]
    return answer