import sys
input = sys.stdin.readline

t = int(input())
res = []
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())

    l = (x2-x1)**2 + (y2-y1)**2
    sr = (r1+r2)**2
    dr = (r1-r2)**2
    if l == 0:
        if r1==r2:res.append('-1')
        else: res.append('0')

    else:
        if l==sr or l==dr:
            res.append('1')
        elif dr < l < sr:
            res.append('2')
        else:
            res.append('0')
sys.stdout.write('\n'.join(res))