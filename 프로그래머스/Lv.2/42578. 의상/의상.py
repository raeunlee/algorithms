def solution(clothes):
    
    # 옷장 딕셔너리
    closet = {} 
    
    for name, kind in clothes:
        if kind in closet.keys():
            closet[kind] += [name]
        else:
            closet[kind] = [name]

    answer = 1
    
    # 종류, 의상
    for k , value in closet.items():
        answer *= (len(value) + 1)
    
    return answer - 1

