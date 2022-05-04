num = input().split()
inpt = input()
def findindex(num, inpt):
    if inpt in num:
        output = num.index(inpt)
    else:
        output = -1
    return output
output = findindex(num, inpt)
print(output)
# -1 0 3 5 9 12