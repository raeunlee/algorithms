from itertools import combinations

n, m = map(int, input().split())
arr= [list(map(int, input().split())) for _ in range(n)]
home = []
chicken = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1: #집
            home.append((i,j))
        elif arr[i][j] == 2: #치킨집
            chicken.append((i,j))


result = 1e9

for each in combinations(chicken, m): #치킨배열을 m개 조합
    dist = 0
    for h in home:
        home_dist = 1e9
        for k in each:
            home_dist = min(home_dist, abs(h[0]-k[0]) + abs(h[1]-k[1]))
        dist += home_dist
    result = min(result, dist)  
print(result)