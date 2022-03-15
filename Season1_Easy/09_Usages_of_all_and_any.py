num = int(input())
a = [bin(int(input()))[2:] for i in range(num)]
strs =[]
strings = ','
for i in range(num):
    if all(a[i][j] == '1' for j in range(len(a[i]))):
        strs.append('True')
    else:
        strs.append('False')
print(strings.join(strs))