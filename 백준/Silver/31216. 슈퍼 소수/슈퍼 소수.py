import sys
input = sys.stdin.readline
def sieve_of_eratosthenes():
    sieve = [True] * (318138)
    sieve[0] = sieve[1] = False
    sup = []
    for i in range(2, int(318137**0.5)+1):
        if sieve[i]:
            sieve[i*i : 318138 : i] = [False] * len(range(i*i, 318138, i))

    primes = [i for i in range(2, 318138) if sieve[i]]
    sup = []
    for idx, prime in enumerate(primes):
        if sieve[idx+1]:
            sup.append(prime)
    return sup

def solve():
    t = int(input())
    sup = sieve_of_eratosthenes()
    for _ in range(t):
        n = int(input())
        print(sup[n-1])
solve()