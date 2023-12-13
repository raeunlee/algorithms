n, m = map(int, input().split())
ns = []
ms = []
for i in range(n):
    ns.append(input())
for i in range(m):
    ms.append(input())
    
intersection = list(set(ns) & set(ms))
intersection.sort()
print(len(intersection))
for i in range(len(intersection)):
    print(intersection[i])