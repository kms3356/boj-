def solution(s):
    x = s[0]
    count = 1
    answer = 1
    for i in range(1, len(s)):
        if x == s[i]:
            count += 1
        else:
            count -= 1
            if count == 0:
                
                count = 0
                if i < len(s)-1:
                    x = s[i+1]
                    answer += 1
    return answer

print(solution('aaabbaccccabba'))
