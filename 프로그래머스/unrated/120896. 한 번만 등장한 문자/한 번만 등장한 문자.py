from collections import Counter

def solution(s):
    answer = '' 
    cnt = Counter(s)
    for i in range(len(s)):
        if cnt[s[i]] == 1:
            answer += s[i]
            
    ans = ''.join(sorted(answer))
    
    return ans