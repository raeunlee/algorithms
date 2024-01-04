
def solution(n, times):
    times.sort()
    left = times[0] # 최소
    right = max(times) * n # 최대 
    
    while left <= right:
        
        # 중간값
        mid = (left + right) // 2 
        # 심사한 사람의 수
        p = 0
        
        for t in times: 
            # 주어진 시간동안 심사 받은 수 더해주기
            p += mid // t
            # 만약 n명보다 많이 심사했다면 종료
            if p >= n:
                break
                
        # n명을 초과하면 시간이 너무 많은 것
        if p >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
        
    return answer