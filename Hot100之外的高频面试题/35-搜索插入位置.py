'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。
示例 1:
输入: [1,3,5,6], 5
输出: 2
示例 2:
输入: [1,3,5,6], 2
输出: 1
'''
class Solution(object):
    def searchInsert(self, nums, target):
        n = len(nums)
        if n == 0:
            return 0
        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return n
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            if left == right:
                return mid
            if target > nums[mid]:
                left = mid + 1
            if target < nums[mid]:
                right = mid


if __name__ == '__main__':
    u = Solution()
    n1 = [1,3,5,6]
    n2 = [1,3,5,6]
    print(u.searchInsert(n1, 5))
    print(u.searchInsert(n2, 2))