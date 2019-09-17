"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
"""


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 若k大于n，取余数，节约步数
        k %= len(nums)
        for i in range(k):
            tmp = nums.pop()
            nums.insert(0, tmp)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    s = Solution()
    s.rotate(nums, 3)
    print(nums)
