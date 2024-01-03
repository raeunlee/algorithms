from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    for p in permutations(dungeons, len(dungeons)):
        tmp = k
        count = 0
        for i in p:
            if tmp >= i[0]:
                tmp -= i[1]
                count += 1
                
        answer = max(answer, count)
                

    return answer