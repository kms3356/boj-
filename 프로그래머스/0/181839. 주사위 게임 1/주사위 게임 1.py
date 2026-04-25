def solution(a, b):
    a_odd = a%2==0
    b_odd = b%2==0
    if a_odd and b_odd: ans = abs(a-b)
    elif not a_odd and not b_odd: ans = a**2 + b**2
    else: ans = 2 * (a+b)
    return ans