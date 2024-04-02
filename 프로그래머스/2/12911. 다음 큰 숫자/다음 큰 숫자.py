# 전부다 1이고, 19자리 이하일 경우는 맨 앞 0으로 바꾸고, 그 앞에 1 추가
# 1,000,000 이면 20자리임,,
# 전부다 1이 아닐 경우 1011 -> 1110, 1110 이런거 -> 1101
# 1001110 -> 1010011 
# 오른쪽 0이면 끝에 모든 1들은 오른쪽으로, 하나는 옆으로
# 오른쪽 1이면 
# 1111 -> 10111
def solution(n):
    answer = 0
    origin = list(bin(n))
    origin_cnt = 0 # 1의 개수
    print(list(origin))
    for o in origin:
        if o == '1':
            origin_cnt += 1
    print(origin_cnt)
    
    for i in range(n+1, n + 17):
        # print(i)
        now = list(bin(i))
        now_cnt = 0
        for n in now:
            if n == '1':
                now_cnt += 1
        if origin_cnt == now_cnt:
            answer = i
            break
 

            
    
    return answer