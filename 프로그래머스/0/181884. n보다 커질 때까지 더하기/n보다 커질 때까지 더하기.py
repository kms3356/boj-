def solution(numbers, n):
    Sum = 0
    for s in numbers:
        Sum+=s
        if Sum > n:
            return Sum