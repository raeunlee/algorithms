def solution(number, k):
    answer = ''
    tmp = []
    
    for n in number:
        #숫자 배열이 비어있으면 하나 넣어준다
        if len(tmp) == 0:
            tmp.append(n)
            continue
        if k > 0: #제거할 숫자가 0이상이면
            while tmp[-1] < n: # 맨 위가 현재 숫자보다 작다면
                tmp.pop()
                k -= 1 # 제거할 숫자도 줄어듦
                if len(tmp) == 0 or k == 0:
                    break #tmp가 0이거나 k가 0이면 break
        tmp.append(n)
        
    if k > 0:
        tmp = tmp[:-k]
    else:
        tmp
    return ''.join(tmp)
            