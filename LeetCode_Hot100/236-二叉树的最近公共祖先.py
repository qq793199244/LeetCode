'''
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，
最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
例如，给定如下二叉树: root =[3,5,1,6,2,0,8,null,null,7,4]
示例 1:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
示例2:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
说明:
所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
解题思路：
两个节点 p,q 分为两种情况：① p 和 q 在相同子树中    ② p 和 q 在不同子树中
从根节点遍历，递归向左右子树查询节点信息
递归终止条件：如果当前节点为空或等于 p 或 q，则返回当前节点
递归遍历左右子树，如果左右子树查到节点都不为空，则表明 p 和 q 分别在左右子树中，因此，当前节点即为最近公共祖先；
如果左右子树其中一个不为空，则返回非空节点。
'''
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root or root.val == p.val or root.val == q.val:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root
# 时间复杂度O(n)
# 空间复杂度O(n)

if __name__ == '__main__':
    u = Solution()
    root = TreeNode(3)
    n5 = root.left = TreeNode(5)
    n1 = root.right = TreeNode(1)
    n6 = n5.left = TreeNode(6)
    n2 = n5.right = TreeNode(2)
    n0 = n1.left = TreeNode(0)
    n8 = n1.right = TreeNode(8)
    n7 = n2.left = TreeNode(7)
    n4 = n2.right = TreeNode(4)
    p = TreeNode(5)
    q = TreeNode(1)
    res = u.lowestCommonAncestor(root, p, q)  # 3
    print(res)
    print(res.val)
