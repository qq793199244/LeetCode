'''
给定一个二叉树，检查它是否是镜像对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.dfs(root.left, root.right)

    def dfs(self, left, right):
        if not (left or right):
            return True
        if not (left and right):
            return False
        if left.val!=right.val:
            return False
        return self.dfs(left.left,right.right) and self.dfs(left.right,right.left)


if __name__ == '__main__':
    u = Solution()
    # [1,2,2,3,4,4,3]
    root = TreeNode(1)
    l1 = root.left = TreeNode(2)
    r1 = root.right = TreeNode(2)
    l21 = l1.left = TreeNode(3)
    l22 = l1.right = TreeNode(4)
    r21 = r1.left = TreeNode(4)
    r22 = r1.right = TreeNode(3)
    res = u.isSymmetric(root)
    print(res)