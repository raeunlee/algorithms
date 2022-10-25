n = int(input())
arr = list(map(int,input().split()))
count = 0
turn = 0
arr.sort(reverse=False)

for i in range(n):
    
    turn += arr[i]
    count += turn
    
print(count)
