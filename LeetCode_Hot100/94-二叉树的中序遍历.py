# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def dfs(root):
            if not root:
                return root
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res

if __name__ == '__main__':
    u = Solution()
    root = TreeNode(1)
    r1 = root.right = TreeNode(2)
    r1l1 = r1.left = TreeNode(3)
    res = u.inorderTraversal(root)
    print(res)