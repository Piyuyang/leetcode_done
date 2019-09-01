class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            depth = max(left_depth, right_depth) + 1
        return depth


# [3,9,20,null,null,15,7]
a = TreeNode(15)
b = TreeNode(7)
c = TreeNode(20)
c.left = a
c.right = b
d = TreeNode(9)
root = TreeNode(3)
root.left = d
root.right = c

s = Solution()
depth = s.maxDepth(root)
print(depth)
