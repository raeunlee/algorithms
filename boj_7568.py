#덩치

n = int(input())

#키랑 몸무게
arr = [list(map(int, input().split())) for _ in range(n)]

#등수
grade = []

for i in range(n):
    count = 0
    for j in range(n):
        if arr[i][0] < arr [j][0] and arr[i][1] < arr[j][1]: # 몸무게와 키 모두 자신보다 큰 사람의 수를 센다
            count += 1 
    grade.append(count + 1) # 덩치 등수는 자신보다 몸무계 키 모두 큰 사람의 수 + 1 이므로 count + 1을 ans에 append한다.
 
for k in grade:
    print(k)