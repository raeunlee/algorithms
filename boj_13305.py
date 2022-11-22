
# 도시의 수
n = int(input())
# 도시 사이의 거리 list
arr1=list(map(int, input().split()))
# 도시 당 기름 가격 list
arr2=list(map(int, input().split()))
# 총 요금
cost = 0
# 기준점이 되는 첫 도시를 min으로 설정
min_cost = arr2[0]

for i in range(len(arr1)):
    if arr2[i] >= min_cost: #첫도시보다 기름값이 비싸면
       cost+= min_cost * arr1[i] #첫도시값 * 거리
    else: #첫도시보다 기름값이 싸다면!
        min_cost = arr2[i] #이 도시를 min값으로 두고, 거리값곱하기
        cost += min_cost * arr1[i]
    
print(cost)

    