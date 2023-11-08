from collections import deque

def solution(begin, target, words):    
    if target in words: #target이 words에 있을 경우
        q = deque()
        q.append([begin, 0]) #시작단어, 카운트
        
        while q:
            b, cnt = q.popleft() #시작단어와 카운트 pop
            if b == target: #시작 단어가 타겟과 같으면
                return cnt #카운트 반환
            for i in range(0, len(words)):
                diff = 0 # 다른거 찾기
                word = words[i] # 한 단어씩
                for j in range(len(b)): #시작단어의 알파벳 하나씩 
                    if b[j] != word[j]: #한 단어의 알파벳 하나씩 
                        diff += 1
                if diff == 1: #다른 알파벳이 하나라면 
                    q.append([words[i], cnt+1]) #큐에 다시 넣어준다
        return cnt
        
    else:
        return 0

