def solution(brown, yellow):
    answer = []
    
    total = brown + yellow
    
    for sero in range(1, brown//2 + 1):
        if total % sero == 0:
            garo = total // sero
            if (garo - 2) * (sero - 2) == yellow:
                if garo >= sero:
                    answer.append(garo)
                    answer.append(sero)
    return answer
