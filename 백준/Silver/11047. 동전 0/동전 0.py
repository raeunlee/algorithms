n, k = map(int, input().split())
coin = []
count = 0 

for i in range(n):
    coin.append(int(input())) #동전을 차례로 입력받기 1, 5, 10, 50,,,
    
for j in reversed(range(n)): #처음써보는 reversed 세상 좋아짐
    count += k // coin[j] # 제일큰 동전부터 시작하여 K가 나누어지면 count해준다. count는 계속 쌓임
    k = k%coin[j] # 위에서 나눈 동전의 나머지로 리셋
   #이걸 n번 만큼 반복함
print(count)
    