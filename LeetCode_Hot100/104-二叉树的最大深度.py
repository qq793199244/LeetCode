'''
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。
示例：
给定二叉树 [3,9,20,null,null,15,7]，
    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
'''


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # 时间复杂度O(n)，空间复杂度O(Height)
    def maxDepth(self, root):
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

    # 迭代，层序遍历。时间复杂度O(n)，空间复杂度取决于队列存储的元素数量，其在最坏情况下会达到O(n)
    def maxDepth2(self, root):
        if not root:
            return 0
        res = 0
        queue = [root]
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res += 1
        return res


if __name__ == '__main__':
    u = Solution()
    n3 = TreeNode(3)
    n9 = n3.left = TreeNode(9)
    n20 = n3.right = TreeNode(20)
    n15 = n20.left = TreeNode(15)
    n7 = n20.right = TreeNode(7)
    print(u.maxDepth(n3))
    print(u.maxDepth2(n3))
