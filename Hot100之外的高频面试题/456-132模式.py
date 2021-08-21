'''
给你一个整数数组 nums ，数组中共有 n 个整数。
132 模式的子序列 由三个整数 nums[i]、nums[j] 和 nums[k] 组成，并同时满足：i < j < k 和 nums[i] < nums[k] < nums[j] 。
如果 nums 中存在 132 模式的子序列 ，返回 true ；否则，返回 false 。
示例 1：
输入：nums = [1,2,3,4]
输出：false
解释：序列中不存在 132 模式的子序列。
示例 2：
输入：nums = [3,1,4,2]
输出：true
解释：序列中有 1 个 132 模式的子序列： [1, 4, 2] 。
示例 3：
输入：nums = [-1,3,2,0]
输出：true
解释：序列中有 3 个 132 模式的的子序列：[-1, 3, 2]、[-1, 3, 0] 和 [-1, 2, 0] 。
'''


class Solution:
    # 暴力法超时。时间复杂度O(n^3)，空间复杂度O(1)
    def find132pattern(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                for k in range(j, n):
                    if nums[i] < nums[k] < nums[j]:
                        return True
        return False

    # 暴力降维，也超时。时间复杂度O(n^2)，空间复杂度O(1)
    def find132pattern2(self, nums):
        n = len(nums)
        leftMin = nums[0]
        for j in range(n - 1):
            for k in range(j + 1, n):
                if leftMin < nums[k] < nums[j]:
                    return True
                leftMin = min(leftMin, nums[j])
        return False

    # 单调栈。时间复杂度O(n)，空间复杂度O(n)
    def find132pattern3(self, nums):
        stack = []
        n = len(nums)
        k = float('-inf')
        for i in range(n - 1, -1, -1):
            if nums[i] < k:
                return True
            while stack and stack[-1] < nums[i]:
                k = max(k, stack.pop())
            stack.append(nums[i])
        return False


if __name__ == '__main__':
    u = Solution()
    print(u.find132pattern([1, 2, 3, 4]))  # False
    print(u.find132pattern([3, 1, 4, 2]))  # True
    print(u.find132pattern([-1, 3, 2, 0]))  # True

    print(u.find132pattern2([1, 2, 3, 4]))  # False
    print(u.find132pattern2([3, 1, 4, 2]))  # True
    print(u.find132pattern2([-1, 3, 2, 0]))  # True

    print(u.find132pattern3([1, 2, 3, 4]))  # False
    print(u.find132pattern3([3, 1, 4, 2]))  # True
    print(u.find132pattern3([-1, 3, 2, 0]))  # True
