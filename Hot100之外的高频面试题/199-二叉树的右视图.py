'''
给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
示例 1:
输入:[1,2,3,null,5,null,4]
输出:[1,3,4]
示例 2:
输入:[1,null,3]
输出:[1,3]
示例 3:
输入:[]
输出:[]
提示:
二叉树的节点个数的范围是 [0,100]
-100 <= Node.val <= 100
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 层序遍历，每层最后一个元素添加到结果中。时间复杂度O(n)，空间复杂度O(n)
    def rightSideView(self, root):
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
            res.append(tmp[-1])
        return res


if __name__ == '__main__':
    u = Solution()
    root1 = TreeNode(1)
    r1n2 = root1.left = TreeNode(2)
    r1n3 = root1.right = TreeNode(3)
    r1n5 = r1n2.right = TreeNode(5)
    r1n4 = r1n3.right = TreeNode(4)

    root2 = TreeNode(1)
    r2n3 = root2.right = TreeNode(3)

    root3 = TreeNode(None)

    print(u.rightSideView(root1))
    print(u.rightSideView(root2))
    print(u.rightSideView(root3))
