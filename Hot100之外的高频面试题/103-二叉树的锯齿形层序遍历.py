'''
给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
例如：
给定二叉树[3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层序遍历如下：
[[3],
[20,9],
[15,7]]
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        res = []
        cur_queue = [root]
        while cur_queue:
            tmp = []
            for i in range(len(cur_queue)):
                node = cur_queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    cur_queue.append(node.left)
                if node.right:
                    cur_queue.append(node.right)
            res.append(tmp)
        for row in range(len(res)):
            if row % 2 != 0:
                res[row].reverse()
        return res


if __name__ == '__main__':
    u = Solution()
    root = TreeNode(3)
    n9 = root.left = TreeNode(9)
    n20 = root.right = TreeNode(20)
    n15 = n20.left = TreeNode(15)
    n7 = n20.right = TreeNode(7)
    print(u.zigzagLevelOrder(root))
