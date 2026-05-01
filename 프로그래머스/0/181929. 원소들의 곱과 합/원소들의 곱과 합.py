import math
def solution(num_list):
    s = sum(num_list)**2
    a = math.prod(num_list)
    return int(a < s)