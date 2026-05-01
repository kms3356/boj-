def solution(strArr):
    answer = [st.upper() if i&1==1 else st.lower() for i, st in enumerate(strArr) ]
    return answer