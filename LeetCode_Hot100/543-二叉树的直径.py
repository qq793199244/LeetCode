'''
给定一棵二叉树，你需要计算它的直径长度。
一棵二叉树的直径长度是任意两个结点路径长度中的最大值。
这条路径可能穿过也可能不穿过根结点。
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.res = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.maxpath(root)
        return self.res

    def maxpath(self, root):
        if not root:
            return 0
        L = self.maxpath(root.left)
        R = self.maxpath(root.right)
        self.res = max(self.res, L + R)
        return max(L, R) + 1
