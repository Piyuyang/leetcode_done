# -*- coding:utf-8 -*-
def twoSum(nums, target):
    d_nums = dict()
    for index, value in enumerate(nums):
        sub = target - value
        # 根据后加入的数据找之前数据
        if sub in d_nums.keys():
            return [d_nums[sub], index]
        d_nums[value] = index
    else:
        return []


print(twoSum([1, 2, 3, 4], 7))
print(twoSum([1, 2, 2, 4], 4))
print(twoSum([3, 3], 6))
print(twoSum([1, 2], 6))
