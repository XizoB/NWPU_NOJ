nums = input().split(" ")
ans = 0
start = 0
out = 0
up = []
#贪心法
for i in range(len(nums)):
    if i > 0 and nums[i] <= nums[i - 1]:
        start = i
        up.append(start)
    #ans = max(ans, i - start + 1)
for i in range(len(up)):
    if i > 0 and (up[i] - up[i-1])>1:
        out = max(up[i-1]+1-ans, out)
        ans = up[i-1]
print(out)