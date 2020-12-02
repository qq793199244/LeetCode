# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    # 递归。时间复杂度O(n) 空间复杂度O(n)
    def inorderTraversal1(self, root):
        res = []
        def dfs(root):
            if not root: return root
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res

    # 非递归。时间复杂度O(n) 空间复杂度O(n)
    def inorderTraversal2(self, root):
        res = []
        if not root: return res
        stack = [root]
        while stack:
            while root.left:
                stack.append(root.left)
                root = root.left
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
                root = node.right
        return res


if __name__ == '__main__':
    u = Solution()
    # 输入[1, 2, 3, null, 4, 5, 6] 输出[2, 4, 1, 5, 3, 6]
    root = TreeNode(1)
    node2 = root.left = TreeNode(2)
    node3 = root.right = TreeNode(3)
    node4 = node2.right = TreeNode(4)
    node5 = node3.left = TreeNode(5)
    node6 = node3.right = TreeNode(6)
    print(u.inorderTraversal1(root))
    print(u.inorderTraversal2(root))