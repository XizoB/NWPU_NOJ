num = int(input())
a = 1
sum = -1
for i in range(num):
    a += 10**i
    sum += a
print(sum)