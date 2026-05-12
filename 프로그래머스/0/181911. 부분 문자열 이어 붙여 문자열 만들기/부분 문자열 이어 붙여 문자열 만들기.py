def solution(my_strings, parts):
    return ''.join(my[part[0]:part[1]+1] for my, part in zip(my_strings, parts))