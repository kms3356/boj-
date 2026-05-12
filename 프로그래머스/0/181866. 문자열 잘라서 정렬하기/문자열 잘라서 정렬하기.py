def solution(myString):
    return sorted(i for i in myString.strip('x').split('x') if i)