def solution(ingredient):
    count = 0
    stack = []
    
    for i in ingredient:
        stack.append(i)
        
        if stack[-4:] == [1, 2, 3, 1]:
            count += 1
            del stack[-4:] 
            
    return count
        
                