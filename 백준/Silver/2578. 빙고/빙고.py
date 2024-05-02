# 빙고 판 입력 받기
arr = [list(map(int, input().split())) for _ in range(5)]

# 사회자가 부르는 숫자 입력 받기
speak = []
for _ in range(5):
    speak.extend(map(int, input().split()))

bingo = [[0] * 5 for _ in range(5)]

# 빙고 검사 함수
def check_bingo():
    count = 0
    # 가로, 세로 빙고 검사
    for i in range(5):
        if all(bingo[i][j] == 1 for j in range(5)):
            count += 1
        if all(bingo[j][i] == 1 for j in range(5)):
            count += 1
    
    # 대각선 빙고 검사
    if all(bingo[i][i] == 1 for i in range(5)):
        count += 1
    if all(bingo[i][4-i] == 1 for i in range(5)):
        count += 1
    
    return count >= 3

# 사회자의 숫자를 듣고 마킹, 빙고 검사
for index, number in enumerate(speak):
    found = False
    for i in range(5):
        for j in range(5):
            if arr[i][j] == number:
                bingo[i][j] = 1
                if check_bingo():
                    print(index + 1)
                    found = True
                    break
        if found:
            break
    if found:
        break

