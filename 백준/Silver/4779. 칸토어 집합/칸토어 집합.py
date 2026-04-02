import sys

def canto(st):
    if st == 1: return '-'
    size = st//3
    side = canto(size)
    center = " " * size
    return side + center + side

inp = map(int, sys.stdin.read().split())

for n in inp:
    st = 3**n
    print(canto(st))
