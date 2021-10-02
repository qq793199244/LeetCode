'''
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点的左右两个子树的高度差的绝对值不超过 1 。
示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：true
示例 2：
输入：root = [1,2,2,3,3,null,null,4,4]
输出：false
示例 3：
输入：root = []
输出：true
'''


class TreeNode:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x


class Solution:
    # 时间复杂度O(nlogn)，空间复杂度O(n)
    def isBalanced(self, root):

        def height(root):
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)
            return max(left, right) + 1

        if not root:
            return True
        return abs(height(root.left) - height(root.right)) <= 1 and \
               self.isBalanced(root.left) and self.isBalanced(root.right)


if __name__ == '__main__':
    u = Solution()
    t1 = TreeNode(3)
    t1_2 = t1.left = TreeNode(9)
    t1_3 = t1.right = TreeNode(20)
    t1_4 = t1_3.left = TreeNode(15)
    t1_5 = t1_3.right = TreeNode(7)

    t2 = TreeNode(1)
    t2_2 = t2.left = TreeNode(2)
    t2_3 = t2.right = TreeNode(2)
    t2_4 = t2_2.left = TreeNode(3)
    t2_5 = t2_2.right = TreeNode(3)
    t2_6 = t2_4.left = TreeNode(4)
    t2_7 = t2_4.right = TreeNode(4)

    t3 = TreeNode(None)

    print(u.isBalanced(t1))  # True
    print(u.isBalanced(t2))  # False
    print(u.isBalanced(t3))  # True
