def solution(picture, k):
    answer = []
    for line in picture:
        for _ in range(k):
            answer.append(''.join(char * k for char in line))
    return answer