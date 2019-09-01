# -*- coding:utf-8 -*-
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
# 最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
digits = [1,2,3]
for i in range(len(digits)-1, -1, -1):
    digits[i] += 1
    digits[i] %= 10
    if digits[i] != 0:
        break
if digits[0] == 0:
    digits.insert(0,1)

print(digits)
