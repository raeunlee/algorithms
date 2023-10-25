from collections import defaultdict
def solution(keymap, targets):
    answer = []
    data = defaultdict(list)
    for key in keymap:
        for i, k in enumerate(key): # 인덱스와 요소 한번에 가져옴
            if data[k] == []:
                data[k] = i+1
            
            elif data[k] != [] and (i+1) < data[k]:
                data[k] = i+1
    

    for target in targets:
        values = 0
        for t in target:
            if data[t] == []:
                values = -1
                break
            values += data[t]
        answer.append(values)
    return answer