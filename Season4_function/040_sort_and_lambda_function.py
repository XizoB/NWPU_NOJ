inpt = input().split()
num = input().split()
def sortlambda(num, inpt):
    nums = [abs(int(num[i])-int(inpt[1])) for i in range(len(num))]
    sum = list(zip(num, nums))
    sum = sorted(sum, key=lambda x:x[1])
    output = [sum[i][0] for i in range(len(sum))]
    output = " ".join(output)
    return output
output = sortlambda(num, inpt)
print(output)
# 1 2 3 4 5 6 7 8 9