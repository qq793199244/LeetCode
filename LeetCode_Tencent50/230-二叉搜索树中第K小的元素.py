'''
给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。
示例 1：
输入：root = [3,1,4,null,2], k = 1
输出：1
示例 2：
输入：root = [5,3,6,2,4,null,null,1], k = 3
输出：3
提示：
树中的节点数为 n 。
1 <= k <= n <= 10^4
0 <= Node.val <= 10^4
进阶：如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？
'''


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # 中序遍历递归。时间复杂度O(n)，空间复杂度O(n)
    def kthSmallest(self, root, k):
        seq = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            seq.append(node.val)
            inorder(node.right)

        inorder(root)
        return seq[k - 1]

    # 中序遍历+计数。时间复杂度O(n)，空间复杂度O(H)
    def kthSmallest2(self, root, k):
        count = 0
        if not root:
            return
        leftRes = self.kthSmallest(root.left, k)
        if leftRes:
            return leftRes
        count += 1
        if count == k:
            return root.val
        return self.kthSmallest(root.right, k)

'''进阶
在节点定义中增加一个变量，记录该节点在BST中是第几小，这个变量也是满足BST的属性的。
这样就能通过k和该变量的对比来选择往左或往右，在logN的时间复杂度完成一次查找。但貌似力扣不能改结构。
'''

if __name__ == '__main__':
    u = Solution()
    root1 = TreeNode(3)
    r1_n1 = root1.left = TreeNode(1)
    r1_n2 = r1_n1.right = TreeNode(2)
    r1_n4 = root1.right = TreeNode(4)
    print(u.kthSmallest(root1, 1))  # 1
    print(u.kthSmallest2(root1, 1))  # 1

    root2 = TreeNode(5)
    r2_n3 = root2.left = TreeNode(3)
    r2_n6 = root2.right = TreeNode(6)
    r2_n2 = r2_n3.left = TreeNode(2)
    r2_n4 = r2_n3.right = TreeNode(4)
    r2_n1 = r2_n2.left = TreeNode(1)
    print(u.kthSmallest(root2, 3))  # 3
    print(u.kthSmallest2(root2, 3))  # 3
