def solution(board):
    n = len(board)
    dx = [-1,1,0,0,-1,-1,1,1]
    dy = [0,0,-1,1,-1,1,-1,1]
    
    boom =[]

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                boom.append((i,j)) # 지뢰
    
    # 지뢰 주변 8개에 폭탄 설치해서 인덱스 1로 바꾸기            
    for x,y in boom:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                board[nx][ny] = 1
    
    # 탐색해서 0인거만 카운트
    answer = 0
    for x in range(n):
        for y in range(n):
            if board[x][y] == 0:
                answer += 1

    return answer