# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

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
        if root.left is None and root.right is None:
            if root == sum:
                return True
            else:
                return False
        else:
            sum -= root
            return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
