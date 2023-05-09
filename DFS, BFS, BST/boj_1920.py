#BST 원하는 정수찾기 


N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())

target_list = list(map(int, input().split()))

for i in range(M):
    find = False #못찾음
    target = target_list[i] #찾아야하는 타겟 
    
    start = 0 #이진탐색 시작점
    end = len(A) - 1 
    
    while start <= end: #끝점이 시작점보다 작거나 같으면 
        midi = int((start+end) / 2) #중간점
        midv = A[midi] #중간노드
        
        if midv > target:
            end = midi - 1
        elif midv < target:
            start = midi + 1
        else: 
            find = True
            break
    
    if find:
        print(1)
    else:
        print(0)