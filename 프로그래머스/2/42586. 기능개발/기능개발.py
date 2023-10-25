def solution(progresses, speeds):
   
    result = []  # 각 배포마다 완료된 작업 수를 저장할 리스트

    while speeds:
        # 모든 작업 1일씩 업데이트
        for idx, speed in enumerate(speeds):
            progresses[idx] += speed
            print(progresses[idx])
        count = 0 

        # 작업물이 아직 있고, 맨 앞 작업물이 100일때
        while progresses and progresses[0] >= 100:
            # 맨 앞 작업물과 해당 속도 삭제 
            del progresses[0], speeds[0]
            count += 1 # 카운트 추가 
       
        # 배포될 작업 수를 결과 리스트에 추가
        if count > 0:
            result.append(count)

    return result
