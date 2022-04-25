import copy
import random
class Solution:
    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        self.nums = self.nums.copy().copy()
        return self.nums

    def shuffle(self):
        for i in range(len(self.nums)):
            j = random.randrange(i, len(self.nums))
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums


nums = [i for i in range(3)]
sh = Solution(nums)
for i in range(6):
    #a = sh.reset()
    a = sh.shuffle()
    print(a)

# def permutations(arr, position, end):
#     if position == end:
#         print(arr)
#     else:
#         for index in range(position, end):
#             arr[index], arr[position] = arr[position], arr[index]
#             permutations(arr, position + 1, end) # 递归调用
#             arr[index], arr[position] = arr[position], arr[index]  # 还原到交换前的状态，为了进行下一次交换
 
 
# arr = [1, 2, 3]
# permutations(arr, 0, len(arr))

# import itertools
# n=3
# a=[str(i) for i in range(n)]
# s=""
# s=s.join(a)
# print(s)
# s = '021'
# for i in itertools.permutations(s,2):
#     print (''.join(i))

# import itertools
# n=3
# a=[str(i) for i in range(n)]
# s=""
# s=s.join(a)
# for i in itertools.combinations(s,2):
#     print (''.join(i))


visit = [True, True, True]
temp = ["" for x in range(0, 3)]

 
def dfs(position):
    # 递归出口
    if position == 2:#len(arr):
        print(temp)
        return
    # 递归主体
    for index in range(0, len(arr)):
        if visit[index] == True:
            temp[position] = arr[index]
            visit[index] = False  # 试探 
            dfs(position + 1)
            visit[index] = True  # 回溯。非常重要
 
 
arr = [1, 2, 3]
#dfs(0)