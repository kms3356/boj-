import itertools

def fast_simul(po, cur):
    """문자열 연산 없이 튜플 형태로 (Strike, Ball)을 반환하여 속도를 극대화"""
    s = 0
    b = 0
    for i in range(4):
        if cur[i] == po[i]:
            s += 1
        elif cur[i] in po:
            b += 1
    return (s, b)

def solution(n, submit):
    # 1. 1~9로 이루어진 서로 다른 4자리 수 3024개 생성
    all_perms = list(itertools.permutations(range(1, 10), 4))
    nums = all_perms[:]
    
    # 첫 번째 제출은 연산 시간을 벌기 위해 가장 이상적인 수(1234)로 고정
    cur = (1, 2, 3, 4)
    
    while True:
        # 튜플 (1, 2, 3, 4) -> 정수 1234 로 변환 (join보다 훨씬 빠름)
        cur_int = cur[0]*1000 + cur[1]*100 + cur[2]*10 + cur[3]
        result = submit(cur_int)
        
        if result == "4S 0B":
            return cur_int
            
        # 서버가 준 "1S 2B" 같은 문자열을 (1, 2) 튜플로 변환
        s_str, b_str = result.split("S ")
        target_res = (int(s_str), int(b_str.replace("B", "")))
        
        # 2. 결과와 일치하지 않는 후보는 모두 제거
        nums = [po for po in nums if fast_simul(po, cur) == target_res]
        
        # 후보가 하나만 남았다면 다음 턴에 바로 제출
        if len(nums) == 1:
            cur = nums[0]
            continue

        # 3. Minimax (최악의 경우 최소화) - 서버의 꼼수 차단
        best_guess = None
        min_max_size = float('inf')
        
        nums_set = set(nums) # 검색 속도 향상을 위한 set
        
        # 핵심: 남은 후보(nums) 안에서만 질문을 찾는 게 아니라, 
        # 전체 3024개(all_perms) 중에서 남은 후보를 가장 잘게 쪼개는 '완벽한 질문'을 찾습니다.
        for g in all_perms:
            counts = {}
            for cand in nums:
                res = fast_simul(cand, g)
                counts[res] = counts.get(res, 0) + 1
            
            if not counts:
                continue
                
            # g를 제출했을 때, 서버가 도망갈 수 있는 가장 큰 덩어리의 크기
            max_size = max(counts.values())
            
            if max_size < min_max_size:
                min_max_size = max_size
                best_guess = g
            elif max_size == min_max_size:
                # 최대 남은 개수가 같다면, 실제 정답일 가능성이 있는(nums에 있는) 숫자를 우선 선택
                if g in nums_set and best_guess not in nums_set:
                    best_guess = g
                    
        cur = best_guess