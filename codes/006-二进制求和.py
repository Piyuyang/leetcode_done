# -*- coding:utf-8 -*-

# 给定两个二进制字符串，返回他们的和（用二进制表示）。
# 输入为非空字符串且只包含数字 `1` 和 `0`。
# 输入: a = "11", b = "1"
# 输出: "100"
# 输入: a = "1010", b = "1011"
# 输出: "10101"
a = "1010"
b = "1011"


def add_binary(a, b):
    # 1 内置函数法1
    # return bin(int(a, 2) + int(b, 2))[2:]

    # 2 内置函数法2
    # a = a.rjust(max(len(a), len(b)), '0')
    # b = b.rjust(max(len(a), len(b)), '0')
    # res = list(str(eval(a) + eval(b)))
    # for i in range(len(res)-1, -1, -1):
    #     if res[i] == '2':
    #         res[i] = '0'
    #         if i != 0:
    #             res[i-1] = str(eval(res[i-1])+1)
    #         else:
    #             res.insert(0, '1')
    # return eval(''.join(res))

    # 3 暴力法
    a = a.rjust(max(len(a), len(b)), '0')
    b = b.rjust(max(len(a), len(b)), '0')
    res = ''
    flag = 0
    for i in range(len(a)-1, -1, -1):
        tmp = int(a[i]) + int(b[i]) + flag
        res = str(tmp % 2) + res
        flag = tmp // 2
    if flag == 1:
        res = '1' + res
    return res


print(add_binary(a, b))
