"""
给定一个整数 n，返回 n! 结果尾数中零的数量

输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。

输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.
"""


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # res = 1
        # for i in range(1, n + 1):
        #     res *= i
        # zero = 0
        # ten = 10
        # while res % ten == 0:
        #     zero += 1
        #     ten *= 10
        # return zero

        # 乘数中包含几个5，结果的尾数中就有几个0
        re = 0
        while n >= 5:
            n //= 5
            re += n
        return re


if __name__ == '__main__':
    re = 1
    for i in range(1, 36):
        re *= i
    print(re)

    s = Solution()
    print(s.trailingZeroes(35))
