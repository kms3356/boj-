def solution(myString):
    dic = {chr(i):i for i in range(97, 123)}
    answer = ['l' if dic[char] < 108 else char for char in myString ]
    return ''.join(answer)