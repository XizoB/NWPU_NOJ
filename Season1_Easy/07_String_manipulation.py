length = int(input())
a = [input() for i in range(length)]
length, count = len(a[0]), len(a)
for i in range(length):
    c = a[0][i]
    if any(i == len(a[j]) or a[j][i] != c for j in range(1, count)): # 寻找最长公共前缀
        if i == 0:
            print('None')
        else:
            print(a[0][:i])
        break