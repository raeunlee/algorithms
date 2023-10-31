def solution(number, k):
    answer = ''
    tmp = [] # 만들 수 
    
    for n in number:
        if len(tmp) == 0: #비어있다면 넣어준다
            tmp.append(n)
            continue
        if k > 0:        
            while tmp[-1] < n: #맨 위가 number의 숫자 보다 작다면?
                tmp.pop()
                k -= 1
                if len(tmp) == 0 or k<=0:
                    break
        tmp.append(n)
    
    if k > 0:
        tmp = tmp[:-k] #스택 맨 위부터 차례로
        
        
    
    
   
    return ''.join(tmp)