# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
# 返回的下标值（index1 和 index2）不是从零开始的。

def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    left = 0
    right = len(numbers) - 1
    while left < right:
        sum = numbers[left] + numbers[right]
        if sum == target:
            return [left+1, right+1]
        elif sum > target:
            right -= 1
        else:
            left += 1


print(twoSum([2, 7, 11, 15], 9))
