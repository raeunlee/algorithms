
N, d, k, c = map(int, input().split())
arr = []
for i in range(N):
    arr.append(int(input()))
# print(arr)

#원형
arr = arr + arr[:k-1]

ans = 0

for i in range(N):
    tmp = set(arr[i:i+k])
    
    if c not in tmp:
        tmp.add(c)
        
    ans = max(ans, len(tmp))
            
        
print(ans)