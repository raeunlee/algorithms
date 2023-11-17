N = input()

tmp1, tmp2 = 0, 0

for i in range(len(N)):
    if i < len(N)/2:
        tmp1 += int(N[i])
    else:
        tmp2 += int(N[i])
if tmp1 - tmp2 == 0:
    print("LUCKY")
else:
    print("READY")
