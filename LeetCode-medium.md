# 1、最大二叉树

给定一个不含重复元素的整数数组。一个以此数组构建的最大二叉树定义如下：

二叉树的根是数组中的最大元素。
左子树是通过数组中最大值左边部分构造出的最大二叉树。
右子树是通过数组中最大值右边部分构造出的最大二叉树。
通过给定的数组构建最大二叉树，并且输出这个树的根节点。

```
输入：[3,2,1,6,0,5]
输出：返回下面这棵树的根节点：

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
```

## 思路：迭代

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        max_n = max(nums)
        max_index = nums.index(max_n)
        node = TreeNode(max_n)
        l_nums = nums[:max_index]
        r_nums = nums[max_index + 1:]
        if len(l_nums):
            node.left = self.constructMaximumBinaryTree(l_nums)
        if len(r_nums):
            node.right = self.constructMaximumBinaryTree(r_nums)
        return node
```

