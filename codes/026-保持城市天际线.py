"""
在二维数组grid中，grid[i][j]代表位于某处的建筑物的高度。 我们被允许增加任何数量（不同建筑物的数量可能不同）的建筑物的高度。 高度 0 也被认为是建筑物。

最后，从新数组的所有四个方向（即顶部，底部，左侧和右侧）观看的“天际线”必须与原始数组的天际线相同。 城市的天际线是从远处观看时，由所有建筑物形成的矩形的外部轮廓。 请看下面的例子。

建筑物高度可以增加的最大总和是多少？
"""


class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_row = [max(col) for col in grid]  # 水平天际线
        max_col = []  # 竖直天际线
        size = len(grid)
        for i in range(size):
            col = []
            for g in grid:
                col.append(g[i])
            max_col.append(max(col))

        addition = 0
        for i in range(size):
            for j in range(size):
                addition += min(max_row[i], max_col[j]) - grid[i][j]

        return addition


if __name__ == '__main__':
    s = Solution()
    s.maxIncreaseKeepingSkyline([[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]])
