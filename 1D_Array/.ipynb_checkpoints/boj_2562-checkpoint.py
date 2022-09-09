#2562 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
#첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.

arr1 = []
n = 9
for i in range(n):
    arr1.append(int(input()))

x = max(arr1)
y = arr1.index(x)   
print(x)
print(y+1)

'''모범답안
num_list = []
for i in range(9) :
    num_list.append(int(input()))  			## num_lst 안에 입력된 값들 차례대로 넣기

print(max(num_list))						## max라는 메소드를 이용해 num_lst 내의 최댓값 출력하기
print(num_list.index(max(num_list))+1)
'''