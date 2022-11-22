# N과 M(1)

n, m = map(int,input().split())
# 수열이 담길 리스트 선언
s =[]
visited = [False] * (n+1)

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        dfs()
        s.pop()
        visited[i] = False
        
dfs()