sum = 0
for i in range(100, 201):
    for j in range(2, i):
        if i%j==0:
            break
        elif j==i-1:
            sum += i
print(sum)