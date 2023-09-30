from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]
dq=deque() 

def bfs(i,j):
    dq.append([i,j])
    while dq:
        i,j=dq.popleft()
        for k in range(4):
            nx=i+dx[k]
            ny=j+dy[k]
            if 0<=nx<N and 0<=ny<M and place[nx][ny]==1:
                dq.append([nx,ny])
                place[nx][ny]=0
                

for _ in range(int(input())):
    M,N,K=map(int,input().split())
    place=[[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x,y=map(int,input().split())
        place[y][x]=1 # 좌표 
    cnt=0
    for i in range(N):
        for j in range(M):
            if place[i][j]==1:
                place[i][j]=0
                bfs(i,j)
                cnt+=1
    print(cnt)