def solution(myString, pat):
    l = len(pat)
    count = 0
    for i in range(len(myString)-l+1):
        if myString[i:i+l] == pat:
            count += 1
    return count