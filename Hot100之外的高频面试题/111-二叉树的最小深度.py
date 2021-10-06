'''
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明：叶子节点是指没有子节点的节点。
示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：2
示例 2：
输入：root = [2,null,3,null,4,null,5,null,6]
输出：5
'''


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


if __name__ == '__main__':
    u = Solution()
    tree1 = TreeNode(3)
    n9 = tree1.left = TreeNode(9)
    n20 = tree1.right = TreeNode(20)
    n15 = n20.left = TreeNode(15)
    n7 = n20.right = TreeNode(7)

    tree2 = TreeNode(2)
    n3 = tree2.right = TreeNode(3)
    n4 = n3.right = TreeNode(4)
    n5 = n4.right = TreeNode(5)
    n6 = n5.right = TreeNode(6)

    print(u.minDepth(tree1))  # 2
    print(u.minDepth(tree2))  # 5
