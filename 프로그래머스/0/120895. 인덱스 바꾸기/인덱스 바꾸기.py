def solution(my_string, num1, num2):
    ls = list(my_string)
    ls[num1], ls[num2] = ls[num2], ls[num1]
    return ''.join(ls)