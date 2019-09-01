# -*- coding:utf-8 -*-
# 实现 int sqrt(int x) 函数。
# 计算并返回 x 的平方根，其中 x 是非负整数。
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。


def sqrt(x):
    # 二分查找
    # left = 0
    # right = x // 2 + 1  # 保证取值
    # while left <= right:
    #     mid = (left + right) // 2
    #     if x == mid ** 2:
    #         return mid
    #     elif x < mid ** 2:
    #         right = mid - 1
    #     else:
    #         left = mid + 1
    # return right

    # 牛顿迭代
    if x == 0:
        return 0
    cur = 1
    while True:
        pre = cur
        cur = (cur + x/cur)/2
        if abs(cur - pre) < 1e-6:
            return int(cur)


print(sqrt(9))
