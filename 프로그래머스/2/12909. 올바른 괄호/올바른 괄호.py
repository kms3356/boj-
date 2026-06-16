def solution(s):
    stack = []
    for cur in s:
        if cur == '(':
            stack.append(cur)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
    
    return True if not stack else False