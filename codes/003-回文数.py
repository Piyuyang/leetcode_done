# -*- coding:utf-8 -*-
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。


def ispalindrome(x):
    if str(x)[::-1] == str(x):
        return True
    else:
        return False


ispalindrome(12321)