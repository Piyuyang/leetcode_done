# 给定一个正整数，返回它在 Excel 表中相对应的列名称。
# A->1,B->2,Z->26,AA->27

# 二十六进制
def convertToTitle(n):
    """
    :type n: int
    :rtype: str
    """
    alpha = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    while n:
        n, rem = divmod(n, 26)
        if rem == 0:
            rem = 26
            n -= 1
        res = alpha[rem] + res
    return res


print(convertToTitle(702))


# 给定一个Excel表格中的列名称，返回其相应的列序号。
def titleToNumber(s):
    """
    :type s: str
    :rtype: int
    """
    l = len(s)
    res = 0
    for i in range(0, l):
        tmp = ord(s[i]) - 64
        res = res * 26 + tmp
    return res


print(titleToNumber('AAA'))
