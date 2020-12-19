# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # 递归。时间复杂度O(n) 空间复杂度O(n)
    def postorderTraversal1(self, root):
        if not root: return root
        res = []
        def dfs(root):
            if not root: return root
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)
        dfs(root)
        return res

    # 非递归。时间复杂度O(n) 空间复杂度O(n)
    def postorderTraversal2(self, root):
        res = []
        if not root: return res
        stack = []
        visited = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == visited:
                res.append(root.val)
                visited = root
                root = None
            else:
                stack.append(root)
                root = root.right
        return res

    # 非递归。前序遍历的改编写法；前序（中左右）----------调换（中右左）----------反转（左右中）
    # 时间复杂度O(n) 空间复杂度O(n)
    def postorderTraversal3(self, root):
        res = []
        if not root:
            return res
        tmp_stack = [root]
        while tmp_stack:
            node = tmp_stack.pop()
            res.append(node.val)
            if node.left:
                tmp_stack.append(node.left)
            if node.right:
                tmp_stack.append(node.right)
        return res[::-1]


if __name__ == '__main__':
    u = Solution()
    # 输入[1, 2, 3, null, 4, 5, 6] 输出[4, 2, 5, 6, 3, 1]
    root = TreeNode(1)
    node2 = root.left = TreeNode(2)
    node3 = root.right = TreeNode(3)
    node4 = node2.right = TreeNode(4)
    node5 = node3.left = TreeNode(5)
    node6 = node3.right = TreeNode(6)
    print('递归：', u.postorderTraversal1(root))
    print('迭代1：', u.postorderTraversal2(root))
    print('迭代2：', u.postorderTraversal3(root))