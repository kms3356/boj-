def solution(l, r):
    answer = []
    i = 1
    
    while True:
        # i를 이진수 문자열로 변환하고 '1'을 '5'로 바꿉니다.
        # bin(3) -> '0b11' -> [2:] 슬라이싱으로 '11' 추출 -> '55'
        num_str = bin(i)[2:].replace('1', '5')
        num = int(num_str)
        
        # 생성된 숫자가 r을 넘어가면 반복을 종료합니다.
        if num > r:
            break
            
        # l 이상 r 이하인 경우에만 배열에 추가합니다.
        if num >= l:
            answer.append(num)
            
        i += 1
        
    # 만약 배열이 비어있다면 [-1]을, 있다면 해당 배열을 반환합니다.
    return answer if answer else [-1]