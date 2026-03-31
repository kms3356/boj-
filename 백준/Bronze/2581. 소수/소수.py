import sys
def sieve_of_eratosthenes(max_num):
    sieve = [True] * (max_num+1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(max_num**0.5)+1):
        if sieve[i]:
            sieve[i*i : max_num+1 : i] = [False] * len(range(i*i, max_num+1, i))
    return sieve

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

sieve = sieve_of_eratosthenes(n)

prime_numbers = [i for i in range(m, n+1) if sieve[i]]

if prime_numbers:
    print(sum(prime_numbers), min(prime_numbers), sep = '\n')
else:
    print(-1)    