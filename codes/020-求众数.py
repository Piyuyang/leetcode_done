"""
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在众数。
"""
import collections


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 暴力
        # l = len(nums)/2
        # for n in nums:
        #     if nums.count(n) > l:
        #         return n

        # 中位数
        # nums.sort()
        # return nums[len(nums)//2]

        # 哈希表
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)


if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement([3, 2, 3]))
