import math
def solution(n,a,b):
    i = 0
    while a!=b:
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        i += 1
        
    return i