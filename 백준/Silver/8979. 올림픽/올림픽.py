n, k = map(int, input().split())
team = []

for _ in range(n):
     team.append(list(map(int, input().split())))


sort_team = sorted(team, key = lambda x : (-x[1], -x[2], -x[3]))    

for i in range(n):
    if sort_team[i][0] == k:
        idx = i #구하려는 팀의 등수
for i in range(n): #해당 팀의 점수가 다른 팀의 점수와 같으면? 다른팀 점수 + 1
    if sort_team[idx][1:] == sort_team[i][1:]:
        print(i+1)
        break
        
