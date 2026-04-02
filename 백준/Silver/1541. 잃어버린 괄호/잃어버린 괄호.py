import sys

def solve():
    inp = sys.stdin.readline()
    res = []
    cur = []
    flag = False
    for char in inp:
        if char in ('-','+','\n'):
            if flag:
                res.append(-int(''.join(cur)))
            else:
                res.append(int(''.join(cur)))
            if char == '-':
                flag = True
            cur.clear()
        else:
            cur.append(char)
    print(sum(res))
solve()