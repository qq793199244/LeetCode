'''
路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。
该路径 至少包含一个 节点，且不一定经过根节点。路径和 是路径中各节点值的总和。
给你一个二叉树的根节点 root ，返回其 最大路径和 。
示例 1：
输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
示例 2：
输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
'''


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.maxSum = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        def maxGain(node):
            if not node:
                return 0
            # 递归计算左右子节点的最大贡献值
            # 只有在最大贡献值大于 0 时，才会选取对应子节点
            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)
            # 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
            priceNewpath = node.val + leftGain + rightGain
            # 更新答案
            self.maxSum = max(self.maxSum, priceNewpath)
            # 返回节点的最大贡献值
            return node.val + max(leftGain, rightGain)

        maxGain(root)
        return self.maxSum


if __name__ == '__main__':
    u = Solution()
    r1 = TreeNode(1)
    r1_n2 = r1.left = TreeNode(2)
    r1_n3 = r1.right = TreeNode(3)
    print(u.maxPathSum(r1))  # 6

    r2 = TreeNode(-10)
    r2_n9 = r2.left = TreeNode(9)
    r2_n20 = r2.right = TreeNode(20)
    r2_n15 = r2_n20.left = TreeNode(15)
    r2_n7 = r2_n20.right = TreeNode(7)
    print(u.maxPathSum(r2))  # 42
