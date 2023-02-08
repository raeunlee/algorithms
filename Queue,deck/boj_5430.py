from collections import deque

#testcase 
T = int(input())

#R,D
def R():
    arr.rotate(1)
def D():
    if deque:
        arr.popleft()
    else:
        print("error")

for i in range(T):
    #function
    p = list(str(input()))
    #num
    n = int(input())
    #array
    arr = deque(input())
    print(arr)
    
    for j in range(n):
        if arr[j] == 'R':
            R()
        elif arr[j] == 'D':
            D()
        else:
            continue
print(arr)
    
        
        
    
