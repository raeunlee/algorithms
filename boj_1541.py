arr=input().split('-')
# arr[0]에는 일단 -가 포함되어 있찌 않음
s = 0

for i in arr[0].split('+'): #-가 없는 arr[0]을 다 더하기
    s += int(i)
    
for i in arr[1:]: #-를 기준으로 뒷부분
    for j in i.split('+'):
        s -= int(j) #다 더한것에서 다 빼줌 
        
print(s)
    
    
    