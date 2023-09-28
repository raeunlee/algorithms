def solution(N, stages):
    answer = {}
    length = len(stages)
    for i in range(1,N+1):
        if length!=0: #0은 ㄴㄴ
            answer[i] = stages.count(i)/length # 갯수/길이!! -> 확률
            length -= stages.count(i) #빼주고 다음꺼 계산
            print(answer[i])
        else:
            answer[i] = 0 #없으면 실패율 0
            
    answer = sorted(answer, key = lambda x: answer[x],reverse=True)
    return answer
