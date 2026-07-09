def solution(my_string, overwrite_string, s):
    res = list(my_string)
    res[s:s+len(overwrite_string)] = overwrite_string
    return ''.join(res)