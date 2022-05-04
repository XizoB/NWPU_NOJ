inp = input().split(" ")
inp = [int(inp[i]) for i in range(len(inp))]
trans = 0
max = 0
for i in range(len(inp) - 2):
    for j in range(i+1, len(inp)):
        trans = inp[i] + inp[j]
        if trans > max:
            max = trans
print(max)