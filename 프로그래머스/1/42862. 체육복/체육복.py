def solution(n, lost, reserve):

    set_reserve = set(reserve) - set(lost) #여분 있는 애
    set_lost = set(lost) - set(reserve) #도난당한애
    
    for i in set_reserve: 
        if i-1 in set_lost: #앞번호 분실
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    
        
    return n-len(set_lost)