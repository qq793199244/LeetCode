'''
给定一个二叉树，检查它是否是镜像对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
    1
   / \
  2   2
   \   \
   3    3
进阶：
你可以运用递归和迭代两种方法解决这个问题吗？
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归。时间复杂度O(n)，空间复杂度O(Height)
    def isSymmetric(self, root):
        # 递归三部曲①：确定参数（左子节点、右子节点）和返回值（True 或 False）
        def compare(left, right):
            # 递归三部曲②：确定终止条件
            if not left and not right:
                return True
            elif not left and right:
                return False
            elif left and not right:
                return False
            else:
                # 递归三部曲③：确定单层循环逻辑
                if left.val == right.val:
                    return compare(left.left, right.right) and compare(left.right, right.left)
                else:
                    return False

        return compare(root.left, root.right)

    # 迭代，使用栈。时间复杂度O(n)，空间复杂度O(Height)
    def isSymmetric2(self, root):
        if not root:
            return True
        stack = []
        stack.append(root.left)
        stack.append(root.right)
        while stack:
            right = stack.pop()
            left = stack.pop()
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            stack.append(left.left)
            stack.append(right.right)
            stack.append(left.right)
            stack.append(right.left)
        return True

    # 迭代，使用队列。时间复杂度O(n)，空间复杂度O(n)
    def isSymmetric3(self, root):
        if not root:
            return True
        queue = [root.left, root.right]
        while queue:
            left = queue.pop(0)
            right = queue.pop(0)
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        return True


if __name__ == '__main__':
    u = Solution()
    root1 = TreeNode(1)
    l2 = root1.left = TreeNode(2)
    r2 = root1.right = TreeNode(2)
    l3 = l2.left = TreeNode(3)
    l4 = l2.right = TreeNode(4)
    r4 = r2.left = TreeNode(4)
    r3 = r2.right = TreeNode(3)

    root2 = TreeNode(1)
    r2l2 = root2.left = TreeNode(2)
    r2r2 = root2.right = TreeNode(2)
    r2l3 = r2l2.right = TreeNode(3)
    r2r3 = r2r2.right = TreeNode(3)

    root3 = TreeNode(1)
    r3l2 = root3.left = TreeNode(2)

    print(u.isSymmetric(root1))  # True
    print(u.isSymmetric(root2))  # False
    print(u.isSymmetric(root3))  # False

    print(u.isSymmetric2(root1))  # True
    print(u.isSymmetric2(root2))  # False
    print(u.isSymmetric2(root3))  # False

    print(u.isSymmetric3(root1))  # True
    print(u.isSymmetric3(root2))  # False
    print(u.isSymmetric3(root3))  # False
