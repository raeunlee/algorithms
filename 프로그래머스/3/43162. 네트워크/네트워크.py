def solution(n, computers):
    network = 0
    visited = [False for i in range(n)]
    for num in range(n):
        if visited[num] == False:
            DFS(n, computers, num, visited)
            network +=1
    return network
            
def DFS(n, computers, num, visited):
    visited[num] = True
    for cnt in range(n):
        if num!=cnt and computers[num][cnt]==1:
            if visited[cnt]==False:
                DFS(n, computers, cnt, visited)