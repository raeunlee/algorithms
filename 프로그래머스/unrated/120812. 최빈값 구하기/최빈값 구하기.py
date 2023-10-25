from collections import defaultdict
def solution(array):
    answer = 0
    dd = defaultdict(int)
    
    for num in array:
        dd[num] += 1 #등장할 때 마다 +1
        
    maxNum = 0
    for key in dd:
        if dd[key] > maxNum:
            maxNum = dd[key]
            answer = key
        elif dd[key] == maxNum:
            answer = -1

    return answer

