def solution(triangle):
    answer = 0
    
    
    for i in range(1, len(triangle)): # 둘째 줄부터 끝까지 
        for j in range(i+1):
            if j == 0: # j가 0이면..
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i - 1][j])
                
    return max(triangle[len(triangle)-1])
                
    

    return answer