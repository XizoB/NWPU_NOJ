inp = input()
a, b, c =0, 0, 0
for i in range(len(inp)):
    if inp[i]>="A" and inp[i]<="Z":
        a += 1
    if inp[i]>="a" and inp[i]<="z":
        b += 1
    if inp[i]>="0" and inp[i]<="9":
        c += 1
print(a,b,c)
