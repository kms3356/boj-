def solution(name):
    N = [min(ord(c)-65, 91-ord(c)) for c in name]
    Sum = sum(N)
    if not Sum: return 0
    n = len(N)
    minimum = n-1
    N[0] = 0
    meet_first = True
    for i in range(1,n):
        if N[i]:
            if meet_first:
                meet_first = False
                minimum = min(minimum, n-i)
            post = i+1
            while post < n and not N[post]:
                post += 1
            minimum = min(minimum, i*2 + n-post, i + (n-post)*2)
            
    return minimum + Sum