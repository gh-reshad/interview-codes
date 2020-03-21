# import numpy as np

# class Solution(object):
#     def __init__(self, num, target):
#         self.n = num
#         self.t = target
#         self.arr = []

#     def twoSum(self):

#         for i in range(len(self.n)):
#             j = i + 1
#             while(j < len(self.n)):
#                 sum = self.n[i] + self.n[j]
#                 if sum == self.t:
#                     self.arr.append(i)
#                     self.arr.append(j)
#                 j += 1

#         return self.arr

    



# num = [2, 8, 11, 15]
# target = 9
# c = Solution(num, target)
# res = c.twoSum()
# print(res)


class Solution(object):
    def twoSum(self, nums, target):
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]

nums = [2, 7, 11, 15]
target = 9
c = Solution()
res = c.twoSum(nums, target)
print(res)