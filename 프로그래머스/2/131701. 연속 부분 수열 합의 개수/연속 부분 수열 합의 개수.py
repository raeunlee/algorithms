def solution(elements):
    answer = 0
    num = []
    l = elements + elements 

    for i in range(1, len(elements) + 1):
        for j in range(0, len(elements)): 
            num.append(sum(l[j:j + i])) 
   
    answer = len(set(num))
    
    return answer
