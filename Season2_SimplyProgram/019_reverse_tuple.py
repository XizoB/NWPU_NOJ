inpt = input().split(' ')
output = []
for i in range(len(inpt)):
    output.append(int(inpt[i]) + int(inpt[len(inpt)-1-i]))
print(tuple(output))