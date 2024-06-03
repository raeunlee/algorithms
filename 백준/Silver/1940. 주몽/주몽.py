n = int(input())
m = int(input())
l = list(map(int, input().split()))

l.sort()
cnt = 0
i = 0
j = n-1

#두개의 재료로 만든다!
while i < j:
    #정렬 후 인접한 두개를 더해서 m이 되었을 경우? 카운트 증가, 범위를 좁혀준다
    if l[i] + l[j] == m:
        cnt += 1
        i += 1 
        j -= 1
    elif l[i] + l[j] < m: # m보다 작을 경우, i를 +1
        i += 1
    else: # 클 경우 j - 1
        j -= 1
print(cnt)
        