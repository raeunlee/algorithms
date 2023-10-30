def solution(babbling):
    answer = 0
    for b in babbling:
        cnt = 0
        word = ''
        for i in b:
            word += i #한단어씩
            if word in ["aya", "ye", "woo", "ma"]:
                word = ''
                cnt += 1
        if len(word) == 0 and cnt > 0 :
            answer += 1

    return answer