def solution(brown, yellow):
    answer = []    
    gx = 0
    gy = 0
    
    #갈색카펫 가로는 최소 3부터 brown /2 - 1 이 최대
    for i in range(3, int(brown/2)):
        gx = i #갈색 가로        
        
        #세로는 가로길이 만큼이 최대
        for j in range(1, gx+1):
            gy = j
            
            brown_gatsu = gx*2 + gy*2 - 4 # 갈색 갯수
            yellow_gatsu = (gx-2) * (gy-2)
            all_gatsu = brown_gatsu + yellow_gatsu
            
            if brown_gatsu == brown and yellow_gatsu == yellow:
                if all_gatsu == brown + yellow:
                    print("yes")
           
                    answer.append(gx)
                    answer.append(gy)

    return answer