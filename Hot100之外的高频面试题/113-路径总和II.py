'''
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
说明: 叶子节点是指没有子节点的节点。
示例:
给定如下二叉树，以及目标和 sum = 22，
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:[[5,4,11,2], [5,8,4,5]]
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # DFS 时间复杂度O(n)，空间复杂度O(n)
    def pathSum1(self, root, sum):
        res = []
        path = []
        def dfs(root, sum):
            if not root: return
            path.append(root.val)
            sum -= root.val
            if not root.left and not root.right and sum == 0:
                res.append(path[:])
            dfs(root.left, sum)
            dfs(root.right, sum)
            path.pop()
        dfs(root, sum)
        return res


if __name__ == '__main__':
    u = Solution()
    root = TreeNode(5)
    n4 = root.left = TreeNode(4)
    n8 = root.right = TreeNode(8)
    n11 = n4.left = TreeNode(11)
    n13 = n8.left = TreeNode(13)
    n4_2 = n8.right = TreeNode(4)
    n7 = n11.left = TreeNode(7)
    n2 = n11.right = TreeNode(2)
    n5 = n4_2.left = TreeNode(5)
    n1 = n4_2.right = TreeNode(1)
    print(u.pathSum1(root, 22))
