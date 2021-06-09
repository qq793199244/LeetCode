'''
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：
“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
例如，给定如下二叉搜索树: root = [6,2,8,0,4,7,9,null,null,3,5]
示例 1:
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6
解释: 节点 2 和节点 8 的最近公共祖先是 6。
示例 2:
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
说明:
所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉搜索树中。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归。时间复杂度O(H)，空间复杂度O(H)
    def lowestCommonAncestor(self, root, p, q):
        """
            :type root: TreeNode
            :type p: TreeNode
            :type q: TreeNode
            :rtype: TreeNode
        """
        if not root:
            return None
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

    # 迭代。时间复杂度O(H)，空间复杂度O(1)
    def lowestCommonAncestor2(self, root, p, q):
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root
        return None


if __name__ == '__main__':
    u = Solution()
    r1 = TreeNode(6)
    r1_2 = r1.left = TreeNode(2)
    r1_8 = r1.right = TreeNode(8)
    r1_0 = r1_2.left = TreeNode(0)
    r1_4 = r1_2.right = TreeNode(4)
    r1_3 = r1_4.left = TreeNode(3)
    r1_5 = r1_4.right = TreeNode(5)
    r1_7 = r1_8.left = TreeNode(7)
    r1_9 = r1_8.right = TreeNode(9)
    print(u.lowestCommonAncestor(r1, TreeNode(2), TreeNode(8)).val)  # 6
    print(u.lowestCommonAncestor(r1, TreeNode(2), TreeNode(4)).val)  # 2

    print(u.lowestCommonAncestor2(r1, TreeNode(2), TreeNode(8)).val)  # 6
    print(u.lowestCommonAncestor2(r1, TreeNode(2), TreeNode(4)).val)  # 2
