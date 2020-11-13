'''
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，
这条路径上所有节点值相加等于目标和。
说明: 叶子节点是指没有子节点的节点。
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == sum
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)


if __name__ == '__main__':
    u = Solution()
    root = TreeNode(5)
    n4 = root.left = TreeNode(4)
    n8 = root.right = TreeNode(8)
    n11 = n4.left = TreeNode(11)
    n13 = n8.left = TreeNode(13)
    n4_2 = n8.right = TreeNode(4)
    n7 = n11.left = TreeNode(7)
    n2 = n11.right = TreeNode(2)
    n1 = n4_2.right = TreeNode(1)
    res = u.hasPathSum(root, 22)
    print(res)