n = int(input())

graph = [] 
for _ in range(n):
    graph.append(list(map(int, input().split())))

ans = []

for i in range(n):
    count = 0
    for j in range(n):
        if graph[i][0] < graph[j][0] and graph[i][1] < graph[j][1]: #자신보다 몸무게 키 모두 큰 사람의 수를 센다
            count += 1
    ans.append(count + 1)   #덩치는 자기보다 몸무게 키 큰 사람의 수 + 1 이다!

for num in ans:
    print(num, end=' ')
    