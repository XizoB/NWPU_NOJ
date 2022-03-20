
inp = input()
num = []
data = []
for i in range(len(inp)//2 + 1):
    num.append(int(inp[2*i]))
num.sort()
setsum = set(num) # convert list to set
listnum = list(setsum) # convert set to list
for i in range(len(listnum)):
    take = listnum[i]
    count = 0
    for j in range(len(num)):
        if num[j] == take:
            count += 1
    data.append(count)
#listnum = [str(i) for i in listnum]
out = dict(zip(listnum,data))
print(out)

        
