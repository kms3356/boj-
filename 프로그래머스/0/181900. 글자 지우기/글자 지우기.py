def solution(my_string, indices):
    ms = list(my_string)
    for i in indices:
        ms[i] = ''
    return ''.join(ms)