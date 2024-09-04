def solution(s):
    n = len(s)
    min_length = n 
    
    for i in range(1, n//2 + 1):
        compressed = ""
        prev = s[:i]
        count = 1
        
        for j in range(i, n, i):
            nxt = s[j:j+i] # i 만큼 자른다
            if prev == nxt:
                count += 1
            else:
                if count > 1:
                    compressed += str(count) + prev
                else:
                    compressed += prev
                prev = nxt
                count = 1
        
        # 남는 부분
        if count > 1:
            compressed += str(count) + prev
        else:
            compressed += prev
            
        min_length = min(min_length, len(compressed))
        
    return min_length