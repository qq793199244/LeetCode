'''
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:
输入:
    2
   / \
  1   3
输出: true
示例 2:
输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。根节点的值为 5 ，但是其右子节点值为 4 。
'''


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # 递归。时间复杂度O(n)，空间复杂度O(n)
    def isValidBST(self, root):
        def dfs(node, left=float('-inf'), right=float('+inf')):
            if not node:
                return True
            elif left < node.val < right:
                return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
            else:
                return False

        return dfs(root)

    # 非递归（用栈模拟中序遍历）。时间复杂度O(n)，空间复杂度O(n)
    def isValidBST2(self, root):
        stack, inorder = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True


if __name__ == '__main__':
    u = Solution()
    r1 = TreeNode(2)
    n1 = r1.left = TreeNode(1)
    n3 = r1.right = TreeNode(3)

    r2 = TreeNode(5)
    n_1 = r2.left = TreeNode(1)
    n_4 = r2.right = TreeNode(4)
    n_3 = n_4.left = TreeNode(3)
    n_6 = n_4.right = TreeNode(6)

    print(u.isValidBST(r1))  # True
    print(u.isValidBST(r2))  # False

    print(u.isValidBST2(r1))  # True
    print(u.isValidBST2(r2))  # False
