'''
给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
示例 1：
输入：p = [1,2,3], q = [1,2,3]
输出：true
示例 2：
输入：p = [1,2], q = [1,null,2]
输出：false
示例 3：
输入：p = [1,2,1], q = [1,1,2]
输出：false
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    u = Solution()
    p1 = TreeNode(1)
    q1 = TreeNode(1)
    p1.left = TreeNode(2)
    q1.left = TreeNode(2)
    p1.right = TreeNode(3)
    q1.right = TreeNode(3)

    p2 = TreeNode(1)
    q2 = TreeNode(1)
    p2.left = TreeNode(2)
    q2.right = TreeNode(2)

    p3 = TreeNode(1)
    q3 = TreeNode(1)
    p3.left = TreeNode(2)
    q3.left = TreeNode(1)
    p3.right = TreeNode(1)
    q3.right = TreeNode(2)

    print(u.isSameTree(p1, q1))  # True
    print(u.isSameTree(p2, q2))  # False
    print(u.isSameTree(p3, q3))  # False
