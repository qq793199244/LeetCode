'''
给定一个二叉树，它的每个结点都存放着一个整数值。
找出路径和等于给定数值的路径总数。
路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。
示例：
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1
返回 3。和等于 8 的路径有:
1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    # 双递归，时间复杂度O(n^2)，空间复杂度O(H)
    def pathSum1(self, root, sum):
        def dfs(node, cur_sum):
            if not node:
                return 0
            count = 0
            if node.val == cur_sum:
                count += 1
            count += dfs(node.left, cur_sum-node.val)
            count += dfs(node.right, cur_sum-node.val)
            return count
        if not root:
            return 0
        return dfs(root, sum) + self.pathSum1(root.left, sum) + self.pathSum1(root.right, sum)

    # 前缀和，时间复杂度O(n)，空间复杂度O(H)
    def pathSum2(self, root, sum):
        if not root:
            return 0
        d = {0: 1}
        self.count = 0
        def dfs(root, val, cur_sum, dic):
            if not root:
                return
            cur_sum += root.val
            pre = cur_sum - val
            self.count += dic.get(pre, 0)
            dic[cur_sum] = dic.get(pre, 0) + 1
            dfs(root.left, val, cur_sum, dic)
            dfs(root.right, val, cur_sum, dic)
            dic[cur_sum] -= 1
        dfs(root, sum, 0, d)
        return self.count


if __name__ == '__main__':
    u = Solution()
    root = TreeNode(10)
    n5 = root.left = TreeNode(5)
    n_3 = root.right = TreeNode(-3)
    n31 = n5.left = TreeNode(3)
    n2 = n5.right = TreeNode(2)
    n11 = n_3.right = TreeNode(11)
    n32 = n31.left = TreeNode(3)
    n_2 = n31.right = TreeNode(-2)
    n1 = n2.right = TreeNode(1)
    print(u.pathSum1(root, 8))
    print(u.pathSum2(root, 8))