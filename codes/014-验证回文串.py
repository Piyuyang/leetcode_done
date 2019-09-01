# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
# 说明：本题中，我们将空字符串定义为有效的回文串。

# str1 = "A man, a plan, a canal: Panama"
str1 = "0P"


def isPalindrome(s):
    if not s:
        return True
    s = s.lower().replace(' ', '')
    left = 0
    right = len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    else:
        return True


print(isPalindrome(str1))
