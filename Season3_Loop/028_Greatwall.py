inp = input().split()
countup = 1
countdown = 1
i = 0
up = []
down = []
while i<len(inp)-1:
    if inp[i]<inp[i+1]:
        countup += 1
        down.append(countdown)
        countdown = 1
    elif inp[i]>inp[i+1]:
        countdown += 1
        up.append(countup)
        countup = 1
    i += 1
print(up,down)
for i in range(len(up)):
    if up[i] == 1:
        up.pop(i)
for i in range(len(down)):
    if down[i] == 1:
        down.pop(i)
print(up,down)