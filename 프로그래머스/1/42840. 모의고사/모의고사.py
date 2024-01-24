def solution(answers):
    answer = []    
    no1 = [1,2,3,4,5]
    no2 = [2,1,2,3,2,4,2,5]
    no3 = [3,3,1,1,2,2,4,4,5,5]  
    scores = [0, 0, 0]

    for i in range(len(answers)):
        if no1[i % 5] == answers[i]:
            scores[0] += 1
        if no2[i % 8] == answers[i]:
            scores[1] += 1
        if no3[i % 10] == answers[i]:
            scores[2] += 1

    max_score = max(scores)

    for i, score in sorted(enumerate(scores, start=1), key=lambda x: x[1], reverse=True):
        if score == max_score:
            answer.append(i)

    return answer