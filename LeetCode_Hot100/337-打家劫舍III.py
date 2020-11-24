'''
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。
这个地区只有一个入口，我们称之为“根”。除了“根”之外，每栋房子有且只有一个“父“房子与之相连。
一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
输入: [3,2,3,null,3,null,1]
     3
    / \
   2   3
    \   \
     3   1
输出: 7
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        if not root:
            return 0
        def dfs(root):
            # 如果节点为空就返回(0,0)
            # 第一个0表示当前节点的最大值，第二个0表示所有子节点的最大值
            if not root:
                return 0, 0
            # 获取左右节点的值，这里会拿到四个值，
            # 左节点的值，左节点孩子的值，右节点的值，右节点孩子的值
            left, left_pre = dfs(root.left)
            right, right_pre = dfs(root.right)
            # a当前节点的值+孙子节点的值
            a = left_pre + right_pre + root.val
            # b两个孩子节点的值
            b = left + right
            # 当前节点的最大值就是max(a,b)，同时还要返回子节点的最大值
            return max(a, b), b
        a, b = dfs(root)
        return max(a, b)


if __name__ == '__main__':
    u = Solution()
    root = TreeNode(3)
    node2_l2 = root.left = TreeNode(2)
    node2_r3 = root.right = TreeNode(3)
    node3_r3 = node2_l2.left = TreeNode(3)
    node3_r1 = node2_r3.right = TreeNode(1)
    res = u.rob(root)
    print(res)
