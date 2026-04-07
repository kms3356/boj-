import sys

def solve():
    input_data = sys.stdin.read().split()
    
    n = int(input_data[0])
    target_sequence = list(map(int, input_data[1:]))
    
    stack = []
    result = []
    current_num = 1  
    possible = True
    
    for target in target_sequence:
        while current_num <= target:
            stack.append(current_num)
            result.append("+")
            current_num += 1
        
        if stack[-1] == target:
            stack.pop()
            result.append("-")
        else:
            possible = False
            break

    if possible:
        print("\n".join(result))
    else:
        print("NO")

solve()