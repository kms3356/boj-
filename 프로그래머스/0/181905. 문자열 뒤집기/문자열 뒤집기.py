def solution(my_string, s, e):
    rep = my_string[s:e+1]
    my_string = my_string.replace(rep, rep[::-1])
    return my_string