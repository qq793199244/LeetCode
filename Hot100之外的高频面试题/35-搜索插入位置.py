'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为 O(log n) 的算法。
示例 1:
输入: nums = [1,3,5,6], target = 5
输出: 2
示例 2:
输入: nums = [1,3,5,6], target = 2
输出: 1
示例 3:
输入: nums = [1,3,5,6], target = 7
输出: 4
示例 4:
输入: nums = [1,3,5,6], target = 0
输出: 0
示例 5:
输入: nums = [1], target = 0
输出: 0
提示:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums 为无重复元素的升序排列数组
-104 <= target <= 104
'''


class Solution(object):
    def searchInsert(self, nums, target):
        if not nums:
            return 0
        n = len(nums)
        left, right = 0, n - 1
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return n
        while left <= right:
            mid = (left + right) // 2
            if left == right:
                return mid
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid


if __name__ == '__main__':
    u = Solution()
    print(u.searchInsert(nums=[1, 3, 5, 6], target=5))  # 2
    print(u.searchInsert(nums=[1, 3, 5, 6], target=2))  # 1
    print(u.searchInsert(nums=[1, 3, 5, 6], target=7))  # 4
    print(u.searchInsert(nums=[1, 3, 5, 6], target=0))  # 0
    print(u.searchInsert(nums=[1], target=0))  # 0
