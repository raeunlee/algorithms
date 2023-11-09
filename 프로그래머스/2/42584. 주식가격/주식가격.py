from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices) #주식가격을 큐에 넣는다
    
    while queue: #큐가 비기 전 까지 이를 반복한다
        sec = 0 #가격이 떨어지지 않는 시점 
        price = queue.popleft() #맨앞
        
        for q in queue: #큐 하나씩 
            sec += 1 #가격이 떨어지지 않은 시간
            if price > q: #맨앞보다 가격이 떨어지면 
                break
        answer.append(sec)
    
    return answer