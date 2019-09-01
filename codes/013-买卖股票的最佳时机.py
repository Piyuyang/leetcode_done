# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
# 注意你不能在买入股票前卖出股票。

# price = [7, 1, 5, 3, 6, 4]
# price = [7, 6, 4, 3, 1]
# price = []
# price = [2, 4, 1]
price = [3, 2, 6, 5, 0, 3]


def max_profit(prices):
    if len(prices) <= 1:
        return 0
    min_p = prices[0]
    max_p = 0
    for i in range(len(prices)):
        min_p = min(min_p, prices[i])
        max_p = max(max_p, prices[i] - min_p)
    return max_p


print(max_profit(price))
