import sys

def canto(st):
    if len(st) == 1: return st
    size = len(st)//3
    side = canto(st[:size])
    center = " " * size
    return side + center + side

inp = map(int, sys.stdin.read().split())

for n in inp:
    st = "-" * (3**n)
    print(canto(st))
