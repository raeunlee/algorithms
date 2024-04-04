def solution(n, stations, w):
    answer = 0
    last_covered = 0
    range_cover = 2 * w + 1 # 커버 가능한 구간

    for station in stations: 
        # 기지국을 중심으로 양쪽의 전파가 어디까지 가는지
        left_cover = max(station - w, 1)
        right_cover = min(station + w, n)
        # print(left_cover, right_cover)
        
        # left_cover가 1보다 크다면?
        if last_covered < left_cover - 1:
            # cover가 안된 구간 계산
            uncovered = left_cover - 1 - last_covered
            answer += (uncovered + range_cover - 1) // range_cover
        
        last_covered = right_cover
        
    if last_covered < n:
        answer += (n - last_covered + range_cover - 1) // range_cover 
        
    return answer