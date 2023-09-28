def solution(n):
    answer = [[0] * n for i in range(n)]    
    # 우 하 좌 상 
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dir = 0
    x, y = 0,0 #시작 좌표
    
    
    for i in range(1, (n*n)+1):
        answer[y][x] = i
        nx = x + dx[dir] #다음좌표
        ny = y + dy[dir] #다음좌표
        
        #다음좌표가 벽에걸리거나 숫자가 차있거나 등등이면
        if nx<0 or ny<0 or nx>=n or ny>=n or answer[ny][nx] != 0:
            dir = (dir+1)%4 #0,1,2,3 순서 우하좌상 순서 
            nx = x + dx[dir]
            ny = y + dy[dir] 
            #바뀐 방향으로 다음좌표 재설정
        
        #바뀐좌표로 다시 반복
        x = nx
        y = ny

    return answer