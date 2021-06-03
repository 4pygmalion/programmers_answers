# Q3 H-index

def solution(citations):

    from collections import Counter
    
    cnt = Counter(citations)
    
    for h in range(max(cnt.keys()), 0, -1):
        n_cit = sum([v for k, v in cnt.items() if k >= h])
        
        if h <= n_cit:
            return h
        
    return 0
