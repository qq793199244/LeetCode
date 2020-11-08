'''
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。
（即逐层地，从左到右访问所有节点）
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            length = len(queue)
            level = []
            for _ in range(length):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res

if __name__ == '__main__':
    u = Solution()
    # [3,9,20,null,null,15,7]
    root = TreeNode(3)
    node9 = root.left = TreeNode(9)
    node20 = root.right = TreeNode(20)
    node15 = node20.left = TreeNode(15)
    node7 = node20.right = TreeNode(7)

    res = u.levelOrder(root)
    print(res)