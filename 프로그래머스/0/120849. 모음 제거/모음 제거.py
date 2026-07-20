def solution(my_string):
    moum = {'a', 'e', 'i', 'o', 'u'}
    answer = ''.join(c for c in my_string if c not in moum)
    return answer