#회의실배정 1931

n = int(input())
arr =[]

for i in range(n):
    start, end = map(int, input().split())
    arr.append([start, end])

arr = sorted(arr, key=lambda a: a[0])
# 시작 시간을 기준으로 오름차순
arr = sorted(arr, key=lambda a: a[1])
# 끝나는 시간을 기준으로 오름차순

last = 0 #회의의 마지막 시간
count = 0 #회의 개수

for x,y in arr:
    if x>= last: #시작시간이 회의의 마지막 시간보다 크거나 같으면
        count += 1
        last = y
print(count)
        
    
    
