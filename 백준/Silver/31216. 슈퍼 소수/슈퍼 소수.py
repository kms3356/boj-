import sys
def sieve_of_eratosthenes():
    sieve = [True] * (318138)
    sieve[0] = sieve[1] = False
    sup = []
    for i in range(2, int(318137**0.5)+1):
        if sieve[i]:
            sieve[i*i : 318138 : i] = [False] * len(range(i*i, 318138, i))

    primes = [2] + [i for i in range(3, 318138, 2) if sieve[i]]
    sup = [primes[i] for i in range(len(primes)) if sieve[i+1]]
    return sup

def solve():
    inp = map(int, sys.stdin.read().split())
    t = next(inp)
    res = []
    sup = sieve_of_eratosthenes()
    for _ in range(t):
        n = next(inp)
        res.append(str(sup[n-1]))
    sys.stdout.write('\n'.join(res))
solve()