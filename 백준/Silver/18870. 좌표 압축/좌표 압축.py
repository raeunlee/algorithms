n = int(input())
l = list(map(int, input().split()))
sort_l = sorted(list(set(l)))

dic = {}
for i in range(len(sort_l)):
    dic[sort_l[i]] = i
for i in l:
    print(dic[i], end=' ')  

