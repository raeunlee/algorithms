from collections import deque


def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer
    
    q = deque()
    q.append([begin, 0]) #시작단어, 카운트
    
    while q:
        b, cnt = q.popleft()
        if b == target:
            return cnt
        for i in range(0, len(words)):
            different = 0
            word = words[i] #단어 하나하나
            for j in range(len(b)):
                if b[j] != word[j]:
                    different += 1 
            if different == 1:
                q.append([words[i], cnt+1])

    return cnt
        
    