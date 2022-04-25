inp = int(input())
older = 0
old = 1
for i in range(inp):
    sum = old + older
    older = old
    old = sum
print(sum)