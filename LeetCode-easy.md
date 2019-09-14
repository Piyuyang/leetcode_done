# 1、两数之和

​		给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

## 思路一：暴力

两层循环，以下标为变量，外层循环(i, len(nums))，内层循环(i+1, len(nums))，满足条件的下标append到返回列表中

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if num[i]+num[j] == target:
                    return [i, j]
        else:
            return []
```

## 思路二：字典

将nums中数字及对应下标存入字典，key为数字，value为数字下标

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d_nums = dict()
        for index,value in enumerate(nums):
        	sub = target - value
            # 根据后加入的数据找之前数据
            if sub in d_nums.keys():
                return [d_nums[sub], index]
            d_nums[value] = index
        else:
            return []
```



##  改：两数之和-输入有序数组

给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
返回的下标值（index1 和 index2）不是从零开始的。

```python
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left+1, right+1]
            elif sum > target:
                right -= 1
            else:
                left += 1
```





# 2、整数反转

​		给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

​		注意：假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

```python
class Solution:
    def reverse(self, x: int) -> int:
        # 转为正数，简化代码
        y, res = abs(x), 0
        flag = (1<<31)-1 if x>0 else 1<<31
        while y:
            res = res*10 + y%10
            if res > flag:
                return 0
            y = y//10
        return res if x>0 else -res
```

> 2的次方可以用二进制1的移位来表示，例如2^3是8，写成二进制是1000，即1<<3



# 3、回文数

​		判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x)[::-1] == str(x):
            return True
        else:
            return False
```

## 进阶（待做）

不用字符串



# 4、罗马数字转整数

罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

```
I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
```

给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

## 思路：字典

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'IV':4, 'V':5, 'IX':9,
            'X':10, 'XL':40, 'L':50, 'XC':90,
            'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000, }
        result = 0
        i = 0
        while i < len(s):
            if i+1 < len(s) and s[i]+s[i+1] in d:
                result += d[s[i]+s[i+1]]
                i += 2
            else:
                result += d[s[i]]
                i += 1
        return result
```



# 5、最长公共前缀

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 `""`。

## 思路一：find()

在剩下字符串中查找第一个字符串，如果没有返回下标0，则表示剩余字符串不是以第一个字符串开头

缩短第一个字符串，重复查找步骤

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        res = strs[0]
        i = 1
        while i < len(strs):
            while strs[i].find(res) != 0:
                res = res[:len(res)-1]
            i += 1
        return res
```

## 思路二：zip()

取每个单词同位置字母，对比是否相同

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for tmp in zip(*strs):
            if len(set(tmp)) == 1:
                res += tmp[0]
            else:
                break
        return res
```

> zip()函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。

```python
a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
zipped = zip(a,b)     # 打包为元组的列表
# [(1, 4), (2, 5), (3, 6)]

zip(a,c)              # 元素个数与最短的列表一致
# [(1, 4), (2, 5), (3, 6)]

zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
# [(1, 2, 3), (4, 5, 6)]
```

## 思路三：排序后对比

利用python的max()和min()，在Python里字符串是可以比较的，按照ASCII值排，举例abb， aba，abac，最大为abb，最小为aba。所以只需要比较最大最小的公共前缀就是整个数组的公共前缀

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        s_max = max(strs)
        s_min = min(strs)
        for i,s in enumerate(s_min):
            if s != s_max[i]:
                return s_max[:i]
        return s_min
```



# 6、有效的括号

给定一个**只包括** '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

​	左括号必须用相同类型的右括号闭合。

​	左括号必须以正确的顺序闭合。

注意空字符串可被认为是有效字符串。

## 思路一：数据结构“栈”

​		利用数据结构“栈”，遇到左括号，将左括号入栈，遇到右括号，对比栈顶括号是否与之配对，能配对则将栈顶元素出栈，不能配对则返回False

```python
class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')', '{':'}', '[':']'}
        tmp = list()
        for i in s:
            if i in d:
                tmp.append(d[i])
            else:
                try:
                    if i == tmp[-1]:
                        tmp.pop()
                    else:
                        return False
                except:
                    return False
        return len(tmp) == 0
```

## 思路二：replace()

​		输入字符串只包含三种括号，成对括号中不含其它字符。所以，可以从最内层括号出发，依次将成对的括号替换成空字符串。（用时较思路一长）

```python
class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''
```



# 7、合并两个有序链表

将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

> 例子：
>
> 输入：1->2->4, 1->3->4
>
> 输出：1->1->2->3->4->4

## 思路一：递归

1、考虑边界情况： 如果 l1 或者 l2 一开始就是 null ，不需要合并，直接返回非空链表。

2、判断 l1 和 l2 哪一个的val更小，然后递归地决定下一个添加到结果里的值。如果两个链表都是空的，那么过程终止，所以递归过程最终一定会终止。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
```

## 思路二：迭代

1、设置哨兵节点head，便于最后返回合并后链表

2、定义res指针，通过迭代获得res.next指向的对象

3、对比l1.val和l2.val，将res.next指向较小值的ListNode对象，然后res指针后移一位（res = res.next）

4、若某个链表被走完，另外链表剩下的元素直接接到res.next即可

5、返回合并链表

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        res = head
        while l1 and l2:
            if l1.val < l2.val:
                res.next = l1
                l1 = l1.next
            else:
                res.next = l2
                l2 = l2.next
            res = res.next
        res.next = l1 if l1 else l2
        return head.next
```



# 8、删除排序数组中的重复项

给定一个排序数组，你需要在**原地**删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在**原地**修改输入数组并在使用 O(1) 额外空间的条件下完成。

## 思路：双指针法

设置两个指针 i（起始位置0）、j（起始位置1）

如果nums[i] == nums[j]，使 j+1 ，跳过重复项 

如果nums[i] != nums[j]，使nums[i+1] = nums[j]，并且将 i 移至下一位

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        if len(nums) == 0:
            return 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i+1
```



# 9、移除元素

给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

## 思路：双指针

用两个指针，指针 j 遍历整个数组，找出不等于 val 的数，赋值给 nums[i]。

当 nums[j] == val ，j 前进一位

当 nums[j] != val，赋值nums[i] = nums[j]，i、j同时前进一位

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0
        if len(nums) == 0:
            return 0
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i
```



# 10、搜索插入位置

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

## 思路一：顺序查找

从前往后顺序查找

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        else:
            for i in range(len(nums)-1):
                if nums[i] < target <= nums[i+1]:
                    return i+1
```

## 思路二：二分查找

### 传统的二分查找

while 循环条件为 left<=right ，需要考虑返回值取left还是right

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        if len(nums) == 0:
            return 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1
        return left
# [0,1,2,3,4] 5
```

### 神奇的二分查找（了解）

while 循环条件为 left<right ，返回时left与right是相等的

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 返回大于等于 target 的索引，有可能是最后一个 
        size = len(nums) 
        if size == 0: 
            return 0 
        l = 0 # 如果 target 比 nums里所有的数都大，则最后一个数的索引 + 1 就是候选值，因此，右边界应该是数组的长度 
        r = size # 二分的逻辑一定要写对，否则会出现死循环或者数组下标越界 
        while l < r: 
            mid = l + (r - l) // 2 
            if nums[mid] < target: 
                l = mid + 1 
            else: 
                r = mid 
        return l
```



# 11、实现strStr()

实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

## 思路：暴力循环寻找

(44ms, 13.1MB)

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l_h = len(haystack)
        l_n = len(needle)
        if l_n == 0:
            return 0
        if l_h < l_n:
            return -1
        i_h = 0
        while i_h < l_h:
            if len(haystack[i_h:]) < l_n:
                return -1
            tmp = i_h
            i_n = 0
            while (i_n < l_n) and (haystack[i_h] == needle[i_n]):
                i_h += 1
                i_n += 1
            if i_n == l_n:
                return tmp
            i_h = tmp + 1
        return -1
```

## 代码简化(不使用内置函数)

(68ms, 13.3MB)

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
```

## 代码简化(使用内置函数find)

(40ms, 13.3MB)

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
```



# 12、报数

报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

> 1. 1
> 2. 11
> 3. 21
> 4. 1211
> 5. 111221
>
> 1 被读作  "one 1"  ("一个一") , 即 11。
> 11 被读作 "two 1s" ("两个一"）, 即 21。
> 21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。

## 思路：递归

函数count_num负责得到具体字符串

```python
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        return self.count_num(self.countAndSay(n-1))
    
    def count_num(self, s: str) -> str:
        i = 0
        result = list()
        while i < len(s):
            c = s[i]
            n_c = 0
            while i < len(s) and s[i] == c:
                i += 1
                n_c += 1
            result.append(n_c)
            result.append(c)
        return ''.join(result)
```



# 13、最大子序和

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

## 思路一：暴力

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ = nums[0]  # 最大子序和
        tmp = max_  # 当前自序和
        for i in range(1, len(nums)):
            if tmp + nums[i] > nums[i]:
                # tmp(当前子序和)+nums[i](此时元素) 大于 tmp 时，
                # 说明最大和的连续子数组还没有结束，记录此时的最大值
                max_ = max(max_, tmp + nums[i])
                tmp = tmp + nums[i]
            else:
                # 当 tmp+nums[i] 小于 nums[i] 时，证明tmp是负数，当前最长序列到此为止。
                # 以nums[i]为起点继续找最大子序和,并记录此时的最大值
                max_ = max(max_, nums[i])
                tmp = nums[i]
        return max_
```

## 思路二：动态规划

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i-1]+nums[i], nums[i])
        return max(nums)
```

## 进阶（待做）

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。



# 14、最后一个单词的长度

给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。

>例子：
>
>输入: "Hello World"
>输出: 5

## 思路

先去除字符串首尾多余空格，以‘ ’为分隔符分割，取最后一个子串，返回其长度

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])
```



# 15、加一

给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

> 例1：
> 输入: [1,2,3]
> 输出: [1,2,4]
> 解释: 输入数组表示数字 123。
>
> 例2：
> 输入: [4,3,2,1]
> 输出: [4,3,2,2]
> 解释: 输入数组表示数字 4321。

## 思路

加一的情况分为两种：9+1 和 非9数字+1

从列表最后位开始，向前循环：

​	若数非9，则直接+1后退出循环

​	若数为9，将该位数值设为0，进入下轮循环

直到循环至首位，若首位为9，则需要手动在下标0处插入元素1

加一得十进一位个位数为 000 加法运算如不出现进位就运算结束了且进位只会是一。

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
            else:
                digits[i] += 1
                break
        return digits
```

## 代码简化

不再判断该位是否为9，统+1后%10

遇到非零数，代表无进位，可跳出循环

若首位为0，手动在0位置插入1，模拟进位

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            digits[i] %= 10
            if digits[i] != 0:
                break
        if digits[0] == 0:
            digits.insert(0,1)
        return digits
```



# 16、二进制求和

给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为**非空**字符串且只包含数字 `1` 和 `0`。

> 例1：
> 输入: a = "11", b = "1"
> 输出: "100"
>
> 例2：
> 输入: a = "1010", b = "1011"
> 输出: "10101"

## 思路一：内置函数bin、int

```python
class Solution: 
    def addBinary(self, a: str, b: str) -> str: 
        return bin(int(a, 2) + int(b, 2))[2:]
# int(字符串,base=进制)  将数字意义字符串转成目标进制整数
# bin(整数)  返回整数的二进制形式，带有前缀'0b'
```

## 思路二：暴力

将两个字符串较短的用 000 补齐，使得两个字符串长度一致，然后从末尾进行遍历计算，得到最终结果

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a.rjust(max(len(a), len(b)), '0')
        b = b.rjust(max(len(a), len(b)), '0')  # 将两个字符串以0补位到等长
        res = ''
        flag = 0  # 进位标志
        for i in range(len(a)-1, -1, -1):
            tmp = int(a[i]) + int(b[i]) + flag
            res = str(tmp % 2) + res
            flag = tmp // 2
        if flag == 1:
            res = '1' + res
        return res
```



# 17、x的平方根

实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

## 思路一：二分查找

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0  # 保证取值
        right = x//2 + 1  # 保证取值
        # 写法一
        # while left < right:
            # mid = left + (right - left + 1)//2  # 取右中位数，避免死循环
            # if mid**2 <= x:
            #    left = mid
            #else:
            #    right = mid - 1
        # return left
        
        # 写法二
        while left <= right:
            mid = (left + right)//2
            if x == mid**2:
                return mid
            elif x < mid**2:
                right = mid - 1
            else:
                left = mid + 1
        return right
```

## 思路二：牛顿迭代法

> 牛顿法思想：在迭代过程中，**以直线代替曲线**，用一阶泰勒展式（即在当前点的切线）代替原曲线，求直线与 x轴的交点（x0），重复这个过程直到收敛。
>
> 这种算法的原理很简单，我们仅仅是不断用 (x,f(x)) 的切线来逼近方程 x^2-a=0 的根。函数上任一点 (x,f(x)) 处的切线斜率是 2x，那么，x−f(x)/(2x) 就是一个比 x 更接近的近似值。代入 f(x)=x^2-a 得到x-(x^2-a)/(2x)，也就是 (x+a/x)/2。
>

$$
令f(x)=x^2-a
\\ 根据导数定义，f'(x_0)=\frac{f(x_0)-f(x)}{x_0-x}
\\ f(x_0)=f(x)+(x_0-x)f'(x_0)
\\ 令f(x_0)=0\ 则\ x^2-a+(x_0-x)*2x_0=0、x_0^2-a=0
\\ x^2+a-2xx_0=0
\\ x_0=\frac{1}{2}(x+\frac{a}{x})
$$

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        cur = 1  # 起始值任意
        while True:
            pre = cur
            cur = (cur + x/cur)/2  # 用cur逼近x0
            if abs(cur - pre) < 1e-6:  # 当两次结果相差足够小时，认为已找到x轴交点
                return int(cur)
```



# 18、爬楼梯

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

## 思路一：递归

超出时间限制，时间复杂度为O(2^n)

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-1)+self.climbStairs(n-2)
```

## 思路二：动态规划

时间复杂度为O(n)

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        i = 0
        while i < n:
            a, b = b, a+b
        return a 
```

## 思路三：记忆递归（备忘录算法）

改进基本递归方法，将每次计算的f(n)值存入一个字典，下次遇到f(n)时，直接从字典中取出值



# 19、删除排序列表中的重复元素

给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 不考虑已排序  68ms	13.1MB
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        h = head
        if not h:
            return []
        cur1, cur2 = head, head.next
        val_list = [cur1.val]
        while cur2:
            if cur2.val not in val_list:
                val_list.append(cur2.val)
                cur1, cur2 = cur2, cur2.next
            else:
                cur1.next = cur2.next
                cur2 = cur2.next
        return h

# 考虑已排序  96ms	13MB
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
```



# 20、合并两个有序数组

给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

>  说明:
> 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
> 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

## 思路一：双指针、直接修改

以nums1为基准，插入nums2中数据

68 ms	12.9 MB

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m == 0:
            nums1[:] = nums2[:]
        cur1, cur2 = 0, 0
        nums1[:] = nums1[:m]
        while cur2 < n and cur1 < m:
            if nums2[cur2] < nums1[cur1]:
                nums1.insert(cur1, nums2[cur2])
                cur2 += 1
                cur1 += 1
            elif cur1 < m-1 and nums1[cur1] <= nums2[cur2] < nums1[cur1+1]:
                nums1.insert(cur1+1, nums2[cur2])
                cur2 += 1
                cur1 += 2
            else:
                cur1 += 1
            m = len(nums1)
        if cur2 < n:
            nums1[cur1+1:] = nums2[cur2:]
```

## 思路二：合并后排序

利用内置函数sorted()

76 ms	13.1 MB
时间复杂度 : O((n+m)log⁡(n+m))
空间复杂度 : O(1)

```python
class Solution(object): def merge(self, nums1, m, nums2, n):
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[:] = sorted(nums1[:m] + nums2)
```

## 思路三：双指针、创建新数组

将指针p1 置为 nums1的开头， p2为 nums2的开头，在每一步将最小值放入输出数组中。
由于 nums1 是用于输出的数组，需要将nums1中的前m个元素放在其他地方。

72 ms	12.9 MB
时间复杂度：O(n+m)
空间复杂：O(m)

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1_copy = nums1[:m]
        nums1[:] = []  # 若nums1=[]，则nums1指向其他地址空间，无法正确修改
        cur1, cur2 = 0, 0
        while cur1 < m and cur2 < n:
            if nums1_copy[cur1] < nums2[cur2]:
                nums1.append(nums1_copy[cur1])
                cur1 += 1
            else:
                nums1.append(nums2[cur2])
                cur2 += 1
        if cur1 < m:
            nums1[cur1+cur2:] = nums1_copy[cur1:]
        if cur2 < n:
            nums1[cur1+cur2:] = nums2[cur2:]
```



# 21、相同的树

给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

## 思路：递归

首先判断 `p` 和 `q` 是不是 `None`，然后判断它们的值是否相等。
若以上判断通过，则递归对子结点做同样操作。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if (not p) and (not q):
            return True
        elif (not p) or (not q):
            return False
        else:
            if p.val != q.val:
                return False
            else:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```



# 22、对称二叉树

给定一个二叉树，检查它是否是镜像对称的。

## 思路一：迭代

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            return self.isMirro(root.left, root.right)
    
    def isMirro(self, left: TreeNode, right: TreeNode) -> bool:
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        else:
            return left.val==right.val and self.isMirro(left.left, right.right) and self.isMirro(left.right, right.left)
```

## 思路二：队列queue（待做）



# 22、二叉树的最大深度

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

## 思路一：递归

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
          	# 分别求出左子树、右子树的深度，取最大值，再加上自身深度
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            depth = max(left_depth, right_depth) + 1
        return depth
```



# 23、二叉树的层次便利 II

给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

## 思路：逐层遍历，类似队列

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        node = [root]
        tree = []
        while node:
            tmp_tree, n = [], len(node)
            for i in range(n):
                tmp_node = node.pop(0)
                tmp_tree.append(tmp_node.val)
                if tmp_node.left:
                    node.append(tmp_node.left)
                if tmp_node.right:
                    node.append(tmp_node.right)
            tree.insert(0,tmp_tree)
        return tree
```



# 23、杨辉三角

给定一个非负整数 *numRows，*生成杨辉三角的前 *numRows* 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。

杨辉三角第一行：numRows=1

## 思路：动态规划

如果能够知道一行杨辉三角，我们就可以根据每对相邻的值轻松地计算出它的下一行。

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        triangle = [[1]]
        for i in range(1, numRows):
            tmp = [1, 1]
            for j in range(1, i):
                tmp.insert(j, triangle[i-1][j-1] + triangle[i-1][j])
            triangle.append(tmp)
        return triangle
```



# 24、杨辉三角II

给定一个非负索引 *k*，其中 *k* ≤ 33，返回杨辉三角的第 *k* 行。

此题中，杨辉三角第一行：k=0

## 思路：动态规划

```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [1]
        for i in range(rowIndex):
            tmp = [1, 1]
            for j in range(1, i+1):
                tmp.insert(j, triangle[j-1] + triangle[j])
            triangle = tmp
        return triangle
```



# 25、买卖股票的最佳时机

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多**<u>只允许完成一笔交易</u>**（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。

## 思路一：暴力（超出时间限制）

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if not prices:
            return profit
        for i, v in enumerate(prices):
            min_p = v
            max_p = max(prices[i:]) 
            profit = max(max_p - min_p, profit)
        return profit
```

## 思路二：动态规划

最大利润 = max( 之前的最大利润, 今天的价格 - 之前的最低价格 )

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        min_p = prices[0]
        max_p = 0
        for i in range(len(prices)):
            min_p = min(min_p, prices[i])
            max_p = max(max_p, prices[i] - min_p)
        return max_p
```



# 26、买卖股票的最佳时机II

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（<u>**多次**</u>买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

## 思路一：简单的一次遍历

不需要寻找最大差值的极值对，直接计算数组连续数字之间的差值，如果第二个数字大于第一个数字，我们获得的总和将是最大利润。

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] - prices[i] > 0:
                profit += (prices[i+1] - prices[i])
        return profit
```



# 27、验证回文串

给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

**说明：**本题中，我们将空字符串定义为有效的回文串。

## 思路一：双指针

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
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
        return True
```

## 思路二：正则表达式提取有效字符，再比较

> re.sub(pattern, repl, string, count=0, flags=0)
>
> 参数：
> pattern : 正则中的模式字符串。
> repl : 替换的字符串，也可为一个函数。
> string : 要被查找替换的原始字符串。
> count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
>
> 选取string中满足正则表达式部分，替换到repl中

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        tmp = re.sub(r"[^A-Za-z0-9]","", s).lower()
        return tmp == tmp[::-1]
```



# 28、只出现一次的数字

给定一个**非空**整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

## 思路一：列表.count(元素)

超出时间限制

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for n in nums:
            if nums.count(n) == 1:
                return n
```

## 思路二：列表操作

- 遍历列表nums
- 如果某个nums 中的数字是新出现的，则将它添加到列表中
- 如果某个数字已经在列表中，删除它

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        alist = []
        for n in nums:
            if n not in alist:
                alist.append(n)
            else:
                alist.remove(n)
        return alist.pop()
```

## 思路三：哈希表

用哈希表避免每次查找元素是否存在需要的 O(n) 时间。

- 遍历 nums 中的每一个元素
- 查找 hash_table 中是否有当前元素的键
- 如果没有，将当前元素作为键插入 hash_table
- 最后， hash_table 中仅有一个元素，用 popitem 获得

```python
class Solution(object):
    def singleNumber(self, nums):
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]
```

## 思路四：数学

$2(a+b+c)-(a+a+b+b+c)=c$

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums)) - sum(nums)
```

## 思路五：位操作

- 如果对a和0进行按位异或，得到结果为a​ ——>$a ⊕ 0 = a$

- 如果a与a异或，结果为0 ——> $a ⊕ a = 0$
- 异或满足交换律和结合律 ——> $a⊕b⊕a = a⊕a⊕b = (a⊕a)⊕b = 0⊕b = b$

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res
```



# 29、环形链表

给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

![image-20190725094022137](/Users/piyuyang/Library/Application Support/typora-user-images/image-20190725094022137.png)

## 思路一：列表存储

列表存储已出现的节点，若某节点指向的下一节点再已出现的节点中，表示该链表是成环的

执行时间1752 ms
内存消耗17.9 MB

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node_list = []
        while head:
            if head in node_list:
                return True
            else:
                node_list.append(head)
                head = head.next
        else:
            return False
```

## 思路二：双指针

​	通过使用具有 不同速度 的快、慢两个指针遍历链表，空间复杂度可以被降低至 O(1)。慢指针每次移动一步，而快指针每次移动两步。
​	如果列表中不存在环，最终快指针将会最先到达尾部，此时我们可以返回 false。
​	现在考虑一个环形链表，把慢指针和快指针想象成两个在环形赛道上跑步的运动员（分别称之为慢跑者与快跑者）。而快跑者最终一定会追上慢跑者。

执行时间76 ms	
内存消耗18 MB

```python
class Solution(object):
    def hasCycle(self, head):
        if not (head and head.next):
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not (fast and fast.next):
                return False
            slow = slow.next
            fast = fast.next.next
        else:
            return True
```



# 30、最小栈

设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。

## 思路：辅助栈

```python
class MinStack(object):
    def __init__(self):
        self.data = []
        self.help = []
    def push(self, x):
        # 非同步栈：只有入栈的元素最小时，辅助栈才入栈
        self.data.append(x)
        if len(self.help) == 0 or x <= self.help[-1]:
            self.help.append(x)
            
        # 同步栈：如果入栈元素非最小值，辅助栈入栈当前栈定元素，即当前最小值
        # self.data.append(x)
        # if len(self.help) == 0 or x <= self.help[-1]:
        #     self.help.append(x)
        # else:
        #     self.help.append(self.help[-1])
        
    def pop(self):
        # 非同步栈：只有出栈元素最小时，辅助栈同步出栈
        if self.data:
        	num = self.data.pop()
        if self.help and num == self.help[-1]:
            self.help.pop()
        
        # 同步栈：辅助栈同步出栈
        # if self.data:
        #     self.data.pop()
        #     self.help.pop()
        
    def top(self):
        if self.data:
            return self.data[-1]
    def getMin(self):
        if self.help:
            return self.help[-1]
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```



# 31、Excel表列名称、序号

## 序号-->名称（二十六进制）

给定一个正整数，返回它在 Excel 表中相对应的列名称。
A->1, B->2, Z->26, AA->27

问题：26个字母中，没有字母表示0
解决：当余数为0时，向商借1

```python
class Solution(object):
    def convertToTitle(self, n):
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
```

## 名称-->序号

```python
class Solution(object):
    def titleToNumber(self, s):
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
```

# 32、路径总和
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

## 思路：递归

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # 如果该节点为叶子节点，判断root是否等于sum
        # 如果该节点存在子节点，sum-=root，分两路循环
        if root is None:
            return False
        # if root.left is None and root.right is None:
        #     if root == sum:
        #         return True
        #     else:
        #         return False
        # else:
        #     sum -= root
        #     return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

        sum -= root.val
        if not root.left and not root.right:
            return sum == 0
        else:
            return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

```
