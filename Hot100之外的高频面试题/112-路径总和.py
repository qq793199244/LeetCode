'''
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，
这条路径上所有节点值相加等于目标和。
说明: 叶子节点是指没有子节点的节点。
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    # DFS 时间复杂度O(n)，空间复杂度O(H)，最坏O(n)，平均O(logn)
    def hasPathSum1(self, root, sum):
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == sum
        return self.hasPathSum1(root.left, sum-root.val) or \
               self.hasPathSum1(root.right, sum-root.val)


    # BFS 时间复杂度O(n)，空间复杂度O(n)
    def hasPathSum2(self, root, sum):
        if not root: return False
        from collections import deque
        que_node = deque([root])
        que_val = deque([root.val])
        while que_node:
            now = que_node.popleft()
            tmp = que_val.popleft()
            if not now.left and not now.right:
                if tmp == sum:
                    return True
                continue
            if now.left:
                que_node.append(now.left)
                que_val.append(tmp + now.left.val)
            if now.right:
                que_node.append(now.right)
                que_val.append(tmp + now.right.val)
        return False


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
    n1 = n4_2.right = TreeNode(1)
    print(u.hasPathSum1(root, 22))
    print(u.hasPathSum2(root, 22))