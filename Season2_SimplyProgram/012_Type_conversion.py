data = input().split()
sum = 0
true = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
for i in range(len(data)):
    if data[i].count('.') == 1 and set(data[i])-{'.'}-true == set() and true&set(data[i]) != set(): #, true&set(data[i]) != set()
        data[i] = float(data[i])
    elif true&set(data[i]) != set() and set(data[i])-true == set():
        data[i] = int(data[i])
    else:
        data[i] = data[i]
        continue
    sum += data[i]
print(data)
print(sum)