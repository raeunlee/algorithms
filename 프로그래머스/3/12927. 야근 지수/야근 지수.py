import heapq

def solution(n, works):
    
    # 최대 힙을 사용하기 위해 음수로 변환하여 힙에 넣기
    arr = []
    for work in works:
        arr.append(-work)
    
    heapq.heapify(arr)  # 리스트를 힙 구조로 변환
    print(arr)
    
    # n 동안 가장 큰 작업량을 줄이기
    for _ in range(n):
        if arr[0] == 0:  # max가 0이면 break
            break
        max_work = -heapq.heappop(arr)  # 가장 큰 값
        max_work -= 1  # 작업량을 1 줄임
        heapq.heappush(arr, -max_work)  # 다시 음수로 변환하여 넣기

    total = 0 
    for work in arr:
        total += work * work

    return total



 