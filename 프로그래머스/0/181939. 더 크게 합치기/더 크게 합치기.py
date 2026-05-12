def solution(a, b):
    a = str(a)
    b = str(b)
    A = int(a+b)
    B = int(b+a)
    return A if A > B else B