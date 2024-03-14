# 1, 2번째 제외하고 3번째 부터는,, 
# 7
# 3   8
# 8   1   0
# 2   7   4   4
# 4   5   2   6   5
# 
# 밑으로 내려오면서 
# 0번째 순서는 그 위 0
# N번째 순서는 그 위 N-1
# 나머지 숫자들은 그 전줄 자기위치 -1과 자기위치 숫자중 더 큰것을 받는다
# 맨 마지막 줄에서 가장 큰 수를 print

n = int(input())
graph = []
for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

# graph[1][0] += graph[0][0]
# graph[1][1] += graph[0][0]

# 세번째 줄 부터 시작
for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            graph[i][j] += graph[i-1][j]
        elif j == len(graph[i]) - 1:
            graph[i][j] += graph[i-1][j-1]
        else: 
            graph[i][j] += max(graph[i-1][j-1], graph[i-1][j])

print(max(graph[n-1]))
