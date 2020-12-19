'''
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # 递归。时间复杂度O(n) 空间复杂度O(n)
    def preorderTraversal1(self, root):
        if not root: return root
        res = []
        def dfs(root):
            if not root: return root
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res

    # 非递归。时间复杂度O(n) 空间复杂度O(n)
    def preorderTraversal2(self, root):
        res = []
        if not root: return res
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            # 利用栈先进后出性质，先把右子节点放入栈
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res


if __name__ == '__main__':
    u = Solution()
    # 输入[1, 2, 3, null, 4, 5, 6] 输出[1, 2, 4, 3, 5, 6]
    root = TreeNode(1)
    node2 = root.left = TreeNode(2)
    node3 = root.right = TreeNode(3)
    node4 = node2.right = TreeNode(4)
    node5 = node3.left = TreeNode(5)
    node6 = node3.right = TreeNode(6)
    print(u.preorderTraversal1(root))
    print(u.preorderTraversal2(root))