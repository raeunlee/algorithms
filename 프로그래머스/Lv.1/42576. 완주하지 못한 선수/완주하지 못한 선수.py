def solution(participant, completion):
    answer = ''
    
    participant.sort()
    completion.sort()
    
    #순서대로 탐색했을 때, 발견하면 그 이름 return
    for i in range(len(completion)):
        if completion[i] != participant[i]:
            answer += participant[i]
            break
    
    if answer == '':
        answer += participant[-1]
        
    return answer