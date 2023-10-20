import sys
input = sys.stdin.readline
m, n = map(int, input().split())

dict = {}
for i in range(m):
    tmp = input().rstrip()
    if len(tmp) >= n: # 길이가 n이상일때 
        if tmp in dict:
            dict[tmp] += 1
        else:
            dict[tmp] = 1

sorted_dict = sorted(dict.items(), key = lambda x: (-x[1],-len(x[0]), x[0]))
# print(sorted_dict)

for items in sorted_dict:
    print(items[0])