n = int(input())
student=[]
for _ in range(n):  
    student.append(input().split())
student.sort(key = lambda x : ( -int(x[1]), int(x[2]), -int(x[3]), x[0]))

for s in student:
    print(s[0])