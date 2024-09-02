from collections import deque

def solution(land):
    answer = 0
    
    # 차례로 열과 행
    n, m = len(land), len(land[0])
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    visited = [[False] * m for _ in range(n)]
    # 각 열의 기름의 총량을 저장 (가로)
    oil = [0] * m
    
    def bfs(a, b):
        q = deque()
        q.append((a, b))
        visited[a][b] = True
        cnt = 1
        # 중복방지 - 열
        oil_covered = {b}
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and land[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    cnt += 1
                    # 석유 발견한 열 추가
                    oil_covered.add(ny)
                    
        for c in oil_covered:
            oil[c] += cnt
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                bfs(i, j)

    answer = max(oil)
    
    return answer
