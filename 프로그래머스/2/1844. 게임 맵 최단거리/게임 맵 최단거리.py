from collections import deque

def solution(maps):
    r = len(maps)
    c = len(maps[0])

    queue = deque()
    queue.append([0,0])        
    while queue:
        # x(행),y(열) 좌표 받기
        x,y = queue.popleft()

        # 방향 벡터(상,하,좌,우)로 탐색
        dx = [1,-1,0,0]
        dy = [0,0,-1,1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나는 경우 무시
            if nx < 0 or ny < 0 or nx >= r or ny >= c: 
                continue
            # 벽인 경우 무시
            if maps[nx][ny] == 0: 
                continue
            # 방문한 적이 없는 경우에만
            if maps[nx][ny] == 1:
                # 이전 좌표값 +1
                maps[nx][ny] = maps[x][y] + 1
                # 큐에 새로 추가
                queue.append([nx,ny])

    # 상대 진영에 방문한 적이 없다면
    if maps[r-1][c-1] == 1: return -1
    # 상대 진영에 방문했다면 기록 반환
    else: return maps[r-1][c-1]
