import sys
input = sys.stdin.readline
def solve():
    input()
    st = input().rstrip()
    Sum = 0
    a = 0
    for i in st:
        Sum += (ord(i) - 96) * (31 ** a)
        a += 1
    print(Sum%1234567891)
solve()