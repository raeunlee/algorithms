def change(x):
    if switch[x] == 0:
        switch[x] = 1
    else:
        switch[x] = 0
    return


n = int(input())
#스위치는 1번부터시작함
switch = [0] + list(map(int,input().split()))
m = int(input())

for _ in range(m):
    sex, num = map(int,input().split())
    if sex == 1: #man
        for i in range(num, n+1, num): #받은 수 부터 끝까지 num만큼만 이동
            change(i)
    elif sex == 2: #woman
        change(num) #자기 자신 반전

        for i in range(n//2): # 절반 만큼 탐색
            if num+i>n or num-i<1: break #범위 벗어나면 break
            if switch[num+i] == switch[num-i]: #대칭된 자리의 값이 같으면
                change(num+i)
                change(num-i)
            else: #좌우 다르면 break
                break

for i in range(1, n+1):
    print(switch[i], end = ' ')
    if i % 20 == 0:
        print() #20개마다 한줄띄워주기