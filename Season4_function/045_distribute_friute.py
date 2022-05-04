num = input().split()
fruite = int(num[1])
nums = int(num[0])
child = [0]*nums
def distribute(child, fruite, nums, count = 1):
    while fruite >= count:
        i = count%nums-1
        child[i] += count
        fruite -= count
        count += 1
    child[i+1] += fruite
    return child
output = distribute(child, fruite, nums)
output = [str(output[i]) for i in range(len(output))]
print(" ".join(output))