'''
给定一个二叉树，返回其节点值的锯齿形层次遍历。
（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
例如：给定二叉树 [3,9,20,null,null,15,7],
返回锯齿形层次遍历如下：
[[3],
[20,9],
[15,7]]
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        cur = [root]
        res = []
        while cur:
            temp = []
            n = len(cur)
            for i in range(n):
                node = cur.pop(0)
                temp.append(node.val)
                if node.left:
                    cur.append(node.left)
                if node.right:
                    cur.append(node.right)
            res.append(temp)
        for i in range(len(res)):
            if i % 2 != 0:
                res[i].reverse()
        return res


if __name__ == '__main__':
    u = Solution()
    root = TreeNode(3)
    node9 = root.left = TreeNode(9)
    node20 = root.right = TreeNode(20)
    node15 = node20.left = TreeNode(15)
    node7 = node20.right = TreeNode(7)
    res = u.zigzagLevelOrder(root)
    print(res)