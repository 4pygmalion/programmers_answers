def solution(n, lost, reserve):
    
    _lost = list(set(lost) - set(reserve))
    _reserve = list(set(reserve) - set(lost))
    

    for i in sorted(_reserve):
        if i-1 in _lost:
            _lost.remove(i-1)
        elif i+1 in _lost:
            _lost.remove(i+1)

    return n - len(_lost)
