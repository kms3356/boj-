import numpy as np
def solution(arr, k):
    ar = np.array(arr)
    
    return (ar * k if k&1 else ar + k).tolist()