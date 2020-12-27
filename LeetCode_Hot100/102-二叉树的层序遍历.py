'''
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
示例：
二叉树：[3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回其层序遍历结果：
[
  [3],
  [9,20],
  [15,7]
]
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            tmp = []
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res
# 时间复杂度O(n)
# 空间复杂度O(n)


if __name__ == '__main__':
    u = Solution()
    root = TreeNode(3)
    n9 = root.left = TreeNode(9)
    n20 = root.right = TreeNode(20)
    n15 = n20.left = TreeNode(15)
    n7 = n20.right = TreeNode(7)
    print(u.levelOrder(root))