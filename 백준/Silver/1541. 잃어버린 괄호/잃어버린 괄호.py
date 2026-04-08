import sys
def solve():
    inp = sys.stdin.readline()
    res = 0
    cur = []
    flag = False
    for char in inp:
        if char in ('-','+','\n'):
            if flag:
                res -= int(''.join(cur))
            else:
                res += int(''.join(cur))
            if char == '-':
                flag = True
            cur.clear()
        else:
            cur.append(char)
    print(res)
solve()