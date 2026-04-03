import sys
input_data = iter(sys.stdin.read().split())

N = int(next(input_data))
stack = []
res = []
for _ in range(N):
    op = next(input_data)
    match op:
        case "push": stack.append(next(input_data))
        case "pop" : res.append(stack.pop() if stack else '-1')
        case "size" : res.append(str(len(stack)))
        case "empty" : res.append('0' if stack else '1')
        case "top" : res.append(stack[-1] if stack else '-1')

print('\n'.join(res))