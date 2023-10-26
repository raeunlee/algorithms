def solution(park, routes):

    n, m = len(park), len(park[0]) #세로, 가로
    dir = {"N":(-1,0), "S":(1,0), "W":(0,-1), "E":(0,1)}
    
    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                x, y = i, j
 
    for r in routes:
        op, can = r.split(" ")
        dx, dy = x, y
        for i in range(int(can)):
            nx = x + dir[op][0]
            ny = y + dir[op][1]
            if 0 <= nx < n and 0 <= ny < m and park[nx][ny] != 'X':
                x, y = nx, ny
            else: 
                x, y = dx, dy
                break
    return (x,y)