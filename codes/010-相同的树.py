# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSameTree(p, q):
    if (not p) and (not q):
        return True
    elif (not p) or (not q):
        return False
    else:
        if p.val != q.val:
            return False
        else:
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
