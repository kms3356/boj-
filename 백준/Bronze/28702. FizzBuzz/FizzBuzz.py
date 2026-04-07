import sys
def solve():
    inp = sys.stdin.read().split()
    for i in range(3):
        if inp[i] in ('Fizz', 'Buzz', 'FizzBuzz'):
            continue
        else:
            c = int(inp[i]) + 3-i
            if c%3==0:
                if c%5==0:
                    ans = 'FizzBuzz'
                else:
                    ans = 'Fizz'
            else:
                if c%5==0:
                    ans = 'Buzz'
                else:
                    ans = c
            break
    print(ans)
solve()