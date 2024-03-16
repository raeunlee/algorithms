# 백준 리모콘

import sys
input = sys.stdin.readline

target = int(input())
n = int(input())
broken = []

if n != 0:
    broken = list(input().split())

# + , - 만 사용해서 이동하는 경우
count = abs(100-target)

#0부터 1000000 까지 모든 숫자를 탐색
for num in range(1000001):
   #문자열로 취급 (각 자리수에 접근하기 위함)
    for n in str(num):
        if n in broken: # 숫자가 고장난 번호면 break
            break
    # 고장난 버튼 없고 모든 자릿수 확인했다면?
    else:
        # 타겟까지 누르는데 필요한 횟수 + 현재 숫자의 자릿수
        count = min(count, abs(int(num) - target) + len(str(num)))

print(count)