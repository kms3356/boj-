import re

def solution(myStr):
    answer = [cur for cur in re.split('[abc]+', myStr) if cur]
    
    return answer if answer else ["EMPTY"]