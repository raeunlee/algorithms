def solution(name):
    answer = 0
    n = len(name)  # 이름의 길이
    
    # 위, 아래 움직임 계산
    for i in range(n):
        # 'A'에서 해당 문자로 가는 가장 가까운 거리 계산
        #  A 에서 아래쪽으로 이동(+1)하면 Z로 이동가능
        up_down = min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
        answer += up_down  # 위아래로 움직인 횟수 더하기
    
    # 좌우 움직임! 오른쪽으로 갈거냐, 왼쪽으로 갈거냐
    move = n - 1 # 오른쪽으로 간다고 가정한다
    for i in range(n):
        next_idx = i + 1
        # A가 있으면 움직이지 않아도 되므로 i를 움직인다
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
        # 좌우 이동 거리 중 가장 적은 걸 선택
        # i + n - next_idx : 현재 위치에서 반대방향으로 돌아가는 경우
        # i 앞으로 가는경우
        # n - next_idx 그냥 뒤로 가는 경우
        move = min(move, i + n - next_idx + min(i, n - next_idx))
    
    answer += move  # 좌우로 움직인 횟수 더하기
    
    return answer
