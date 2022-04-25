
oldinp = input().split(' ')
limitinp = input().split(' ')
count = 0
oldinp = [int(oldinp[i]) for i in range(len(oldinp))]
limitinp = [int(limitinp[i]) for i in range(len(limitinp))]
for i in range(len(oldinp)-2):
    ii = oldinp[i]
    for j in range(i+1, len(oldinp)-1):
        jj = oldinp[j]
        for k in range(j+1, len(oldinp)):
            kk = oldinp[k]
            if abs(oldinp[i]-oldinp[j]) <= limitinp[0] and abs(oldinp[j]-oldinp[k]) <= limitinp[1] and abs(oldinp[i]-oldinp[k]) <= limitinp[2]:
                count += 1
print(count)