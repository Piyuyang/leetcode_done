class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # return bin(n).count('1')

        res = 0
        while n:
            n &= (n-1)
            res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    # print(s.hammingWeight())
