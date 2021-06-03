# Q1. k-th element 

def solution(array, commands):
    ''' get k-th element from given window
    Parameters
    ----------
    commands: list
    
    return
    ------
    array: list
    '''
    answer = []
    
    for com in commands:
        start_idx, end_idx, return_idx = com[0], com[1], com[2]
        return_v = sorted(array[start_idx-1:end_idx])[return_idx-1]
        answer.append(return_v)
    
    return answer
  
 
