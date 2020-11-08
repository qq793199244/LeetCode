'''
给定一个二叉树，原地将它展开为一个单链表。
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        res = []
        def dfs(root):
            if not root:
                return root
            res.append(root)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        head = res.pop(0)
        head.left = None
        while res:
            tmp = res.pop(0)
            head.left = None
            head.right = tmp
            head = tmp

