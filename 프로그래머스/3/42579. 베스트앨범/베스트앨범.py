def solution(genres, plays):
    answer = []
    g_d = {}
    
    for i in range(len(genres)):
        if genres[i] in g_d:
            g_d[genres[i]] += plays[i]
        else:
            g_d[genres[i]] = plays[i]

    g_d_sorted = sorted(g_d.items(), key = lambda item: item[1], reverse = True)
    
    for each in g_d_sorted:
        tmp = []
        for i in range(len(genres)):
            if each[0] == genres[i]:
                tmp.append([i, plays[i]])
        tmp_sorted = sorted(tmp, key = lambda x: x[1], reverse = True)
        count = 0
        for i in range(len(tmp_sorted)):
            if count >= 2:
                break
            answer.append(tmp_sorted[i][0])
            count += 1
                
    
    
    return answer