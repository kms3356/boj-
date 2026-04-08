import sys
input = sys.stdin.readline
def solve():
    n,m = map(int,input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if A[0] >= B[-1]:
        B.extend(A)
        sys.stdout.write(' '.join(map(str,B)))
        return
    if B[0] >= A[-1]:
        A.extend(B)
        sys.stdout.write(' '.join(map(str,A)))
        return
    
    res = []
    i=j=0
    while i < n and j < m:
        if A[i] <= B[j]:
            res.append(A[i])
            i+=1
        else:
            res.append(B[j])
            j+=1

    res.extend(A[i:] if i < n else B[j:])
    sys.stdout.write(' '.join(map(str,res)))
solve()