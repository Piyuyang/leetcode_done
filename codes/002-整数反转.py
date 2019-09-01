# -*- coding:utf-8 -*-
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
# ​	注意：假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。
# 请根据这个假设，如果反转后整数溢出那么就返回 0。


def reverse(x):
    # 转为正数，简化代码
    y, res = abs(x), 0
    flag = (1<<31)-1 if x>0 else 1<<31
    while y:
        res = res*10 + y%10
        if res > flag:
            return 0
        y = y//10
    return res if x>0 else -res


reverse(123)