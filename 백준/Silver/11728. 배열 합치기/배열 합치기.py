import sys
input = sys.stdin.readline

n,m = map(int,input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
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