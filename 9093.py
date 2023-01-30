import sys
n = int(input())

# 파이썬에서 제공하는 reverse()

# n개만큼 반복
for _ in range(n):
    str = sys.stdin.readline().rstrip()
    # 문장마다 단어 split
    words = list(str.split())
    # 역으로 바꿔줄 리스트
    reverse = []
    
    # 단어 reverse, 파이썬 reverse기능으로!
    for word in words:
        reverse.append(word[::-1])
    
    answer = " ".join(reverse)
    print(answer)