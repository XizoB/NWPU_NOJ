num = input().split(' ')
num = [int(num[i]) for i in range(len(num))]
length = len(num)
sum = sum(num)
smallone = min(num)
bigone = max(num)
print("{},{},{},{}".format(length,bigone,smallone,sum))
for i in range(length):
    num[i] = abs(num[i])
num.sort()
print(num)