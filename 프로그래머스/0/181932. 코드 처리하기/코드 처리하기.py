def solution(code):
    mode = False
    ret = []
    for idx in range(len(code)):
        if code[idx] == '1':
            mode = not mode
            continue
        if not mode and idx & 1 == 0:
            ret.append(code[idx])
        elif mode and idx & 1 == 1:
            ret.append(code[idx])
    answer = ''.join(ret) if ret else 'EMPTY'
    return answer