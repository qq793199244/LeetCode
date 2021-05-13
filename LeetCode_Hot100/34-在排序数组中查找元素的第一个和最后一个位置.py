'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
进阶：
你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
示例 2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
示例 3：
输入：nums = [], target = 0
输出：[-1,-1]
提示：
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums 是一个非递减数组
-109 <= target <= 109
'''


class Solution:
    # 二分查找。时间复杂度O(logn)，空间复杂度O(1)
    def searchRange(self, nums, target):
        n = len(nums)
        if n == 0:
            return [-1, -1]
        left, right = 0, n - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        if nums[left] != target:
            return [-1, -1]
        L = left
        right = n
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        R = right
        return [L, R-1]


if __name__ == '__main__':
    u = Solution()
    print(u.searchRange([5, 7, 7, 8, 8, 10], 8))
    print(u.searchRange([5, 7, 7, 8, 8, 10], 6))
    print(u.searchRange([], 0))
    print(u.searchRange([8, 8, 8, 8, 8, 8], 8))
