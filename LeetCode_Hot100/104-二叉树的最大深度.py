'''
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == '__main__':
    u = Solution()
    root = TreeNode(3)
    n9 = root.left = TreeNode(9)
    n20 = root.right = TreeNode(20)
    n15 = n20.left = TreeNode(15)
    n7 = n20.right = TreeNode(7)
    n1 = n7.left = TreeNode(1)

    res = u.maxDepth(root)
    print(res)